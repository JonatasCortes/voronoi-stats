"""All tunable values for voronoi-stats. Every other file reads from here.

Output must be deterministic: same data -> same SVG, byte for byte.
Never use unseeded random, Python's hash(), or dates inside the SVG.

Every constant is annotated with ``Final`` and an explicit type so the module
passes Pylance/Pyright strict mode. Requires Python 3.9+.
"""

from types import MappingProxyType
from typing import Final, Mapping

# ── Output / API ────────────────────────────────────────────────────────────
OUTPUT_PATH: Final[str] = "assets/stats.svg"
TOKEN_ENV: Final[str] = "GH_TOKEN"
GRAPHQL_URL: Final[str] = "https://api.github.com/graphql"
REPOS_PAGE_SIZE: Final[int] = 50      # repositories per GraphQL page
LANGS_PER_REPO: Final[int] = 20       # language edges requested per repository

# ── Data rules ──────────────────────────────────────────────────────────────
# top N languages; the rest become "Other"
MAX_LANGUAGES: Final[int] = 5
OTHER_LABEL: Final[str] = "Other"
# minimum territory area (2.5%) so small languages stay visible
MIN_AREA_SHARE: Final[float] = 0.025
# push within this window -> pulsing cyan dot
ACTIVE_DAYS: Final[int] = 90
WEEKS: Final[int] = 52                # weekly points per activity chart
ACTIVITY_KEYS: Final[tuple[str, ...]] = (
    "commits", "pull_requests", "issues", "reviews")

OPACITY_MIN: Final[float] = 0.15
OPACITY_MAX: Final[float] = 0.55

# ── Card layout (px) ────────────────────────────────────────────────────────
CARD_W: Final[int] = 880
CARD_RADIUS: Final[int] = 15
CARD_STROKE: Final[float] = 2.0
PAD: Final[int] = 22                  # inner padding of the card

HEADER_Y: Final[int] = 22             # top of the header row
HEADER_BAR_W: Final[int] = 4
HEADER_BAR_H: Final[int] = 22
# title text starts this far right of the bar
TITLE_X_OFFSET: Final[int] = 15
TITLE_BASELINE: Final[int] = 17       # title baseline below HEADER_Y

PLOT_X: Final[int] = PAD
PLOT_Y: Final[int] = 54
PLOT_W: Final[int] = 550
PLOT_H: Final[int] = 300              # was 230 in the prototype
PLOT_RADIUS: Final[int] = 10

LEGEND_GAP: Final[int] = 16           # space between plot and legend
# fixed legend height; render.py must fit inside it
LEGEND_H: Final[int] = 110

CARD_PAD_BOTTOM: Final[int] = PAD
CARD_H: Final[int] = PLOT_Y + PLOT_H + \
    LEGEND_GAP + LEGEND_H + CARD_PAD_BOTTOM  # 502

ACTIVITY_X: Final[int] = 598          # left edge of the activity column
# width of the activity column (ends at x=858)
ACTIVITY_W: Final[int] = 260
# line chart starts this far right of ACTIVITY_X
SPARK_X_OFFSET: Final[int] = 126
ACTIVITY_ROW_COUNT: Final[int] = 4
# height reserved for REPOS / STARS / FORKS at the bottom
FOOTER_STATS_H: Final[int] = 62

# ── Geometry (weighted Voronoi) ─────────────────────────────────────────────
POWER_MAX_ITER: Final[int] = 200      # max weight-adjustment iterations
# stop when every cell area is within 1% of its target
POWER_TOLERANCE: Final[float] = 0.01
POWER_STEP: Final[float] = 0.5        # damping for weight updates (0-1)
# keep initial points this fraction away from the edges
SEED_MARGIN: Final[float] = 0.08
DOMINANT_SHARE: Final[float] = 0.60   # dominant language takes the large block
# (others are stacked in a column on the left)

