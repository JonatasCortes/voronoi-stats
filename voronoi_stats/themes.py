from typing import Final, TypedDict


class Theme(TypedDict):
    background: str        # card background and gap between cells
    plot_background: str   # map area background
    text: str              # text and numbers
    accent: str            # title, header bar, line charts, REPOS/STARS/FORKS, glow
    pulse: str             # pulsing chart end dot, header texts
    border_start: str      # card border gradient start
    border_end: str        # card border gradient end
    legend_title: str      # legend titles with their colon ("Area:")
    legend_text: str       # legend explanations and language names
    hue_start: float       # language hue range start (degrees)
    hue_end: float         # language hue range end (degrees)
    saturation: float      # 0-1
    lightness: float       # 0-1


THEMES: Final[dict[str, Theme]] = {

    "red": {
        "background": "#0D0505", "plot_background": "#1A0A0A", "text": "#FFB3B3",
        "accent": "#FF3344", "pulse": "#FF6677",
        "border_start": "#E60012", "border_end": "#660008",
        "legend_title": "#FF8A98", "legend_text": "#FFB3B3",
        "hue_start": 375.0, "hue_end": 295.0, "saturation": 0.85, "lightness": 0.50,
    },
    "orange": {
        "background": "#140C07", "plot_background": "#24140B", "text": "#FFE0C2",
        "accent": "#FB923C", "pulse": "#FF8C42",
        "border_start": "#FB923C", "border_end": "#C2410C",
        "legend_title": "#FDBA74", "legend_text": "#FFE0C2",
        "hue_start": 5.0, "hue_end": 80.0, "saturation": 0.90, "lightness": 0.55,
    },
    "yellow": {
        "background": "#121008", "plot_background": "#211B0D", "text": "#F7ECC0",
        "accent": "#FDE047", "pulse": "#FFE44D",
        "border_start": "#FDE047", "border_end": "#A16207",
        "legend_title": "#FDE68A", "legend_text": "#F7ECC0",
        "hue_start": 25.0, "hue_end": 100.0, "saturation": 0.85, "lightness": 0.50,
    },
    "green": {
        "background": "#051209", "plot_background": "#081F10", "text": "#A7F3D0",
        "accent": "#10B981", "pulse": "#34D399",
        "border_start": "#059669", "border_end": "#064E3B",
        "legend_title": "#6EE7B7", "legend_text": "#A7F3D0",
        "hue_start": 170.0, "hue_end": 70.0, "saturation": 0.80, "lightness": 0.45,
    },
    "blue": {
        "background": "#080F1F", "plot_background": "#0F1B30", "text": "#BAE6FD",
        "accent": "#7DD3FC", "pulse": "#38BDF8",
        "border_start": "#60A5FA", "border_end": "#1D4ED8",
        "legend_title": "#93C5FD", "legend_text": "#BAE6FD",
        "hue_start": 250.0, "hue_end": 150.0, "saturation": 0.85, "lightness": 0.55,
    },
    "purple": {
        "background": "#0D0918", "plot_background": "#19112B", "text": "#DDD6FE",
        "accent": "#C4B5FD", "pulse": "#C084FC",
        "border_start": "#A78BFA", "border_end": "#5B21B6",
        "legend_title": "#B7A5F5", "legend_text": "#DDD6FE",
        "hue_start": 250.0, "hue_end": 340.0, "saturation": 0.80, "lightness": 0.60,
    },
    "pink": {
        "background": "#0D080F", "plot_background": "#1D101D", "text": "#FBCFE8",
        "accent": "#F9A8D4", "pulse": "#FF4FA3",
        "border_start": "#F472B6", "border_end": "#9D174D",
        "legend_title": "#F5B3D6", "legend_text": "#FBCFE8",
        "hue_start": 270.0, "hue_end": 390.0, "saturation": 0.80, "lightness": 0.65,
    },
    "obsidian": {
        "background": "#050505", "plot_background": "#0F0F0F", "text": "#A3A3A3",
        "accent": "#FAFAFA", "pulse": "#FFFFFF",
        "border_start": "#525252", "border_end": "#171717",
        "legend_title": "#D4D4D4", "legend_text": "#A3A3A3",
        "hue_start": 200.0, "hue_end": 280.0, "saturation": 0.35, "lightness": 0.45,
    },

    "mint": {
        "background": "#F0FDF4", "plot_background": "#DCFCE7", "text": "#064E3B",
        "accent": "#047857", "pulse": "#0F766E",
        "border_start": "#059669", "border_end": "#A7F3D0",
        "legend_title": "#065F46", "legend_text": "#064E3B",
        "hue_start": 180.0, "hue_end": 60.0, "saturation": 0.60, "lightness": 0.60,
    },
    "chocomint": {
        "background": "#EAF8EF", "plot_background": "#D6F5E0", "text": "#5A3A24",
        "accent": "#6B4226", "pulse": "#0B7F58",
        "border_start": "#6B4226", "border_end": "#34D399",
        "legend_title": "#7A4B2E", "legend_text": "#5A3A24",
        "hue_start": 180.0, "hue_end": 40.0, "saturation": 0.60, "lightness": 0.65,
    },
    "lavender": {
        "background": "#F3F0FA", "plot_background": "#E7E1F6", "text": "#5B47A8",
        "accent": "#6D28D9", "pulse": "#9333EA",
        "border_start": "#8B5CF6", "border_end": "#DDD6F3",
        "legend_title": "#6D4FD0", "legend_text": "#5B47A8",
        "hue_start": 290.0, "hue_end": 210.0, "saturation": 0.70, "lightness": 0.60,
    },
    "peach": {
        "background": "#FFF4EC", "plot_background": "#FFE6D5", "text": "#7C2D12",
        "accent": "#C2410C", "pulse": "#D94A12",
        "border_start": "#F28B5B", "border_end": "#FFD3B8",
        "legend_title": "#C4511E", "legend_text": "#7C2D12",
        "hue_start": 310.0, "hue_end": 390.0, "saturation": 0.70, "lightness": 0.75,
    },
    "sky": {
        "background": "#F0F9FF", "plot_background": "#E0F2FE", "text": "#0C4A6E",
        "accent": "#0369A1", "pulse": "#0284C7",
        "border_start": "#0284C7", "border_end": "#BAE6FD",
        "legend_title": "#0B6FA8", "legend_text": "#0C4A6E",
        "hue_start": 240.0, "hue_end": 170.0, "saturation": 0.65, "lightness": 0.75,
    },

    "spring": {
        "background": "#F7FBEF", "plot_background": "#E8F5D6", "text": "#33691E",
        "accent": "#3F7A17", "pulse": "#C2185B",
        "border_start": "#8BC34A", "border_end": "#F8BBD0",
        "legend_title": "#4C8A1F", "legend_text": "#33691E",
        "hue_start": 90.0, "hue_end": 330.0, "saturation": 0.55, "lightness": 0.60,
    },
    "summer": {
        "background": "#FFF8E1", "plot_background": "#FFEFC2", "text": "#9A3412",
        "accent": "#C2410C", "pulse": "#D9480F",
        "border_start": "#FF6B35", "border_end": "#00B4D8",
        "legend_title": "#B45309", "legend_text": "#9A3412",
        "hue_start": 35.0, "hue_end": 190.0, "saturation": 0.85, "lightness": 0.60,
    },
    "autumn": {
        "background": "#191A16", "plot_background": "#292D22", "text": "#E2D5B9",
        "accent": "#E0B66F", "pulse": "#EDB75A",
        "border_start": "#D5A15E", "border_end": "#8D4937",
        "legend_title": "#A3AD7E", "legend_text": "#E2D5B9",
        "hue_start": 45.0, "hue_end": -35.0, "saturation": 0.75, "lightness": 0.45,
    },
    "winter": {
        "background": "#0D1321", "plot_background": "#172033", "text": "#CBD5E1",
        "accent": "#7DD3FC", "pulse": "#5CD6FF",
        "border_start": "#7DD3FC", "border_end": "#1E293B",
        "legend_title": "#93C5FD", "legend_text": "#CBD5E1",
        "hue_start": 190.0, "hue_end": 270.0, "saturation": 0.60, "lightness": 0.60,
    },

    "wine": {
        "background": "#16060C", "plot_background": "#2A0D17", "text": "#F3E4C8",
        "accent": "#E0B65C", "pulse": "#FFD27A",
        "border_start": "#D4A94B", "border_end": "#6E0F2F",
        "legend_title": "#E26A8D", "legend_text": "#F3E4C8",
        "hue_start": 310.0, "hue_end": 390.0, "saturation": 0.65, "lightness": 0.45,
    },
    "beer": {
        "background": "#17110A", "plot_background": "#291E12", "text": "#FBEBC0",
        "accent": "#F59E0B", "pulse": "#FFD166",
        "border_start": "#D97706", "border_end": "#78350F",
        "legend_title": "#FBBF24", "legend_text": "#FBEBC0",
        "hue_start": 20.0, "hue_end": 100.0, "saturation": 0.85, "lightness": 0.50,
    },
    "coffee": {
        "background": "#1C1411", "plot_background": "#2C201C", "text": "#EADDD7",
        "accent": "#C99A74", "pulse": "#F0B27A",
        "border_start": "#8C6046", "border_end": "#4A3326",
        "legend_title": "#B98F6C", "legend_text": "#EADDD7",
        "hue_start": 10.0, "hue_end": 90.0, "saturation": 0.40, "lightness": 0.45,
    },
    "matcha": {
        "background": "#F4F6F0", "plot_background": "#E5E9DD", "text": "#3D4C35",
        "accent": "#4E6A3C", "pulse": "#3F7D20",
        "border_start": "#5B704C", "border_end": "#D2DAC7",
        "legend_title": "#4F7036", "legend_text": "#3D4C35",
        "hue_start": 160.0, "hue_end": 20.0, "saturation": 0.40, "lightness": 0.65,
    },
    "berrymatcha": {
        "background": "#F4F6F0", "plot_background": "#E5E9DD", "text": "#3D4C35",
        "accent": "#D62839", "pulse": "#D62839",
        "border_start": "#5B704C", "border_end": "#E63946",
        "legend_title": "#4B7A2A", "legend_text": "#3D4C35",
        "hue_start": 130.0, "hue_end": -20.0, "saturation": 0.65, "lightness": 0.60,
    },
    "latte": {
        "background": "#FDFBF7", "plot_background": "#F4EBDD", "text": "#7A4F26",
        "accent": "#96591F", "pulse": "#B8651A",
        "border_start": "#D4A373", "border_end": "#A9743B",
        "legend_title": "#A8692B", "legend_text": "#7A4F26",
        "hue_start": 10.0, "hue_end": 90.0, "saturation": 0.40, "lightness": 0.55,
    },
    "brazil": {
        "background": "#071A12", "plot_background": "#0B2B1E", "text": "#F0FDF4",
        "accent": "#22C55E", "pulse": "#FFE14D",
        "border_start": "#FACC15", "border_end": "#166534",
        "legend_title": "#FACC15", "legend_text": "#F0FDF4",
        "hue_start": 170.0, "hue_end": 40.0, "saturation": 0.80, "lightness": 0.45,
    },
    "usa": {
        "background": "#0A1128", "plot_background": "#152238", "text": "#F5F8FF",
        "accent": "#FF334B", "pulse": "#FF5A6E",
        "border_start": "#E61C38", "border_end": "#2563EB",
        "legend_title": "#60A5FA", "legend_text": "#F5F8FF",
        "hue_start": 210.0, "hue_end": 360.0, "saturation": 0.75, "lightness": 0.50,
    },
    "miami": {
        "background": "#00152B", "plot_background": "#002A4D", "text": "#FFDD33",
        "accent": "#FF3D8B", "pulse": "#FF5C9D",
        "border_start": "#00B4D8", "border_end": "#FF2E7E",
        "legend_title": "#00F5C4", "legend_text": "#FFDD33",
        "hue_start": 340.0, "hue_end": 160.0, "saturation": 0.80, "lightness": 0.55,
    },
    "france": {
        "background": "#0A0E1A", "plot_background": "#151C2E", "text": "#F5F7FC",
        "accent": "#5B9BFF", "pulse": "#6FA8FF",
        "border_start": "#ED2939", "border_end": "#0055A5",
        "legend_title": "#FF6670", "legend_text": "#F5F7FC",
        "hue_start": 370.0, "hue_end": 210.0, "saturation": 0.70, "lightness": 0.55,
    },
    "japandark": {
        "background": "#000000", "plot_background": "#0A0A0A", "text": "#F5F5F5",
        "accent": "#FF2A55", "pulse": "#FF5C7A",
        "border_start": "#BC002D", "border_end": "#333333",
        "legend_title": "#FF6B87", "legend_text": "#F5F5F5",
        "hue_start": 315.0, "hue_end": 395.0, "saturation": 0.90, "lightness": 0.45,
    },
    "japanlight": {
        "background": "#F8F9FA", "plot_background": "#E5E7EB", "text": "#111827",
        "accent": "#BC002D", "pulse": "#C8102E",
        "border_start": "#E60033", "border_end": "#990022",
        "legend_title": "#4B5563", "legend_text": "#111827",
        "hue_start": 315.0, "hue_end": 395.0, "saturation": 0.80, "lightness": 0.50,
    },
    "sakura": {
        "background": "#0F111A", "plot_background": "#1A1D2C", "text": "#F7F2EF",
        "accent": "#FF9EAA", "pulse": "#FF86A8",
        "border_start": "#FF6B8B", "border_end": "#7C3AED",
        "legend_title": "#B9A2FF", "legend_text": "#F7F2EF",
        "hue_start": 345.0, "hue_end": 200.0, "saturation": 0.75, "lightness": 0.65,
    },
    "india": {
        "background": "#0D111A", "plot_background": "#182232", "text": "#F5F7FA",
        "accent": "#FF9A1F", "pulse": "#FFA733",
        "border_start": "#FF7A00", "border_end": "#059669",
        "legend_title": "#2FD6A0", "legend_text": "#F5F7FA",
        "hue_start": 15.0, "hue_end": 145.0, "saturation": 0.85, "lightness": 0.50,
    },
    "china": {
        "background": "#120608", "plot_background": "#240C12", "text": "#FFF5E6",
        "accent": "#FFD700", "pulse": "#FF4D3D",
        "border_start": "#DE2910", "border_end": "#8B0000",
        "legend_title": "#FFE066", "legend_text": "#FFF5E6",
        "hue_start": 330.0, "hue_end": 440.0, "saturation": 0.80, "lightness": 0.50,
    },
    "mexico": {
        "background": "#0A140E", "plot_background": "#11231A", "text": "#F5FFF9",
        "accent": "#00D67E", "pulse": "#FF4D5E",
        "border_start": "#00A859", "border_end": "#E4002B",
        "legend_title": "#7DF0B3", "legend_text": "#F5FFF9",
        "hue_start": 160.0, "hue_end": -20.0, "saturation": 0.80, "lightness": 0.55,
    },
    "fiesta": {
        "background": "#170A14", "plot_background": "#2A1020", "text": "#FFEE55",
        "accent": "#FF3FA4", "pulse": "#00E5A8",
        "border_start": "#FF1493", "border_end": "#FFB800",
        "legend_title": "#FFB800", "legend_text": "#FFEE55",
        "hue_start": 330.0, "hue_end": 150.0, "saturation": 0.85, "lightness": 0.55,
    },
    "greece": {
        "background": "#FAFAFA", "plot_background": "#EDF3FA", "text": "#1B4F8A",
        "accent": "#0D5EAF", "pulse": "#0066CC",
        "border_start": "#0D5EAF", "border_end": "#9CC3E8",
        "legend_title": "#0077A8", "legend_text": "#1B4F8A",
        "hue_start": 240.0, "hue_end": 180.0, "saturation": 0.90, "lightness": 0.40,
    },
    "egypt": {
        "background": "#F7EED2", "plot_background": "#EADCA6", "text": "#2B2311",
        "accent": "#1B4A87", "pulse": "#1A7F86",
        "border_start": "#C2A42D", "border_end": "#1B4A87",
        "legend_title": "#8A6A0A", "legend_text": "#2B2311",
        "hue_start": 230.0, "hue_end": 30.0, "saturation": 0.65, "lightness": 0.55,
    },

    "neon": {
        "background": "#080811", "plot_background": "#121324", "text": "#F2F2FF",
        "accent": "#FF1F6E", "pulse": "#00F0FF",
        "border_start": "#FF0055", "border_end": "#7000FF",
        "legend_title": "#B26BFF", "legend_text": "#F2F2FF",
        "hue_start": 340.0, "hue_end": 200.0, "saturation": 1.00, "lightness": 0.50,
    },
    "cyberpunk": {
        "background": "#0D0221", "plot_background": "#180538", "text": "#5EF5FF",
        "accent": "#FF2E97", "pulse": "#00FF41",
        "border_start": "#FF007F", "border_end": "#2B00FF",
        "legend_title": "#FCEE0A", "legend_text": "#5EF5FF",
        "hue_start": 320.0, "hue_end": 180.0, "saturation": 1.0, "lightness": 0.50,
    },
    "steampunk": {
        "background": "#1A1512", "plot_background": "#29211D", "text": "#D4A373",
        "accent": "#D98C3A", "pulse": "#E8B85A",
        "border_start": "#B8631E", "border_end": "#3E2723",
        "legend_title": "#E6C287", "legend_text": "#D4A373",
        "hue_start": 10.0, "hue_end": 80.0, "saturation": 0.60, "lightness": 0.40,
    },
    "synthwave": {
        "background": "#130026", "plot_background": "#240046", "text": "#FF71CE",
        "accent": "#05FFA1", "pulse": "#FFC13D",
        "border_start": "#7B2CBF", "border_end": "#FF006E",
        "legend_title": "#00E5FF", "legend_text": "#FF71CE",
        "hue_start": 250.0, "hue_end": 340.0, "saturation": 0.90, "lightness": 0.55,
    },
    "lofi": {
        "background": "#27273A", "plot_background": "#323247", "text": "#E2D9F3",
        "accent": "#B9A3FF", "pulse": "#5EEAD4",
        "border_start": "#8B5CF6", "border_end": "#4C1D95",
        "legend_title": "#C4B5FD", "legend_text": "#E2D9F3",
        "hue_start": 280.0, "hue_end": 160.0, "saturation": 0.50, "lightness": 0.65,
    },

    "dracula": {
        "background": "#282A36", "plot_background": "#343746", "text": "#F8F8F2",
        "accent": "#FF79C6", "pulse": "#F1FA8C",
        "border_start": "#50FA7B", "border_end": "#BD93F9",
        "legend_title": "#BD93F9", "legend_text": "#F8F8F2",
        "hue_start": 330.0, "hue_end": 135.0, "saturation": 0.70, "lightness": 0.65,
    },
    "mocha": {
        "background": "#1E1E2E", "plot_background": "#242438", "text": "#CDD6F4",
        "accent": "#F5C2E7", "pulse": "#F9E2AF",
        "border_start": "#89DCEB", "border_end": "#CBA6F7",
        "legend_title": "#CBA6F7", "legend_text": "#CDD6F4",
        "hue_start": 215.0, "hue_end": 335.0, "saturation": 0.80, "lightness": 0.75,
    },
    "nord": {
        "background": "#2E3440", "plot_background": "#3B4252", "text": "#E5E9F0",
        "accent": "#88C0D0", "pulse": "#EBCB8B",
        "border_start": "#81A1C1", "border_end": "#434C5E",
        "legend_title": "#81A1C1", "legend_text": "#E5E9F0",
        "hue_start": 210.0, "hue_end": 90.0, "saturation": 0.45, "lightness": 0.65,
    },
    "solarizeddark": {
        "background": "#002B36", "plot_background": "#073642", "text": "#93A1A1",
        "accent": "#C99700", "pulse": "#E5732A",
        "border_start": "#CB4B16", "border_end": "#002B36",
        "legend_title": "#2AA198", "legend_text": "#93A1A1",
        "hue_start": 30.0, "hue_end": 190.0, "saturation": 0.65, "lightness": 0.45,
    },
    "solarizedlight": {
        "background": "#FDF6E3", "plot_background": "#EEE8D5", "text": "#586E75",
        "accent": "#1A6FB0", "pulse": "#C02A72",
        "border_start": "#2AA198", "border_end": "#CCC5B2",
        "legend_title": "#1B857E", "legend_text": "#586E75",
        "hue_start": 190.0, "hue_end": 340.0, "saturation": 0.65, "lightness": 0.50,
    },
    "atlas": {
        "background": "#0B1020", "plot_background": "#151E35", "text": "#D9E4F2",
        "accent": "#E8C878", "pulse": "#FFDA85",
        "border_start": "#8299D4", "border_end": "#62528F",
        "legend_title": "#A99AE8", "legend_text": "#D9E4F2",
        "hue_start": 180.0, "hue_end": 330.0, "saturation": 0.60, "lightness": 0.65,
    },
    "heaven": {
        "background": "#F4F9FF", "plot_background": "#E6F1FC", "text": "#34519E",
        "accent": "#0B6FC2", "pulse": "#B87400",
        "border_start": "#38BDF8", "border_end": "#FFC83D",
        "legend_title": "#1565C0", "legend_text": "#34519E",
        "hue_start": 210.0, "hue_end": 30.0, "saturation": 0.80, "lightness": 0.65,
    },
    "hell": {
        "background": "#0A0303", "plot_background": "#170505", "text": "#FF7A2E",
        "accent": "#FF2D1F", "pulse": "#FF9900",
        "border_start": "#FF3300", "border_end": "#4D0000",
        "legend_title": "#FF6600", "legend_text": "#FF7A2E",
        "hue_start": 330.0, "hue_end": 420.0, "saturation": 0.90, "lightness": 0.45,
    },
    "abyss": {
        "background": "#010A14", "plot_background": "#021226", "text": "#8CF0DC",
        "accent": "#1CC8EA", "pulse": "#3DFFD6",
        "border_start": "#0077B6", "border_end": "#01050A",
        "legend_title": "#4FD1E8", "legend_text": "#8CF0DC",
        "hue_start": 220.0, "hue_end": 140.0, "saturation": 0.85, "lightness": 0.45,
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
