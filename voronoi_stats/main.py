from __future__ import annotations

import argparse
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from voronoi_stats.constants import OUTPUT_PATH
from voronoi_stats.github import GitHubApiError, GitHubData, fetch_github_data, read_token
from voronoi_stats.render import IDLE_EFFECTS, render_svg
from voronoi_stats.stats import StatsReport, build_report
from voronoi_stats.themes import Theme, get_theme


def _parse_bool(value: str) -> bool:
    """'true' / 'false' (any case) -> bool. Used by --entry."""
    text: str = value.strip().lower()
    if text == "true":
        return True
    if text == "false":
        return False
    raise argparse.ArgumentTypeError(
        f"expected 'true' or 'false', got '{value}'")


def _parse_idle(value: str) -> tuple[str, ...]:
    """'wave, Trace' -> ('wave', 'trace'). 'none' or an empty text -> ()."""
    names: list[str] = [part.strip().lower() for part in value.split(",")]
    return tuple(name for name in names if name not in ("", "none"))


def write_svg(svg: str, path: str) -> None:
    target: Path = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8", newline="\n") as file:
        file.write(svg)


def run_report_etl(username: str) -> StatsReport:
    token: str = read_token()
    today: date = datetime.now(timezone.utc).date()

    data: GitHubData = fetch_github_data(username, token, today)
    return build_report(data, today)


def update_voronoi_stats(
    username: str,
    theme_name: str,
    path: str,
    entry: bool,
    idle: tuple[str, ...],
) -> None:
    theme: Theme = get_theme(theme_name)
    report: StatsReport = run_report_etl(username)
    write_svg(render_svg(report, theme, entry, idle), path)


def main() -> int:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Generate the voronoi-stats SVG for a GitHub profile."
    )
    parser.add_argument("username", help="GitHub username")
    parser.add_argument("--theme", default="neon",
                        help="theme name (default: neon)")
    parser.add_argument("--entry", type=_parse_bool, default=True,
                        help="entry animation, true or false (default: true)")
    parser.add_argument("--idle", type=_parse_idle, default=(),
                        help=f"idle animations separated by comma, or none "
                        f"(available: {', '.join(IDLE_EFFECTS)}; default: none)")
    arguments: argparse.Namespace = parser.parse_args()
    username: str = str(arguments.username)
    theme_name: str = str(arguments.theme)
    entry: bool = bool(arguments.entry)
    idle: tuple[str, ...] = tuple(arguments.idle)

    try:
        update_voronoi_stats(username, theme_name, OUTPUT_PATH, entry, idle)
    except (GitHubApiError, ValueError) as error:
        print(f"voronoi-stats: {error}", file=sys.stderr)
        return 1
    print(f"voronoi-stats: saved {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    main()