# ── Drawing ─────────────────────────────────────────────────────────────────
CELL_STROKE_W: Final[float] = 1.4
# wide stroke in the background color (gap effect)
TERRITORY_OUTLINE_W: Final[float] = 3.4
TERRITORY_LINE_W: Final[float] = 1.2      # thin colored stroke on top
TERRITORY_LINE_OPACITY: Final[float] = 0.9
PLOT_BORDER_OPACITY: Final[float] = 0.28
DOT_ACTIVE_R: Final[float] = 2.6
DOT_DORMANT_R: Final[float] = 1.5
DOT_DORMANT_OPACITY: Final[float] = 0.4
SPARK_STROKE_W: Final[float] = 1.6
SPARK_END_R: Final[float] = 2.6
DIVIDER_OPACITY: Final[float] = 0.08
GLOW_OPACITY: Final[float] = 0.16
GLOW_RX: Final[int] = 380
GLOW_RY: Final[int] = 200
# small uppercase labels (COMMITS, REPOS...)
LABEL_TEXT_OPACITY: Final[float] = 0.55
LEGEND_NOTE_OPACITY: Final[float] = 0.5

# Language colors: hue spacing across the theme's hue range.
# "Other" is desaturated vs named languages
OTHER_SATURATION_FACTOR: Final[float] = 0.6

# ── Typography ──────────────────────────────────────────────────────────────
FONT_FAMILY: Final[str] = "Arial,Helvetica,sans-serif"
FONT_TITLE: Final[float] = 18.0
FONT_HEADER: Final[float] = 12.0
FONT_LEGEND: Final[float] = 11.5
FONT_LEGEND_NOTE: Final[float] = 10.0
FONT_METRIC_LABEL: Final[float] = 10.5
FONT_METRIC_VALUE: Final[float] = 28.0
FONT_FOOTER_LABEL: Final[float] = 10.0
FONT_FOOTER_VALUE: Final[float] = 20.0
OUTPUT_DECIMALS: Final[int] = 1           # decimals for coordinates in the SVG

# ── Animation (seconds) ─────────────────────────────────────────────────────
ANIM_CELL_DURATION: Final[float] = 0.9
ANIM_CELL_STEP: Final[float] = 0.04       # stagger between cells
ANIM_CELL_START: Final[float] = 0.15
ANIM_CELL_START_SCALE: Final[float] = 0.55
# outlines and dots fade in after the cells
ANIM_TERRITORY_DELAY: Final[float] = 1.6
ANIM_TERRITORY_DURATION: Final[float] = 1.0
ANIM_SPARK_DELAY: Final[float] = 0.5
ANIM_SPARK_DURATION: Final[float] = 1.8
ANIM_NUM_DELAY: Final[float] = 0.4
ANIM_NUM_DURATION: Final[float] = 0.8
ANIM_PULSE_DELAY: Final[float] = 2.4
ANIM_PULSE_DURATION: Final[float] = 6.0
ANIM_PULSE_MIN_OPACITY: Final[float] = 0.5

# ── Text (change here to translate) ─────────────────────────────────────────
LABELS: Final[Mapping[str, str]] = MappingProxyType(
    {
        "title": "CODE TERRITORY",
        "header_activity": "ACTIVITY · 12 MONTHS",
        "header_hint": "1 cell = 1 repository · area = code",
        "commits": "COMMITS",
        "pull_requests": "PULL REQUESTS",
        "issues": "ISSUES",
        "reviews": "REVIEWS",
        "repos": "REPOS",
        "stars": "STARS",
        "forks": "FORKS",
        # Legend (7 items)
        "legend_languages": "Language color and real share of code",
        "legend_territory": "Territory = language",
        "legend_area": "Area = bytes of code (2.5% minimum so small languages stay visible)",
        "legend_cell": "Cell = repository in that language; multi-language repos appear in each territory",
        "legend_opacity": "Opacity = recency of last push",
        "legend_opacity_old": "oldest",
        "legend_opacity_new": "newest",
        "legend_active": "Pulsing cyan dot = push in the last 90 days",
        "legend_dormant": "White dot = no recent activity",
        "legend_activity": "Right: weekly activity; cyan dot = current week",
        # Accessibility
        "svg_title": "Code Territory",
        "svg_desc": (
            "Weighted Voronoi map of {user}'s repositories: each territory is a language "
            "and each cell is a repository, with area proportional to bytes of code. "
            "Opacity shows how recent the last push was. On the right, weekly activity "
            "for the last 12 months."
        ),
    }
)

# Number formatting (English): thousands with comma, decimal with dot, e.g. 2,847 and 91.2%
THOUSANDS_SEP: Final[str] = ","
DECIMAL_SEP: Final[str] = "."
PERCENT_DECIMALS: Final[int] = 1
