from typing import Final, TypedDict


class Theme(TypedDict):
    background: str        # card background and gap between cells
    plot_background: str   # map area background
    text: str              # text, numbers and dormant dots
    accent: str            # title, header bar, line charts, REPOS/STARS/FORKS, glow
    pulse: str             # pulsing dots, chart end dot, header hint text
    border_start: str      # card border gradient start
    border_end: str        # card border gradient end
    hue_start: float       # language hue range start (degrees)
    hue_end: float         # language hue range end (degrees)
    saturation: float      # 0-1
    lightness: float       # 0-1


THEMES: Final[dict[str, Theme]] = {
    # ── 1. Basic colors ─────────────────────────────────────────────────────
    "red": {
        "background": "#0d0d0d", "plot_background": "#141016", "text": "#ff9999",
        "accent": "#ff4257", "pulse": "#ff5a6e",
        "border_start": "#ff3659", "border_end": "#7b142b",
        "hue_start": 355.0, "hue_end": 295.0, "saturation": 0.85, "lightness": 0.55,
    },
    "orange": {
        "background": "#140C07", "plot_background": "#24140B", "text": "#FFEDD5",
        "accent": "#F97316", "pulse": "#FF8C42",
        "border_start": "#FB923C", "border_end": "#C2410C",
        "hue_start": 15.0, "hue_end": 85.0, "saturation": 0.90, "lightness": 0.55,
    },
    "yellow": {
        "background": "#121008", "plot_background": "#211B0D", "text": "#FEF3C7",
        "accent": "#EAB308", "pulse": "#FFE44D",
        "border_start": "#FDE047", "border_end": "#A16207",
        "hue_start": 45.0, "hue_end": 115.0, "saturation": 0.90, "lightness": 0.52,
    },
    "green": {
        "background": "#071510", "plot_background": "#0D211A", "text": "#A7F3D0",
        "accent": "#10B981", "pulse": "#2EEFA6",
        "border_start": "#34D399", "border_end": "#047857",
        "hue_start": 165.0, "hue_end": 95.0, "saturation": 0.75, "lightness": 0.48,
    },
    "blue": {
        "background": "#080F1F", "plot_background": "#0F1B30", "text": "#BAE6FD",
        "accent": "#3B82F6", "pulse": "#38BDF8",
        "border_start": "#60A5FA", "border_end": "#1D4ED8",
        "hue_start": 225.0, "hue_end": 155.0, "saturation": 0.85, "lightness": 0.58,
    },
    "purple": {
        "background": "#0D0918", "plot_background": "#19112B", "text": "#DDD6FE",
        "accent": "#8B5CF6", "pulse": "#C084FC",
        "border_start": "#A78BFA", "border_end": "#5B21B6",
        "hue_start": 265.0, "hue_end": 335.0, "saturation": 0.80, "lightness": 0.62,
    },
    "pink": {
        "background": "#0D080F", "plot_background": "#1D101D", "text": "#FBCFE8",
        "accent": "#EC4899", "pulse": "#FF4FA3",
        "border_start": "#F472B6", "border_end": "#9D174D",
        "hue_start": 335.0, "hue_end": 395.0, "saturation": 0.85, "lightness": 0.62,
    },

    # ── 2. Year seasons ─────────────────────────────────────────────────────
    "spring": {
        "background": "#21171C", "plot_background": "#35242C", "text": "#E8DCCB",
        "accent": "#B87989", "pulse": "#C5B5D6",
        "border_start": "#D6A6AD", "border_end": "#754957",
        "hue_start": 350.0, "hue_end": 275.0, "saturation": 0.35, "lightness": 0.68,
    },
    "summer": {
        "background": "#201713", "plot_background": "#35231B", "text": "#E7D2AC",
        "accent": "#C16F48", "pulse": "#8DB4A8",
        "border_start": "#E0B56D", "border_end": "#81452F",
        "hue_start": 25.0, "hue_end": 165.0, "saturation": 0.45, "lightness": 0.60,
    },
    "autumn": {
        "background": "#191A16", "plot_background": "#292D22", "text": "#E2D5B9",
        "accent": "#B96345", "pulse": "#E0B66F",
        "border_start": "#D5A15E", "border_end": "#8D4937",
        "hue_start": 12.0, "hue_end": 85.0, "saturation": 0.42, "lightness": 0.58,
    },
    "winter": {
        "background": "#191B22", "plot_background": "#272B35", "text": "#E8E3DA",
        "accent": "#71899D", "pulse": "#B7A9BD",
        "border_start": "#9FB9C8", "border_end": "#465363",
        "hue_start": 207.0, "hue_end": 285.0, "saturation": 0.30, "lightness": 0.66,
    },

    # ── 3. Drinks ───────────────────────────────────────────────────────────
    "wine": {
        "background": "#190B10", "plot_background": "#2A101B", "text": "#E7D5BC",
        "accent": "#A65368", "pulse": "#E0B56F",
        "border_start": "#C06A78", "border_end": "#5B1E35",
        "hue_start": 340.0, "hue_end": 410.0, "saturation": 0.50, "lightness": 0.55,
    },
    "beer": {
        "background": "#1C1510", "plot_background": "#302219", "text": "#E8D7B5",
        "accent": "#B96D32", "pulse": "#D5B86A",
        "border_start": "#E5A642", "border_end": "#8C4225",
        "hue_start": 35.0, "hue_end": 100.0, "saturation": 0.65, "lightness": 0.52,
    },

    # ── 4. Countries and culture ────────────────────────────────────────────
    "brazil": {
        "background": "#0C1714", "plot_background": "#172720", "text": "#E8E2C9",
        "accent": "#249B72", "pulse": "#F4C84A",
        "border_start": "#F4C84A", "border_end": "#16845D",
        "hue_start": 160.0, "hue_end": 45.0, "saturation": 0.80, "lightness": 0.48,
    },
    "usa": {
        "background": "#0A1128", "plot_background": "#152238", "text": "#FFFFFF",
        "accent": "#E61C38", "pulse": "#FFFFFF",
        "border_start": "#E61C38", "border_end": "#1E3A8A",
        "hue_start": 352.0, "hue_end": 217.0, "saturation": 0.80, "lightness": 0.55,
    },
    "france": {
        "background": "#0A0E1A", "plot_background": "#151C2E", "text": "#FFFFFF",
        "accent": "#ED2939", "pulse": "#3B82F6",
        "border_start": "#ED2939", "border_end": "#0055A5",
        "hue_start": 220.0, "hue_end": 355.0, "saturation": 0.75, "lightness": 0.56,
    },
    "india": {
        "background": "#0D111A", "plot_background": "#182232", "text": "#FFFFFF",
        "accent": "#FF7A00", "pulse": "#10B981",
        "border_start": "#FF7A00", "border_end": "#059669",
        "hue_start": 29.0, "hue_end": 160.0, "saturation": 0.85, "lightness": 0.52,
    },
    "china": {
        "background": "#120608", "plot_background": "#240C12", "text": "#FFF5E6",
        "accent": "#DE2910", "pulse": "#FFD700",
        "border_start": "#DE2910", "border_end": "#8B0000",
        "hue_start": 5.0, "hue_end": 65.0, "saturation": 0.85, "lightness": 0.50,
    },
    "japan": {
        "background": "#0D0E12", "plot_background": "#1B1D26", "text": "#FFFFFF",
        "accent": "#FF1A3C", "pulse": "#FFFFFF",
        "border_start": "#E60033", "border_end": "#7A001A",
        "hue_start": 345.0, "hue_end": 225.0, "saturation": 0.70, "lightness": 0.55,
    },
    "japanlight": {
        "background": "#F8F9FA", "plot_background": "#E5E7EB", "text": "#111827",
        "accent": "#BC002D", "pulse": "#BC002D",
        "border_start": "#E60033", "border_end": "#990022",
        "hue_start": 345.0, "hue_end": 225.0, "saturation": 0.70, "lightness": 0.45,
    },
    "sakura": {
        "background": "#0F111A", "plot_background": "#1A1D2C", "text": "#F7F2EF",
        "accent": "#FF6B8B", "pulse": "#FF9EAA",
        "border_start": "#FF6B8B", "border_end": "#7C3AED",
        "hue_start": 347.0, "hue_end": 255.0, "saturation": 0.85, "lightness": 0.72,
    },

    # ── 5. Classical UI ─────────────────────────────────────────────────────
    "dracula": {
        "background": "#282A36", "plot_background": "#343746", "text": "#F8F8F2",
        "accent": "#BD93F9", "pulse": "#8BE9FD",
        "border_start": "#50FA7B", "border_end": "#BD93F9",
        "hue_start": 330.0, "hue_end": 135.0, "saturation": 0.85, "lightness": 0.72,
    },
    "mocha": {
        "background": "#1E1E2E", "plot_background": "#242438", "text": "#CDD6F4",
        "accent": "#89B4FA", "pulse": "#94E2D5",
        "border_start": "#89DCEB", "border_end": "#CBA6F7",
        "hue_start": 215.0, "hue_end": 335.0, "saturation": 0.80, "lightness": 0.76,
    },
    "neon": {
        "background": "#080811", "plot_background": "#121324", "text": "#FFFFFF",
        "accent": "#FF0055", "pulse": "#00F0FF",
        "border_start": "#FF0055", "border_end": "#7000FF",
        "hue_start": 340.0, "hue_end": 213.0, "saturation": 1.00, "lightness": 0.50,
    },
    "atlas": {
        "background": "#0B1020", "plot_background": "#151E35", "text": "#D9E4F2",
        "accent": "#647DB8", "pulse": "#E8C878",
        "border_start": "#8299D4", "border_end": "#62528F",
        "hue_start": 222.0, "hue_end": 300.0, "saturation": 0.50, "lightness": 0.62,
    },
    "heaven": {
        "background": "#101C32", "plot_background": "#1C2B43", "text": "#EAF2FA",
        "accent": "#91BCE0", "pulse": "#F2D79A",
        "border_start": "#B8DDF2", "border_end": "#8C83C7",
        "hue_start": 200.0, "hue_end": 270.0, "saturation": 0.60, "lightness": 0.76,
    },
    "hell": {
        "background": "#120B0A", "plot_background": "#261210", "text": "#F2D0A0",
        "accent": "#E74722", "pulse": "#E5AC45",
        "border_start": "#FF8A32", "border_end": "#7B1026",
        "hue_start": 345.0, "hue_end": 405.0, "saturation": 0.80, "lightness": 0.47,
    },
}


def get_theme(theme_name: str) -> Theme:
    """Return a theme by name, ignoring case, spaces, "-" and "_"."""
    key: str = theme_name.lower().strip().replace(
        " ", "").replace("-", "").replace("_", "")
    theme: Theme | None = THEMES.get(key)
    if theme is None:
        available: str = ", ".join(sorted(THEMES))
        raise ValueError(
            f"Theme '{theme_name}' not found. Available: {available}")
    return theme
