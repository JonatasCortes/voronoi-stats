from __future__ import annotations

import colorsys
from string import Template
from xml.sax.saxutils import escape

from voronoi_stats.constants import (
    ACTIVITY_ROW_COUNT,
    ACTIVITY_W,
    ACTIVITY_X,
    ANIM_CELL_DURATION,
    ANIM_CELL_START,
    ANIM_CELL_START_SCALE,
    ANIM_CELL_STEP,
    ANIM_NUM_DELAY,
    ANIM_NUM_DURATION,
    ANIM_PULSE_DELAY,
    ANIM_PULSE_DURATION,
    ANIM_PULSE_MIN_OPACITY,
    ANIM_SPARK_DELAY,
    ANIM_SPARK_DURATION,
    ANIM_TERRITORY_DELAY,
    ANIM_TERRITORY_DURATION,
    CARD_H,
    CARD_RADIUS,
    CARD_STROKE,
    CARD_W,
    CELL_STROKE_W,
    DECIMAL_SEP,
    DIVIDER_OPACITY,
    FONT_FAMILY,
    FONT_FOOTER_LABEL,
    FONT_FOOTER_VALUE,
    FONT_HEADER,
    FONT_LEGEND,
    FONT_METRIC_LABEL,
    FONT_METRIC_VALUE,
    FONT_TITLE,
    FOOTER_STATS_H,
    GLOW_OPACITY,
    GLOW_RX,
    GLOW_RY,
    HEADER_BAR_H,
    HEADER_BAR_W,
    HEADER_Y,
    LABEL_TEXT_OPACITY,
    LABELS,
    LEGEND_GAP,
    LEGEND_PAD_Y,
    LEGEND_ROW_H,
    LEGEND_SCALE_GAP,
    LEGEND_SCALE_STEPS,
    LEGEND_SWATCH,
    LEGEND_SWATCH_RADIUS,
    OPACITY_MAX,
    OPACITY_MIN,
    OTHER_LABEL,
    OTHER_SATURATION_FACTOR,
    OUTPUT_DECIMALS,
    PAD,
    PERCENT_DECIMALS,
    PLOT_BORDER_OPACITY,
    PLOT_H,
    PLOT_RADIUS,
    PLOT_W,
    PLOT_X,
    PLOT_Y,
    SPARK_END_R,
    SPARK_STROKE_W,
    SPARK_X_OFFSET,
    TERRITORY_LINE_OPACITY,
    TERRITORY_LINE_W,
    TERRITORY_OUTLINE_W,
    THOUSANDS_SEP,
    TITLE_BASELINE,
    TITLE_X_OFFSET,
)
from voronoi_stats.geometry import Bounds, CellShape, Point, TerritoryMap, build_territory_map
from voronoi_stats.stats import ActivityMetric, LanguageShare, StatsReport, Totals
from voronoi_stats.themes import Theme


# ── Number and text formatting ──────────────────────────────────────────────
def _trim(text: str) -> str:
    """'12.50' -> '12.5', '3.0' -> '3', '-0' -> '0'."""
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return "0" if text in ("", "-0") else text


def _n(value: float) -> str:
    """A coordinate, with OUTPUT_DECIMALS decimals at most."""
    return _trim(f"{value:.{OUTPUT_DECIMALS}f}")


def _t(value: float) -> str:
    """A time or opacity, with 2 decimals at most."""
    return _trim(f"{value:.2f}")


def _points(polygon: tuple[Point, ...]) -> str:
    return " ".join(f"{_n(x)},{_n(y)}" for x, y in polygon)


def format_int(value: int) -> str:
    """2847 -> '2,847' (separator comes from constants.py)."""
    return f"{value:,}".replace(",", THOUSANDS_SEP)


def format_percent(value: float) -> str:
    """91.234 -> '91.2%' (decimal sign comes from constants.py)."""
    return f"{value:.{PERCENT_DECIMALS}f}".replace(".", DECIMAL_SEP) + "%"


