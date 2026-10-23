from __future__ import annotations
from datetime import date, datetime, timezone
from pathlib import Path
from ._constants import OUTPUT_PATH
from ._github import GitHubData, fetch_github_data, read_token
from ._render import render_svg
from ._stats import StatsReport, build_report
from ._themes import get_theme


def _write_svg(svg: str, path: str = OUTPUT_PATH) -> None:
    """Save the SVG, creating the folder if needed (overwrites an existing file)."""
    target: Path = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    # newline="\n" keeps the bytes identical on every system, so git sees no change
    with target.open("w", encoding="utf-8", newline="\n") as file:
        file.write(svg)


def update_voronoi_stats(username: str, theme: str) -> None:
    """Run the whole pipeline for one user."""
    token: str = read_token()
    today: date = datetime.now(timezone.utc).date()

    data: GitHubData = fetch_github_data(username, token, today)
    report: StatsReport = build_report(data, today)
    _write_svg(render_svg(report, get_theme(theme)))
