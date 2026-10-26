from __future__ import annotations

import argparse
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from voronoi_stats.constants import OUTPUT_PATH
from voronoi_stats.github import GitHubApiError, GitHubData, fetch_github_data, read_token
from voronoi_stats.render import render_svg
from voronoi_stats.stats import StatsReport, build_report
from voronoi_stats.themes import Theme, get_theme


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


def update_voronoi_stats(username: str, theme_name: str, path: str) -> None:
    theme: Theme = get_theme(theme_name)
    report: StatsReport = run_report_etl(username)
    write_svg(render_svg(report, theme), path)


def main() -> int:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Generate the voronoi-stats SVG for a GitHub profile."
    )
    parser.add_argument("username", help="GitHub username")
    parser.add_argument("--theme", default="neon",
                        help="theme name (default: neon)")
    arguments: argparse.Namespace = parser.parse_args()
    username: str = str(arguments.username)
    theme_name: str = str(arguments.theme)

    try:
        update_voronoi_stats(username, theme_name, OUTPUT_PATH)
    except (GitHubApiError, ValueError) as error:
        print(f"voronoi-stats: {error}", file=sys.stderr)
        return 1
    print(f"voronoi-stats: saved {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    main()
