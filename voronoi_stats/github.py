from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from datetime import date, datetime, time, timedelta, timezone
from typing import Final, NamedTuple, NoReturn, cast

from voronoi_stats.constants import GRAPHQL_URL, LANGS_PER_REPO, REPOS_PAGE_SIZE, GH_TOKEN, WEEKS

JsonObject = dict[str, object]

_TIMEOUT_SECONDS: Final[int] = 30


# ── Types shared with the other modules ─────────────────────────────────────
class GitHubApiError(Exception):
    """Any problem talking to GitHub (missing token, bad user, rate limit...)."""


class LanguageBytes(NamedTuple):
    name: str
    size: int  # bytes of code in this language, inside one repository


class Repository(NamedTuple):
    name: str
    pushed_at: datetime  # timezone-aware (UTC)
    stars: int
    forks: int
    languages: tuple[LanguageBytes, ...]


class WeeklyActivity(NamedTuple):
    week_start: date
    commits: int
    pull_requests: int
    issues: int
    reviews: int


class GitHubData(NamedTuple):
    username: str
    repositories: tuple[Repository, ...]  # no forks, no archived repos
    weeks: tuple[WeeklyActivity, ...]  # WEEKS items, oldest first


# ── Queries ─────────────────────────────────────────────────────────────────
_REPOS_QUERY: Final[str] = """
query($login: String!, $first: Int!, $langs: Int!, $after: String) {
  user(login: $login) {
    repositories(
      first: $first, after: $after, ownerAffiliations: OWNER, isFork: false,
      orderBy: {field: NAME, direction: ASC}
    ) {
      pageInfo { hasNextPage endCursor }
      nodes {
        name
        pushedAt
        createdAt
        stargazerCount
        forkCount
        isArchived
        languages(first: $langs, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name } }
        }
      }
    }
  }
}
"""

_COUNT_FIELDS: Final[str] = (
    "totalCommitContributions "
    "totalPullRequestContributions "
    "totalIssueContributions "
    "totalPullRequestReviewContributions"
)


# ── Small helpers that turn "unknown JSON" into real types ──────────────────
def _as_object(value: object) -> JsonObject:
    if not isinstance(value, dict):
        raise GitHubApiError(
            "Unexpected answer from GitHub (expected an object).")
    return cast("JsonObject", value)


def _as_list(value: object) -> list[object]:
    if not isinstance(value, list):
        raise GitHubApiError(
            "Unexpected answer from GitHub (expected a list).")
    return cast("list[object]", value)


def _as_str(value: object) -> str:
    if not isinstance(value, str):
        raise GitHubApiError("Unexpected answer from GitHub (expected text).")
    return value


def _as_int(value: object) -> int:
    # bool is a subclass of int in Python, so it must be rejected explicitly
    if isinstance(value, bool) or not isinstance(value, int):
        raise GitHubApiError(
            "Unexpected answer from GitHub (expected a number).")
    return value


def _as_bool(value: object) -> bool:
    if not isinstance(value, bool):
        raise GitHubApiError(
            "Unexpected answer from GitHub (expected true/false).")
    return value


def _parse_time(value: object) -> datetime:
    # GitHub sends "2026-10-01T12:00:00Z"; fromisoformat only accepts "Z" on 3.11+
    return datetime.fromisoformat(_as_str(value).replace("Z", "+00:00"))


def _iso(moment: datetime) -> str:
    return moment.strftime("%Y-%m-%dT%H:%M:%SZ")


# ── Talking to the API ──────────────────────────────────────────────────────
def read_token() -> str:
    """Read the token from the environment variable named in constants.py."""
    token: str = os.environ.get(GH_TOKEN, "").strip()
    if not token:
        raise GitHubApiError(
            f"Environment variable {GH_TOKEN} is empty or missing.")
    return token


def _raise_graphql_error(errors: list[object]) -> NoReturn:
    for item in errors:
        error: JsonObject = _as_object(item)
        error_type: object = error.get("type")
        if error_type == "NOT_FOUND":
            raise GitHubApiError("GitHub user not found.")
        if error_type == "RATE_LIMITED":
            raise GitHubApiError("GitHub rate limit reached. Try again later.")
    first: JsonObject = _as_object(errors[0]) if errors else {}
    raise GitHubApiError(f"GitHub API error: {first.get('message')}")