# ── Colors ──────────────────────────────────────────────────────────────────
def _hsl_to_hex(hue: float, saturation: float, lightness: float) -> str:
    red, green, blue = colorsys.hls_to_rgb(hue / 360.0, lightness, saturation)
    return f"#{round(red * 255):02x}{round(green * 255):02x}{round(blue * 255):02x}"


def _language_colors(languages: tuple[LanguageShare, ...], theme: Theme) -> dict[str, str]:
    """Spread the languages evenly across the theme's hue range, biggest first."""
    colors: dict[str, str] = {}
    count: int = len(languages)
    for language in languages:
        position: float = language.rank / (count - 1) if count > 1 else 0.0
        hue: float = (theme["hue_start"] + (theme["hue_end"] -
                      theme["hue_start"]) * position) % 360.0
        saturation: float = theme["saturation"]
        if language.name == OTHER_LABEL:
            saturation *= OTHER_SATURATION_FACTOR
        colors[language.name] = _hsl_to_hex(
            hue, saturation, theme["lightness"])
    return colors


# ── Styles and definitions ──────────────────────────────────────────────────
_CSS: Template = Template(
    ".cell{animation:cell-in ${cell_dur}s ease-out both}"
    ".terr{animation:fade-in ${terr_dur}s ease-out ${terr_delay}s both}"
    ".spark{stroke-dasharray:1;stroke-dashoffset:0;"
    "animation:draw ${spark_dur}s ease-out ${spark_delay}s both}"
    ".num{animation:fade-in ${num_dur}s ease-out ${num_delay}s both}"
    ".endpt{animation:fade-in ${num_dur}s ease-out ${end_delay}s both}"
    ".pulse{animation:pulse ${pulse_dur}s ease-in-out ${pulse_delay}s infinite}"
    "@keyframes cell-in{from{opacity:0;transform:scale(${start_scale})}"
    "to{opacity:1;transform:scale(1)}}"
    "@keyframes fade-in{from{opacity:0}to{opacity:1}}"
    "@keyframes draw{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}"
    "@keyframes pulse{0%,100%{opacity:1}50%{opacity:${pulse_min}}}"
    "@media (prefers-reduced-motion:reduce){"
    ".cell,.terr,.spark,.num,.endpt,.pulse{animation:none}}"
)


def _style_block() -> str:
    css: str = _CSS.substitute(
        cell_dur=_t(ANIM_CELL_DURATION),
        terr_dur=_t(ANIM_TERRITORY_DURATION),
        terr_delay=_t(ANIM_TERRITORY_DELAY),
        spark_dur=_t(ANIM_SPARK_DURATION),
        spark_delay=_t(ANIM_SPARK_DELAY),
        num_dur=_t(ANIM_NUM_DURATION),
        num_delay=_t(ANIM_NUM_DELAY),
        end_delay=_t(ANIM_SPARK_DELAY + ANIM_SPARK_DURATION),
        pulse_dur=_t(ANIM_PULSE_DURATION),
        pulse_delay=_t(ANIM_PULSE_DELAY),
        start_scale=_t(ANIM_CELL_START_SCALE),
        pulse_min=_t(ANIM_PULSE_MIN_OPACITY),
    )
    return f"<style>{css}</style>"


def _defs_block(theme: Theme) -> str:
    card_w: str = _n(CARD_W - CARD_STROKE)
    card_h: str = _n(CARD_H - CARD_STROKE)
    half: str = _n(CARD_STROKE / 2.0)
    return (
        "<defs>"
        '<linearGradient id="border" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0" stop-color="{theme["border_start"]}"/>'
        f'<stop offset="1" stop-color="{theme["border_end"]}"/>'
        "</linearGradient>"
        '<radialGradient id="glow">'
        f'<stop offset="0" stop-color="{theme["accent"]}" stop-opacity="{_t(GLOW_OPACITY)}"/>'
        f'<stop offset="1" stop-color="{theme["accent"]}" stop-opacity="0"/>'
        "</radialGradient>"
        f'<clipPath id="card-clip"><rect x="{half}" y="{half}" width="{card_w}" height="{card_h}" '
        f'rx="{CARD_RADIUS}"/></clipPath>'
        f'<clipPath id="plot-clip"><rect x="{PLOT_X}" y="{PLOT_Y}" width="{PLOT_W}" height="{PLOT_H}" '
        f'rx="{PLOT_RADIUS}"/></clipPath>'
        "</defs>"
    )


