from __future__ import annotations

import argparse
import sys
from voronoi_stats.constants import OUTPUT_PATH
from voronoi_stats.github import GitHubApiError
from voronoi_stats.main import run_report_etl, write_svg
from voronoi_stats.render import IDLE_EFFECTS, render_svg
from voronoi_stats.stats import StatsReport
from voronoi_stats.themes import THEMES, Theme, get_theme

DEMO_THEME: str = "neon"


def _asset_path(suffix: str) -> str:
    """'assets/stats.svg' + 'red' -> 'assets/stats_red.svg'."""
    return OUTPUT_PATH.replace("stats", f"stats_{suffix}")


def _idle_combinations() -> list[tuple[str, ...]]:
    """The demo groups: each effect alone, then all together."""
    groups: list[tuple[str, ...]] = [(effect,) for effect in IDLE_EFFECTS]
    groups.append(IDLE_EFFECTS)
    return groups


def update_assets() -> int:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Generate all assets for the repository."
    )
    parser.add_argument("username", help="GitHub username")
    arguments: argparse.Namespace = parser.parse_args()
    username: str = str(arguments.username)

    try:
        report: StatsReport = run_report_etl(username)

        # One card per theme (entry animation only)
        for theme_name in THEMES:
            path: str = _asset_path(theme_name)
            print(f"update: {path}")
            theme: Theme = get_theme(theme_name)
            write_svg(render_svg(report, theme), path)

        # One card per idle animation and per combination, all in the demo theme
        demo_theme: Theme = get_theme(DEMO_THEME)
        for group in _idle_combinations():
            idle_path: str = _asset_path(
                f"{DEMO_THEME}_idle_{'_'.join(group)}")
            print(f"update: {idle_path}")
            write_svg(render_svg(report, demo_theme, True, group), idle_path)

    except (GitHubApiError, ValueError) as error:
        print(f"voronoi-stats: {error}", file=sys.stderr)
        return 1
    print("Successfully updated assets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(update_assets())
