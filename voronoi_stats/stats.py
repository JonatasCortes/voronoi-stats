from __future__ import annotations

from datetime import date
from typing import NamedTuple

from voronoi_stats.constants import (
    ACTIVITY_KEYS,
    MAX_LANGUAGES,
    MIN_AREA_SHARE,
    OPACITY_MAX,
    OPACITY_MIN,
    OTHER_LABEL,
)
from voronoi_stats.github import GitHubData, Repository, WeeklyActivity


# ── Report types (the only input of the renderer) ───────────────────────────
class LanguageShare(NamedTuple):
    name: str
    size: int  # bytes of code
    percent: float  # real share, 0-100 (shown in the legend)
    area_weight: float  # share used for the territory area, 0-1 (sums to 1)
    rank: int  # 0 = biggest language; "Other" is always last


class RepoCell(NamedTuple):
    repo: str
    language: str  # name of a LanguageShare
    size: int  # bytes of this repo in that language
    opacity: float  # OPACITY_MIN..OPACITY_MAX, from the recency of the last push


class ActivityMetric(NamedTuple):
    key: str  # one of ACTIVITY_KEYS
    total: int
    values: tuple[int, ...]  # one value per week, oldest first


class Totals(NamedTuple):
    repos: int
    stars: int
    forks: int


class StatsReport(NamedTuple):
    username: str
    languages: tuple[LanguageShare, ...]
    cells: tuple[RepoCell, ...]
    metrics: tuple[ActivityMetric, ...]
    totals: Totals


# ── Languages ───────────────────────────────────────────────────────────────
def _by_size_then_name(item: tuple[str, int]) -> tuple[int, str]:
    """Sort key: biggest first; equal sizes are ordered by name (deterministic)."""
    return (-item[1], item[0])


def _area_weights(shares: list[float]) -> list[float]:
    """Give every language at least MIN_AREA_SHARE of the area.

    Small languages are raised to the minimum and the other ones are scaled down
    to pay for it. Scaling can push another language under the minimum, so the
    loop repeats until nobody is under it.
    """
    floored: set[int] = set()
    while True:
        free: float = 1.0 - MIN_AREA_SHARE * len(floored)
        big_total: float = sum(
            share for i, share in enumerate(shares) if i not in floored)
        if big_total <= 0.0:
            return [1.0 / len(shares)] * len(shares)
        weights: list[float] = [
            MIN_AREA_SHARE if i in floored else share * free / big_total
            for i, share in enumerate(shares)
        ]
        newly_small: set[int] = {
            i for i, weight in enumerate(weights) if i not in floored and weight < MIN_AREA_SHARE
        }
        if not newly_small:
            return weights
        floored |= newly_small


def _build_languages(repositories: tuple[Repository, ...]) -> tuple[LanguageShare, ...]:
    totals: dict[str, int] = {}
    for repository in repositories:
        for language in repository.languages:
            totals[language.name] = totals.get(
                language.name, 0) + language.size

    ranked: list[tuple[str, int]] = sorted(
        totals.items(), key=_by_size_then_name)
    top: list[tuple[str, int]] = ranked[:MAX_LANGUAGES]
    rest: list[tuple[str, int]] = ranked[MAX_LANGUAGES:]
    if rest:
        top.append((OTHER_LABEL, sum(size for _, size in rest)))

    grand_total: int = sum(size for _, size in top)
    if grand_total <= 0:
        return ()

    shares: list[float] = [size / grand_total for _, size in top]
    weights: list[float] = _area_weights(shares)
    return tuple(
        LanguageShare(
            name=name,
            size=size,
            percent=shares[rank] * 100.0,
            area_weight=weights[rank],
            rank=rank,
        )
        for rank, (name, size) in enumerate(top)
    )


# ── Repository cells ────────────────────────────────────────────────────────
def _age_in_weeks(pushed_at: date, today: date) -> int:
    """Whole weeks since the last push (so the opacity does not change every day)."""
    return max(0, (today - pushed_at).days) // 7


def _opacity(age: int, youngest: int, oldest: int) -> float:
    """Oldest push -> OPACITY_MIN, newest push -> OPACITY_MAX, linear in between."""
    if oldest == youngest:
        return OPACITY_MAX
    freshness: float = (oldest - age) / (oldest - youngest)
    return OPACITY_MIN + (OPACITY_MAX - OPACITY_MIN) * freshness


def _build_cells(
    repositories: tuple[Repository, ...],
    languages: tuple[LanguageShare, ...],
    today: date,
) -> tuple[RepoCell, ...]:
    rank_of: dict[str, int] = {
        language.name: language.rank for language in languages}

    # One cell per (repo, language). Languages outside the top ones are merged
    # into "Other", so a repo gets at most one "Other" cell.
    pending: list[tuple[Repository, dict[str, int]]] = []
    for repository in repositories:
        sizes: dict[str, int] = {}
        for language in repository.languages:
            name: str = language.name if language.name in rank_of else OTHER_LABEL
            sizes[name] = sizes.get(name, 0) + language.size
        if sizes:
            pending.append((repository, sizes))

    if not pending:
        return ()

    ages: list[int] = [_age_in_weeks(
        repo.pushed_at.date(), today) for repo, _ in pending]
    youngest: int = min(ages)
    oldest: int = max(ages)

    cells: list[RepoCell] = []
    for (repository, sizes), age in zip(pending, ages):
        opacity: float = _opacity(age, youngest, oldest)
        for name, size in sizes.items():
            if size > 0:
                cells.append(RepoCell(repository.name, name, size, opacity))

    # Fixed order: language rank, then biggest cell first, then repo name.
    cells.sort(key=lambda cell: (
        rank_of[cell.language], -cell.size, cell.repo))
    return tuple(cells)


# ── Activity and totals ─────────────────────────────────────────────────────
def _week_value(week: WeeklyActivity, key: str) -> int:
    if key == "commits":
        return week.commits
    if key == "pull_requests":
        return week.pull_requests
    if key == "issues":
        return week.issues
    if key == "reviews":
        return week.reviews
    raise ValueError(f"Unknown activity key: {key}")


def _build_metrics(weeks: tuple[WeeklyActivity, ...]) -> tuple[ActivityMetric, ...]:
    metrics: list[ActivityMetric] = []
    for key in ACTIVITY_KEYS:
        values: tuple[int, ...] = tuple(
            _week_value(week, key) for week in weeks)
        metrics.append(ActivityMetric(
            key=key, total=sum(values), values=values))
    return tuple(metrics)


def _build_totals(repositories: tuple[Repository, ...]) -> Totals:
    return Totals(
        repos=len(repositories),
        stars=sum(repository.stars for repository in repositories),
        forks=sum(repository.forks for repository in repositories),
    )


# ── Public entry point ──────────────────────────────────────────────────────
def build_report(data: GitHubData, today: date) -> StatsReport:
    """Combine everything into the single object the renderer needs."""
    languages: tuple[LanguageShare, ...] = _build_languages(data.repositories)
    return StatsReport(
        username=data.username,
        languages=languages,
        cells=_build_cells(data.repositories, languages, today),
        metrics=_build_metrics(data.weeks),
        totals=_build_totals(data.repositories),
    )