# ── Card, glow and header ───────────────────────────────────────────────────
def _card_svg(theme: Theme) -> list[str]:
    half: str = _n(CARD_STROKE / 2.0)
    return [
        f'<rect x="{half}" y="{half}" width="{_n(CARD_W - CARD_STROKE)}" '
        f'height="{_n(CARD_H - CARD_STROKE)}" rx="{CARD_RADIUS}" fill="{theme["background"]}" '
        f'stroke="url(#border)" stroke-width="{_t(CARD_STROKE)}"/>',
        f'<ellipse cx="{CARD_W // 2}" cy="{CARD_H // 2}" rx="{GLOW_RX}" ry="{GLOW_RY}" '
        'fill="url(#glow)" clip-path="url(#card-clip)"/>',
    ]


def _header_svg(theme: Theme) -> list[str]:
    baseline: int = HEADER_Y + TITLE_BASELINE
    return [
        f'<rect x="{PAD}" y="{HEADER_Y}" width="{HEADER_BAR_W}" height="{HEADER_BAR_H}" '
        f'rx="2" fill="{theme["accent"]}"/>',
        f'<text x="{PAD + TITLE_X_OFFSET}" y="{baseline}" font-size="{_t(FONT_TITLE)}" '
        f'font-weight="700" letter-spacing="1" fill="{theme["accent"]}">'
        f'{escape(LABELS["title"])}</text>',
        f'<text x="{ACTIVITY_X}" y="{baseline}" font-size="{_t(FONT_HEADER)}" '
        f'letter-spacing="1" fill="{theme["pulse"]}">{escape(LABELS["header_activity"])}</text>',
    ]


# ── Map ─────────────────────────────────────────────────────────────────────
def _cells_svg(cells: tuple[CellShape, ...], colors: dict[str, str], theme: Theme) -> list[str]:
    lines: list[str] = []
    for index, shape in enumerate(cells):
        center_x, center_y = shape.center
        delay: float = ANIM_CELL_START + index * ANIM_CELL_STEP
        lines.append(
            f'<polygon class="cell" points="{_points(shape.polygon)}" '
            f'fill="{colors[shape.cell.language]}" fill-opacity="{_t(shape.cell.opacity)}" '
            f'stroke="{theme["background"]}" stroke-width="{_t(CELL_STROKE_W)}" '
            'stroke-linejoin="round" '
            f'style="transform-origin:{_n(center_x)}px {_n(center_y)}px;'
            f'animation-delay:{_t(delay)}s"/>'
        )
    return lines


def _overlay_svg(tmap: TerritoryMap, colors: dict[str, str], theme: Theme) -> list[str]:
    """Territory outlines (double stroke)."""
    lines: list[str] = ['<g class="terr">']
    for territory in tmap.territories:
        points: str = _points(territory.polygon)
        lines.append(
            f'<polygon points="{points}" fill="none" stroke="{theme["background"]}" '
            f'stroke-width="{_t(TERRITORY_OUTLINE_W)}" stroke-linejoin="round"/>'
        )
        lines.append(
            f'<polygon points="{points}" fill="none" stroke="{colors[territory.language]}" '
            f'stroke-width="{_t(TERRITORY_LINE_W)}" stroke-opacity="{_t(TERRITORY_LINE_OPACITY)}" '
            'stroke-linejoin="round"/>'
        )
    lines.append("</g>")
    return lines


