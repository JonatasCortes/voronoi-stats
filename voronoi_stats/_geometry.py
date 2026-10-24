from __future__ import annotations
import hashlib
import math
from typing import Final, NamedTuple
from voronoi_stats._constants import (
    DOMINANT_SHARE,
    POWER_MAX_ITER,
    POWER_STEP,
    POWER_TOLERANCE,
    SEED_MARGIN,
)
from voronoi_stats._stats import LanguageShare, RepoCell, StatsReport

Point = tuple[float, float]
Polygon = list[Point]

# rounds that move repo points to their cell centers
_RELAX_STEPS: Final[int] = 3
# tries to find a hash point inside a territory
_SEED_ATTEMPTS: Final[int] = 64
_MIN_SLOPE: Final[float] = 0.5  # keeps weight steps small for odd-shaped cells
# extra damping: long thin cells oscillate with the full step
_STEP_SCALE: Final[float] = 0.5


# ── Result types ────────────────────────────────────────────────────────────
class Bounds(NamedTuple):
    x: float
    y: float
    width: float
    height: float


class TerritoryShape(NamedTuple):
    language: str
    polygon: tuple[Point, ...]


class CellShape(NamedTuple):
    cell: RepoCell  # repo, language, opacity and active flag
    polygon: tuple[Point, ...]
    center: Point  # where to draw the dot


class TerritoryMap(NamedTuple):
    territories: tuple[TerritoryShape, ...]
    cells: tuple[CellShape, ...]


# ── Polygon basics ──────────────────────────────────────────────────────────
def _area(polygon: Polygon) -> float:
    if len(polygon) < 3:
        return 0.0
    total: float = 0.0
    for index, (x1, y1) in enumerate(polygon):
        x2, y2 = polygon[(index + 1) % len(polygon)]
        total += x1 * y2 - x2 * y1
    return abs(total) / 2.0


def _perimeter(polygon: Polygon) -> float:
    total: float = 0.0
    for index, (x1, y1) in enumerate(polygon):
        x2, y2 = polygon[(index + 1) % len(polygon)]
        total += math.hypot(x2 - x1, y2 - y1)
    return total


def _centroid(polygon: Polygon) -> Point:
    """Center of mass of the polygon (plain average if it is almost flat)."""
    twice_area: float = 0.0
    sum_x: float = 0.0
    sum_y: float = 0.0
    for index, (x1, y1) in enumerate(polygon):
        x2, y2 = polygon[(index + 1) % len(polygon)]
        cross: float = x1 * y2 - x2 * y1
        twice_area += cross
        sum_x += (x1 + x2) * cross
        sum_y += (y1 + y2) * cross
    if abs(twice_area) < 1e-9:
        count: int = max(1, len(polygon))
        return (sum(x for x, _ in polygon) / count, sum(y for _, y in polygon) / count)
    return (sum_x / (3.0 * twice_area), sum_y / (3.0 * twice_area))


def _contains(polygon: Polygon, point: Point) -> bool:
    """Ray casting: count how many edges a horizontal ray from the point crosses."""
    px, py = point
    inside: bool = False
    for index, (x1, y1) in enumerate(polygon):
        x2, y2 = polygon[(index + 1) % len(polygon)]
        if (y1 > py) != (y2 > py):
            crossing_x: float = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            if px < crossing_x:
                inside = not inside
    return inside


def _clip(polygon: Polygon, nx: float, ny: float, limit: float) -> Polygon:
    """Keep the part of the polygon where nx*x + ny*y <= limit."""
    result: Polygon = []
    for index, current in enumerate(polygon):
        previous: Point = polygon[index - 1]
        current_value: float = nx * current[0] + ny * current[1] - limit
        previous_value: float = nx * previous[0] + ny * previous[1] - limit
        if (current_value <= 0.0) != (previous_value <= 0.0):
            t: float = previous_value / (previous_value - current_value)
            result.append(
                (
                    previous[0] + t * (current[0] - previous[0]),
                    previous[1] + t * (current[1] - previous[1]),
                )
            )
        if current_value <= 0.0:
            result.append(current)
    return result


def _rectangle(bounds: Bounds) -> Polygon:
    x, y, w, h = bounds
    return [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]


# ── Weighted Voronoi ────────────────────────────────────────────────────────
def _power_cells(sites: list[Point], weights: list[float], region: Polygon) -> list[Polygon]:
    """Cut `region` into one cell per site, given the current weights.

    A point belongs to site i when (distance to i)² - weight_i is the smallest.
    For each pair (i, j) that rule is a straight line, so each cell is the
    region cut by one line per neighbor.
    """
    cells: list[Polygon] = []
    for i, (xi, yi) in enumerate(sites):
        polygon: Polygon = list(region)
        for j, (xj, yj) in enumerate(sites):
            if i == j:
                continue
            limit: float = xj * xj + yj * yj - xi * \
                xi - yi * yi + weights[i] - weights[j]
            polygon = _clip(polygon, 2.0 * (xj - xi), 2.0 * (yj - yi), limit)
            if not polygon:
                break
        cells.append(polygon)
    return cells