def _run_query(query: str, variables: JsonObject, token: str) -> JsonObject:
    """Send one GraphQL query and return the "data" part of the answer."""
    body: bytes = json.dumps(
        {"query": query, "variables": variables}).encode("utf-8")
    request = urllib.request.Request(
        GRAPHQL_URL,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "voronoi-stats",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=_TIMEOUT_SECONDS) as response:
            raw: bytes = response.read()
    # must come before URLError (subclass)
    except urllib.error.HTTPError as error:
        if error.code == 401:
            raise GitHubApiError(
                f"GitHub rejected the token. Check {GH_TOKEN}.") from error
        if error.code in (403, 429):
            raise GitHubApiError(
                f"GitHub refused the request (HTTP {error.code}): "
                "rate limit or missing permission."
            ) from error
        raise GitHubApiError(f"GitHub returned HTTP {error.code}.") from error
    except urllib.error.URLError as error:
        raise GitHubApiError(
            f"Could not reach GitHub: {error.reason}") from error

    payload: JsonObject = _as_object(json.loads(raw))
    errors: object = payload.get("errors")
    if errors is not None:
        _raise_graphql_error(_as_list(errors))
    return _as_object(payload.get("data"))


def _get_user(data: JsonObject) -> JsonObject:
    user: object = data.get("user")
    if user is None:
        raise GitHubApiError("GitHub user not found.")
    return _as_object(user)


# ── Repositories ────────────────────────────────────────────────────────────
def _parse_repository(node: JsonObject) -> Repository | None:
    """Return None for archived repos (they are left out of the map)."""
    if _as_bool(node.get("isArchived")):
        return None

    # Repos that were never pushed have pushedAt = null: use the creation date.
    pushed: object = node.get("pushedAt")
    moment: datetime = _parse_time(
        pushed if pushed is not None else node.get("createdAt"))

    languages: list[LanguageBytes] = []
    edges: list[object] = _as_list(
        _as_object(node.get("languages")).get("edges"))
    for edge in edges:
        edge_object: JsonObject = _as_object(edge)
        name: str = _as_str(_as_object(edge_object.get("node")).get("name"))
        languages.append(LanguageBytes(name, _as_int(edge_object.get("size"))))

    return Repository(
        name=_as_str(node.get("name")),
        pushed_at=moment,
        stars=_as_int(node.get("stargazerCount")),
        forks=_as_int(node.get("forkCount")),
        languages=tuple(languages),
    )


def _fetch_repositories(username: str, token: str) -> tuple[Repository, ...]:
    repositories: list[Repository] = []
    cursor: str | None = None
    while True:
        variables: JsonObject = {
            "login": username,
            "first": REPOS_PAGE_SIZE,
            "langs": LANGS_PER_REPO,
            "after": cursor,
        }
        data: JsonObject = _run_query(_REPOS_QUERY, variables, token)
        connection: JsonObject = _as_object(
            _get_user(data).get("repositories"))

        for node in _as_list(connection.get("nodes")):
            repository: Repository | None = _parse_repository(_as_object(node))
            if repository is not None:
                repositories.append(repository)

        page_info: JsonObject = _as_object(connection.get("pageInfo"))
        if not _as_bool(page_info.get("hasNextPage")):
            break
        cursor = _as_str(page_info.get("endCursor"))
    return tuple(repositories)


# ── Weekly activity ─────────────────────────────────────────────────────────
def _fetch_weeks(username: str, token: str, today: date) -> tuple[WeeklyActivity, ...]:
    """Ask for WEEKS windows of 7 days in ONE query (one alias per window).

    The last window ends at the end of `today` (UTC). Windows depend only on
    `today`, so the same day always produces the same request.
    """
    end: datetime = datetime.combine(
        today + timedelta(days=1), time.min, tzinfo=timezone.utc)
    starts: list[datetime] = [
        end - timedelta(days=7 * (WEEKS - index)) for index in range(WEEKS)
    ]

    fields: list[str] = []
    for index, start in enumerate(starts):
        stop: datetime = start + timedelta(days=7)
        fields.append(
            f'w{index}: contributionsCollection(from: "{_iso(start)}", to: "{_iso(stop)}") '
            f"{{ {_COUNT_FIELDS} }}"
        )
    query: str = "query($login: String!) { user(login: $login) { " + \
        " ".join(fields) + " } }"

    data: JsonObject = _run_query(query, {"login": username}, token)
    user: JsonObject = _get_user(data)

    weeks: list[WeeklyActivity] = []
    for index, start in enumerate(starts):
        counts: JsonObject = _as_object(user.get(f"w{index}"))
        weeks.append(
            WeeklyActivity(
                week_start=start.date(),
                commits=_as_int(counts.get("totalCommitContributions")),
                pull_requests=_as_int(counts.get(
                    "totalPullRequestContributions")),
                issues=_as_int(counts.get("totalIssueContributions")),
                reviews=_as_int(counts.get(
                    "totalPullRequestReviewContributions")),
            )
        )
    return tuple(weeks)


# ── Public entry point ──────────────────────────────────────────────────────
def fetch_github_data(username: str, token: str, today: date) -> GitHubData:
    """Fetch repositories and weekly activity for `username`."""
    return GitHubData(
        username=username,
        repositories=_fetch_repositories(username, token),
        weeks=_fetch_weeks(username, token, today),
    )