def _plot_svg(tmap: TerritoryMap, colors: dict[str, str], theme: Theme) -> list[str]:
    lines: list[str] = [
        f'<rect x="{PLOT_X}" y="{PLOT_Y}" width="{PLOT_W}" height="{PLOT_H}" '
        f'rx="{PLOT_RADIUS}" fill="{theme["plot_background"]}"/>',
        '<g clip-path="url(#plot-clip)">',
    ]
    lines.extend(_cells_svg(tmap.cells, colors, theme))
    lines.extend(_overlay_svg(tmap, colors, theme))
    lines.append("</g>")
    lines.append(
        f'<rect x="{PLOT_X}" y="{PLOT_Y}" width="{PLOT_W}" height="{PLOT_H}" rx="{PLOT_RADIUS}" '
        f'fill="none" stroke="{theme["accent"]}" stroke-opacity="{_t(PLOT_BORDER_OPACITY)}"/>'
    )
    return lines


# ── Activity column ─────────────────────────────────────────────────────────
def _spark_points(values: tuple[int, ...], x: float, y: float, width: float, height: float) -> list[Point]:
    """Line chart points: the biggest value touches the top, zero touches the bottom."""
    peak: int = max(values) if values else 0
    last: int = len(values) - 1
    points: list[Point] = []
    for index, value in enumerate(values):
        px: float = x + (width * index / last if last > 0 else 0.0)
        py: float = y + height - (height * value / peak if peak > 0 else 0.0)
        points.append((px, py))
    return points


def _metric_svg(metric: ActivityMetric, top: float, row_h: float, theme: Theme) -> list[str]:
    spark_x: float = float(ACTIVITY_X + SPARK_X_OFFSET)
    spark_w: float = float(ACTIVITY_W - SPARK_X_OFFSET)
    lines: list[str] = [
        f'<text x="{ACTIVITY_X}" y="{_n(top + 15)}" font-size="{_t(FONT_METRIC_LABEL)}" '
        f'letter-spacing="1" fill="{theme["text"]}" fill-opacity="{_t(LABEL_TEXT_OPACITY)}">'
        f'{escape(LABELS[metric.key])}</text>',
        f'<text class="num" x="{ACTIVITY_X}" y="{_n(top + row_h - 12)}" '
        f'font-size="{_t(FONT_METRIC_VALUE)}" font-weight="700" fill="{theme["text"]}">'
        f"{format_int(metric.total)}</text>",
    ]
    points: list[Point] = _spark_points(
        metric.values, spark_x, top + 12, spark_w, row_h - 24)
    if points:
        path: str = "M" + " L".join(f"{_n(x)} {_n(y)}" for x, y in points)
        end_x, end_y = points[-1]
        lines.append(
            f'<path class="spark" d="{path}" pathLength="1" fill="none" stroke="{theme["accent"]}" '
            f'stroke-width="{_t(SPARK_STROKE_W)}" stroke-linecap="round" stroke-linejoin="round"/>'
        )
        lines.append(
            f'<g class="endpt"><circle class="pulse" cx="{_n(end_x)}" cy="{_n(end_y)}" '
            f'r="{_t(SPARK_END_R)}" fill="{theme["pulse"]}"/></g>'
        )
    return lines


def _divider(x1: float, x2: float, y: float, theme: Theme) -> str:
    return (
        f'<line x1="{_n(x1)}" y1="{_n(y)}" x2="{_n(x2)}" y2="{_n(y)}" '
        f'stroke="{theme["text"]}" stroke-opacity="{_t(DIVIDER_OPACITY)}"/>'
    )