def _fit_cells(sites: list[Point], targets: list[float], region: Polygon) -> list[Polygon]:
    """Adjust the weights until every cell area is close to its target area.

    Stops when all cells are within POWER_TOLERANCE of the target, or after
    POWER_MAX_ITER rounds (then the best result so far is used).
    """
    weights: list[float] = [0.0] * len(sites)
    cells: list[Polygon] = _power_cells(sites, weights, region)
    for _ in range(POWER_MAX_ITER):
        areas: list[float] = [_area(cell) for cell in cells]
        if all(abs(area - target) <= POWER_TOLERANCE * target for area, target in zip(areas, targets)):
            break
        for i, cell in enumerate(cells):
            slope: float = 2.0
            if areas[i] > 0.0:
                # How fast the area reacts to the weight, for a cell of this size.
                slope = _perimeter(cell) / \
                    (4.0 * math.sqrt(areas[i] / math.pi))
            weights[i] += _STEP_SCALE * POWER_STEP * \
                (targets[i] - areas[i]) / max(slope, _MIN_SLOPE)
        mean: float = sum(weights) / len(weights)  # only differences matter
        weights = [weight - mean for weight in weights]
        cells = _power_cells(sites, weights, region)
    return cells


# ── Level 1: territories ────────────────────────────────────────────────────
def _territory_sites(languages: tuple[LanguageShare, ...], bounds: Bounds) -> list[Point]:
    """Starting points: the biggest language on the right, the others in a left column."""
    if len(languages) == 1:
        return [(bounds.x + bounds.width / 2.0, bounds.y + bounds.height / 2.0)]

    column_width: float = bounds.width * (1.0 - DOMINANT_SHARE)
    sites: list[Point] = [
        (
            bounds.x + column_width + bounds.width * DOMINANT_SHARE / 2.0,
            bounds.y + bounds.height / 2.0,
        )
    ]
    others: tuple[LanguageShare, ...] = languages[1:]
    others_total: float = sum(language.area_weight for language in others)
    used: float = 0.0
    for language in others:
        middle: float = (used + language.area_weight / 2.0) / others_total
        sites.append((bounds.x + column_width / 2.0,
                     bounds.y + bounds.height * middle))
        used += language.area_weight
    return sites


def _build_territories(
    languages: tuple[LanguageShare, ...], bounds: Bounds
) -> list[Polygon]:
    region: Polygon = _rectangle(bounds)
    if len(languages) == 1:
        return [region]
    total_area: float = bounds.width * bounds.height
    targets: list[float] = [language.area_weight *
                            total_area for language in languages]
    return _fit_cells(_territory_sites(languages, bounds), targets, region)


# ── Level 2: repo cells inside a territory ──────────────────────────────────
def _hash_unit(text: str) -> tuple[float, float]:
    """Two stable numbers in [0, 1) from a text (same text -> same numbers)."""
    digest: bytes = hashlib.sha256(text.encode("utf-8")).digest()
    return (
        int.from_bytes(digest[0:4], "big") / 4294967296.0,
        int.from_bytes(digest[4:8], "big") / 4294967296.0,
    )


def _seed_inside(region: Polygon, key: str) -> Point:
    """A stable starting point for `key` that lies inside `region`."""
    xs: list[float] = [x for x, _ in region]
    ys: list[float] = [y for _, y in region]
    min_x, max_x, min_y, max_y = min(xs), max(xs), min(ys), max(ys)
    span: float = 1.0 - 2.0 * SEED_MARGIN
    for attempt in range(_SEED_ATTEMPTS):
        u, v = _hash_unit(f"{key}|{attempt}")
        point: Point = (
            min_x + (max_x - min_x) * (SEED_MARGIN + span * u),
            min_y + (max_y - min_y) * (SEED_MARGIN + span * v),
        )
        if _contains(region, point):
            return point
    return _centroid(region)


def _build_cells_in(region: Polygon, language: str, cells: list[RepoCell]) -> list[Polygon]:
    if len(cells) == 1:
        return [region]
    total_size: int = sum(cell.size for cell in cells)
    region_area: float = _area(region)
    targets: list[float] = [cell.size /
                            total_size * region_area for cell in cells]

    sites: list[Point] = [_seed_inside(
        region, f"{language}|{cell.repo}") for cell in cells]
    polygons: list[Polygon] = _fit_cells(sites, targets, region)
    # Spread the points out: move each one to the center of its cell, then refit.
    for _ in range(_RELAX_STEPS):
        sites = [
            _centroid(polygon) if len(polygon) >= 3 else site
            for site, polygon in zip(sites, polygons)
        ]
        polygons = _fit_cells(sites, targets, region)
    return polygons


# ── Public entry point ──────────────────────────────────────────────────────
def build_territory_map(report: StatsReport, bounds: Bounds) -> TerritoryMap:
    """Compute every territory and cell polygon, in the coordinates of `bounds`."""
    if not report.languages:
        return TerritoryMap((), ())

    polygons: list[Polygon] = _build_territories(report.languages, bounds)
    territories: list[TerritoryShape] = []
    cell_shapes: list[CellShape] = []

    for language, region in zip(report.languages, polygons):
        territories.append(TerritoryShape(language.name, tuple(region)))
        if len(region) < 3:
            continue
        members: list[RepoCell] = [
            cell for cell in report.cells if cell.language == language.name]
        if not members:
            continue
        for cell, polygon in zip(members, _build_cells_in(region, language.name, members)):
            if len(polygon) >= 3:
                cell_shapes.append(
                    CellShape(cell, tuple(polygon), _centroid(polygon)))

    return TerritoryMap(tuple(territories), tuple(cell_shapes))
