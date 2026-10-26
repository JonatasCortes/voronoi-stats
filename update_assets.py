from __future__ import annotations
import argparse
import sys
from voronoi_stats.themes import THEMES
from voronoi_stats.constants import OUTPUT_PATH
from voronoi_stats.github import GitHubApiError
from voronoi_stats.render import render_svg
from voronoi_stats.stats import StatsReport
from voronoi_stats.themes import Theme, get_theme
from voronoi_stats.main import run_report_etl, write_svg


def update_assets():
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Generate all assets for the repository."
    )
    parser.add_argument("username", help="GitHub username")
    arguments: argparse.Namespace = parser.parse_args()
    username: str = str(arguments.username)

    try:
        report: StatsReport = run_report_etl(username)
        for theme_name in THEMES:
            path = OUTPUT_PATH.replace("stats", f"stats_{theme_name}")
            print(f"update: {path}")
            theme: Theme = get_theme(theme_name)
            write_svg(render_svg(report, theme), path)

    except (GitHubApiError, ValueError) as error:
        print(f"voronoi-stats: {error}", file=sys.stderr)
        return 1
    print(f"Successfully updated assets.")
    return 0


if __name__ == "__main__":
    update_assets()