def _footer_svg(totals: Totals, theme: Theme) -> list[str]:
    top: float = float(PLOT_Y + PLOT_H - FOOTER_STATS_H)
    lines: list[str] = [
        _divider(ACTIVITY_X, ACTIVITY_X + ACTIVITY_W, top, theme)]
    items: tuple[tuple[str, int], ...] = (
        (LABELS["repos"], totals.repos),
        (LABELS["stars"], totals.stars),
        (LABELS["forks"], totals.forks),
    )
    column_w: float = ACTIVITY_W / len(items)
    for index, (label, value) in enumerate(items):
        x: float = ACTIVITY_X + index * column_w
        lines.append(
            f'<text x="{_n(x)}" y="{_n(top + 22)}" font-size="{_t(FONT_FOOTER_LABEL)}" '
            f'letter-spacing="1" fill="{theme["text"]}" fill-opacity="{_t(LABEL_TEXT_OPACITY)}">'
            f"{escape(label)}</text>"
        )
        lines.append(
            f'<text class="num" x="{_n(x)}" y="{_n(top + 22 + FONT_FOOTER_VALUE + 4)}" '
            f'font-size="{_t(FONT_FOOTER_VALUE)}" font-weight="700" fill="{theme["accent"]}">'
            f"{format_int(value)}</text>"
        )
    return lines


def _activity_svg(report: StatsReport, theme: Theme) -> list[str]:
    row_h: float = (PLOT_H - FOOTER_STATS_H) / ACTIVITY_ROW_COUNT
    lines: list[str] = []
    for index, metric in enumerate(report.metrics):
        top: float = PLOT_Y + index * row_h
        if index > 0:
            lines.append(
                _divider(ACTIVITY_X, ACTIVITY_X + ACTIVITY_W, top, theme))
        lines.extend(_metric_svg(metric, top, row_h, theme))
    lines.extend(_footer_svg(report.totals, theme))
    return lines


# ── Legend ──────────────────────────────────────────────────────────────────
# rough width of one character, as a fraction of font size
_TEXT_WIDTH_FACTOR: float = 0.55
_SWATCH_GAP: float = 6.0  # space between a color square and its text
_CHIP_GAP: float = 12.0  # minimum space between two language entries
_TITLE_GAP: float = 6.0  # space between a legend title and its explanation
_SCALE_GAP: float = 8.0  # space between the opacity scale and its two labels


def _text_width(text: str) -> float:
    """Estimated width of a legend text (fonts cannot be measured here)."""
    return len(text) * FONT_LEGEND * _TEXT_WIDTH_FACTOR


def _fit_name(name: str, percent: str, room: float) -> str:
    """Cut a long language name with an ellipsis so "name 12.3%" fits in `room`."""
    if _text_width(f"{name} {percent}") <= room:
        return name
    shown: str = name
    while len(shown) > 1 and _text_width(f"{shown.rstrip()}\u2026 {percent}") > room:
        shown = shown[:-1]
    return shown.rstrip() + "\u2026"


def _legend_svg(report: StatsReport, colors: dict[str, str], theme: Theme) -> list[str]:
    top: float = float(PLOT_Y + PLOT_H + LEGEND_GAP)
    left: float = float(PAD)
    right: float = float(CARD_W - PAD)
    title_color: str = theme["legend_title"]
    text_color: str = theme["legend_text"]

    def row_center(row: int) -> float:
        return top + LEGEND_PAD_Y + row * LEGEND_ROW_H + LEGEND_ROW_H / 2.0

    def baseline(row: int) -> float:
        return row_center(row) + FONT_LEGEND * 0.35

    lines: list[str] = [_divider(left, right, top - LEGEND_GAP / 2.0, theme)]

    # Row 0: color square + name + real share of code, for each language
    if report.languages:
        chip_w: float = (right - left) / len(report.languages)
        for index, language in enumerate(report.languages):
            x: float = left + index * chip_w
            percent: str = format_percent(language.percent)
            room: float = chip_w - LEGEND_SWATCH - _SWATCH_GAP - _CHIP_GAP
            name: str = _fit_name(language.name, percent, room)
            lines.append(
                f'<rect x="{_n(x)}" y="{_n(row_center(0) - LEGEND_SWATCH / 2.0)}" '
                f'width="{LEGEND_SWATCH}" height="{LEGEND_SWATCH}" rx="{_t(LEGEND_SWATCH_RADIUS)}" '
                f'fill="{colors[language.name]}"/>'
            )
            lines.append(
                f'<text x="{_n(x + LEGEND_SWATCH + _SWATCH_GAP)}" y="{_n(baseline(0))}" '
                f'font-size="{_t(FONT_LEGEND)}" fill="{text_color}">{escape(name)} {percent}</text>'
            )

    # Rows 1-3: "Title: explanation" (title and explanation have their own colors)
    for row, key in enumerate(("legend_region", "legend_cell", "legend_opacity"), start=1):
        lines.append(
            f'<text x="{_n(left)}" y="{_n(baseline(row))}" font-size="{_t(FONT_LEGEND)}">'
            f'<tspan font-weight="700" fill="{title_color}">{escape(LABELS[key + "_title"])}</tspan>'
            f'<tspan dx="{_n(_TITLE_GAP)}" fill="{text_color}">{escape(LABELS[key + "_text"])}</tspan>'
            "</text>"
        )

    # Opacity scale (oldest -> newest), at the right end of the Opacity row
    old_label: str = LABELS["legend_opacity_old"]
    new_label: str = LABELS["legend_opacity_new"]
    scale_w: float = float(
        LEGEND_SCALE_STEPS * LEGEND_SWATCH +
        (LEGEND_SCALE_STEPS - 1) * LEGEND_SCALE_GAP
    )
    scale_x: float = right - _text_width(new_label) - _SCALE_GAP - scale_w
    lines.append(
        f'<text x="{_n(scale_x - _SCALE_GAP)}" y="{_n(baseline(3))}" font-size="{_t(FONT_LEGEND)}" '
        f'text-anchor="end" fill="{text_color}">{escape(old_label)}</text>'
    )
    for index in range(LEGEND_SCALE_STEPS):
        opacity: float = OPACITY_MIN + \
            (OPACITY_MAX - OPACITY_MIN) * index / (LEGEND_SCALE_STEPS - 1)
        lines.append(
            f'<rect x="{_n(scale_x + index * (LEGEND_SWATCH + LEGEND_SCALE_GAP))}" '
            f'y="{_n(row_center(3) - LEGEND_SWATCH / 2.0)}" width="{LEGEND_SWATCH}" '
            f'height="{LEGEND_SWATCH}" rx="{_t(LEGEND_SWATCH_RADIUS)}" '
            f'fill="{theme["accent"]}" fill-opacity="{_t(opacity)}"/>'
        )
    lines.append(
        f'<text x="{_n(right)}" y="{_n(baseline(3))}" font-size="{_t(FONT_LEGEND)}" '
        f'text-anchor="end" fill="{text_color}">{escape(new_label)}</text>'
    )
    return lines


# ── Public entry point ──────────────────────────────────────────────────────
def render_svg(report: StatsReport, theme: Theme) -> str:
    """Return the complete SVG text for this report and theme."""
    bounds: Bounds = Bounds(float(PLOT_X), float(
        PLOT_Y), float(PLOT_W), float(PLOT_H))
    territory_map: TerritoryMap = build_territory_map(report, bounds)
    colors: dict[str, str] = _language_colors(report.languages, theme)
    description: str = LABELS["svg_desc"].replace("{user}", report.username)

    parts: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{CARD_W}" height="{CARD_H}" '
        f'viewBox="0 0 {CARD_W} {CARD_H}" font-family="{FONT_FAMILY}" role="img" '
        'aria-labelledby="svg-title svg-desc">',
        f'<title id="svg-title">{escape(LABELS["svg_title"])}</title>',
        f'<desc id="svg-desc">{escape(description)}</desc>',
        _style_block(),
        _defs_block(theme),
    ]
    parts.extend(_card_svg(theme))
    parts.extend(_header_svg(theme))
    parts.extend(_plot_svg(territory_map, colors, theme))
    parts.extend(_activity_svg(report, theme))
    parts.extend(_legend_svg(report, colors, theme))
    parts.append("</svg>")
    return "\n".join(parts) + "\n"
