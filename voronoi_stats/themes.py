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
        "legend_title": "#FF3344", "legend_text": "#FFB3B3",
        "hue_start": 375.0, "hue_end": 295.0, "saturation": 0.85, "lightness": 0.50,
    },
    "orange": {
        "background": "#140C07", "plot_background": "#24140B", "text": "#FFEDD5",
        "accent": "#EA580C", "pulse": "#FF8C42",
        "border_start": "#FB923C", "border_end": "#C2410C",
        "legend_title": "#FDBA74", "legend_text": "#D6AE91",
        "hue_start": 5.0, "hue_end": 80.0, "saturation": 0.90, "lightness": 0.55,
    },
    "yellow": {
        "background": "#121008", "plot_background": "#211B0D", "text": "#FEF3C7",
        "accent": "#D4A20A", "pulse": "#FFE44D",
        "border_start": "#FDE047", "border_end": "#A16207",
        "legend_title": "#FDE68A", "legend_text": "#D6C99A",
        "hue_start": 25.0, "hue_end": 100.0, "saturation": 0.85, "lightness": 0.50,
    },
    "green": {
        "background": "#051209", "plot_background": "#081F10", "text": "#A7F3D0",
        "accent": "#10B981", "pulse": "#34D399",
        "border_start": "#059669", "border_end": "#064E3B",
        "legend_title": "#10B981", "legend_text": "#A7F3D0",
        "hue_start": 170.0, "hue_end": 70.0, "saturation": 0.80, "lightness": 0.45,
    },
    "blue": {
        "background": "#080F1F", "plot_background": "#0F1B30", "text": "#BAE6FD",
        "accent": "#2563EB", "pulse": "#38BDF8",
        "border_start": "#60A5FA", "border_end": "#1D4ED8",
        "legend_title": "#7DD3FC", "legend_text": "#93B4D6",
        "hue_start": 250.0, "hue_end": 150.0, "saturation": 0.85, "lightness": 0.55,
    },
    "purple": {
        "background": "#0D0918", "plot_background": "#19112B", "text": "#DDD6FE",
        "accent": "#6D28D9", "pulse": "#C084FC",
        "border_start": "#A78BFA", "border_end": "#5B21B6",
        "legend_title": "#C4B5FD", "legend_text": "#B0A1D0",
        "hue_start": 250.0, "hue_end": 340.0, "saturation": 0.80, "lightness": 0.60,
    },
    "pink": {
        "background": "#0D080F", "plot_background": "#1D101D", "text": "#FBCFE8",
        "accent": "#BE185D", "pulse": "#FF4FA3",
        "border_start": "#F472B6", "border_end": "#9D174D",
        "legend_title": "#F9A8D4", "legend_text": "#D6A0C4",
        "hue_start": 270.0, "hue_end": 390.0, "saturation": 0.80, "lightness": 0.65,
    },
    "obsidian": {
        "background": "#050505", "plot_background": "#0F0F0F", "text": "#A3A3A3",
        "accent": "#FAFAFA", "pulse": "#E5E5E5",
        "border_start": "#525252", "border_end": "#171717",
        "legend_title": "#FAFAFA", "legend_text": "#A3A3A3",
        "hue_start": 200.0, "hue_end": 280.0, "saturation": 0.35, "lightness": 0.45,
    },

    "mint": {
        "background": "#F0FDF4", "plot_background": "#DCFCE7", "text": "#064E3B",
        "accent": "#10B981", "pulse": "#0D9488",
        "border_start": "#059669", "border_end": "#A7F3D0",
        "legend_title": "#059669", "legend_text": "#065F46",
        "hue_start": 180.0, "hue_end": 60.0, "saturation": 0.60, "lightness": 0.60,
    },
    "chocomint": {
        "background": "#EAF8EF", "plot_background": "#D6F5E0", "text": "#5A3A24",
        "accent": "#10B981", "pulse": "#6B4226",
        "border_start": "#6B4226", "border_end": "#34D399",
        "legend_title": "#6B4226", "legend_text": "#5C4033",
        "hue_start": 180.0, "hue_end": 40.0, "saturation": 0.60, "lightness": 0.65,
    },
    "lavender": {
        "background": "#F3F0FA", "plot_background": "#E7E1F6", "text": "#7E68C8",
        "accent": "#9B7BE0", "pulse": "#9333EA",
        "border_start": "#8B5CF6", "border_end": "#DDD6F3",
        "legend_title": "#7C3AED", "legend_text": "#7E68C8",
        "hue_start": 290.0, "hue_end": 210.0, "saturation": 0.70, "lightness": 0.60,
    },
    "peach": {
        "background": "#FFF4EC", "plot_background": "#FFE6D5", "text": "#7C2D12",
        "accent": "#F28B5B", "pulse": "#9A3412",
        "border_start": "#F28B5B", "border_end": "#FFD3B8",
        "legend_title": "#D9622B", "legend_text": "#9A3412",
        "hue_start": 310.0, "hue_end": 390.0, "saturation": 0.70, "lightness": 0.75,
    },
    "sky": {
        "background": "#F0F9FF", "plot_background": "#E0F2FE", "text": "#0C4A6E",
        "accent": "#0EA5E9", "pulse": "#075985",
        "border_start": "#0284C7", "border_end": "#BAE6FD",
        "legend_title": "#0284C7", "legend_text": "#0C4A6E",
        "hue_start": 240.0, "hue_end": 170.0, "saturation": 0.65, "lightness": 0.75,
    },

    "spring": {
        "background": "#F7FBEF", "plot_background": "#E8F5D6", "text": "#33691E",
        "accent": "#7CB342", "pulse": "#E8467F",
        "border_start": "#8BC34A", "border_end": "#F8BBD0",
        "legend_title": "#4C8A1F", "legend_text": "#33691E",
        "hue_start": 90.0, "hue_end": 330.0, "saturation": 0.55, "lightness": 0.60,
    },
    "summer": {
        "background": "#FFF8E1", "plot_background": "#FFEFC2", "text": "#9A3412",
        "accent": "#FF9F1C", "pulse": "#00B4D8",
        "border_start": "#FF6B35", "border_end": "#00B4D8",
        "legend_title": "#F97316", "legend_text": "#B45309",
        "hue_start": 35.0, "hue_end": 190.0, "saturation": 0.85, "lightness": 0.60,
    },
    "autumn": {
        "background": "#191A16", "plot_background": "#292D22", "text": "#E2D5B9",
        "accent": "#C18C52", "pulse": "#E0B66F",
        "border_start": "#D5A15E", "border_end": "#8D4937",
        "legend_title": "#E0B66F", "legend_text": "#B5AD99",
        "hue_start": 45.0, "hue_end": -35.0, "saturation": 0.75, "lightness": 0.45,
    },
    "winter": {
        "background": "#0D1321", "plot_background": "#172033", "text": "#CBD5E1",
        "accent": "#7DD3FC", "pulse": "#E0F2FE",
        "border_start": "#7DD3FC", "border_end": "#1E293B",
        "legend_title": "#7DD3FC", "legend_text": "#CBD5E1",
        "hue_start": 190.0, "hue_end": 270.0, "saturation": 0.60, "lightness": 0.60,
    },

    "wine": {
        "background": "#16060C", "plot_background": "#2A0D17", "text": "#F3E4C8",
        "accent": "#B0123F", "pulse": "#FFD27A",
        "border_start": "#D4A94B", "border_end": "#6E0F2F",
        "legend_title": "#E0B65C", "legend_text": "#E0B56F",
        "hue_start": 310.0, "hue_end": 390.0, "saturation": 0.65, "lightness": 0.45,
    },
    "beer": {
        "background": "#17110A", "plot_background": "#291E12", "text": "#FEF3C7",
        "accent": "#F59E0B", "pulse": "#FFF3C4",
        "border_start": "#D97706", "border_end": "#78350F",
        "legend_title": "#F59E0B", "legend_text": "#FEF3C7",
        "hue_start": 20.0, "hue_end": 100.0, "saturation": 0.85, "lightness": 0.50,
    },
    "coffee": {
        "background": "#1C1411", "plot_background": "#2C201C", "text": "#EADDD7",
        "accent": "#A67B5B", "pulse": "#E8D5C4",
        "border_start": "#8C6046", "border_end": "#4A3326",
        "legend_title": "#B98F6C", "legend_text": "#EADDD7",
        "hue_start": 10.0, "hue_end": 90.0, "saturation": 0.40, "lightness": 0.45,
    },
    "matcha": {
        "background": "#F4F6F0", "plot_background": "#E5E9DD", "text": "#3D4C35",
        "accent": "#748C61", "pulse": "#3D5A2B",
        "border_start": "#5B704C", "border_end": "#D2DAC7",
        "legend_title": "#5F7E4A", "legend_text": "#3D4C35",
        "hue_start": 160.0, "hue_end": 20.0, "saturation": 0.40, "lightness": 0.65,
    },
    "berrymatcha": {
        "background": "#F4F6F0", "plot_background": "#E5E9DD", "text": "#D62839",
        "accent": "#5F8B3C", "pulse": "#E63946",
        "border_start": "#5B704C", "border_end": "#E63946",
        "legend_title": "#E63946", "legend_text": "#3D4C35",
        "hue_start": 130.0, "hue_end": -20.0, "saturation": 0.65, "lightness": 0.60,
    },
    "latte": {
        "background": "#FDFBF7", "plot_background": "#F4EBDD", "text": "#9A6B3E",
        "accent": "#C19A6B", "pulse": "#C97B2E",
        "border_start": "#D4A373", "border_end": "#A9743B",
        "legend_title": "#A8692B", "legend_text": "#9A6B3E",
        "hue_start": 10.0, "hue_end": 90.0, "saturation": 0.40, "lightness": 0.55,
    },
    "brazil": {
        "background": "#071A12", "plot_background": "#0B2B1E", "text": "#F0FDF4",
        "accent": "#22C55E", "pulse": "#FEF08A",
        "border_start": "#FACC15", "border_end": "#166534",
        "legend_title": "#22C55E", "legend_text": "#FEF08A",
        "hue_start": 170.0, "hue_end": 40.0, "saturation": 0.80, "lightness": 0.45,
    },
    "usa": {
        "background": "#0A1128", "plot_background": "#152238", "text": "#FFFFFF",
        "accent": "#E61C38", "pulse": "#FFFFFF",
        "border_start": "#E61C38", "border_end": "#2563EB",
        "legend_title": "#FF334B", "legend_text": "#C7D2E3",
        "hue_start": 210.0, "hue_end": 360.0, "saturation": 0.75, "lightness": 0.50,
    },
    "miami": {
        "background": "#00152B", "plot_background": "#002A4D", "text": "#FFD60A",
        "accent": "#FF2E7E", "pulse": "#00F5C4",
        "border_start": "#00B4D8", "border_end": "#FF2E7E",
        "legend_title": "#FF3D8B", "legend_text": "#FFD60A",
        "hue_start": 340.0, "hue_end": 160.0, "saturation": 0.80, "lightness": 0.55,
    },
    "france": {
        "background": "#0A0E1A", "plot_background": "#151C2E", "text": "#FFFFFF",
        "accent": "#ED2939", "pulse": "#3B82F6",
        "border_start": "#ED2939", "border_end": "#0055A5",
        "legend_title": "#3B82F6", "legend_text": "#8E9BB0",
        "hue_start": 370.0, "hue_end": 210.0, "saturation": 0.70, "lightness": 0.55,
    },
    "japandark": {
        "background": "#000000", "plot_background": "#0A0A0A", "text": "#FFFFFF",
        "accent": "#E60033", "pulse": "#FFFFFF",
        "border_start": "#BC002D", "border_end": "#333333",
        "legend_title": "#E60033", "legend_text": "#FFFFFF",
        "hue_start": 315.0, "hue_end": 395.0, "saturation": 0.90, "lightness": 0.45,
    },
    "japanlight": {
        "background": "#F8F9FA", "plot_background": "#E5E7EB", "text": "#111827",
        "accent": "#FF4D4D", "pulse": "#BC002D",
        "border_start": "#E60033", "border_end": "#990022",
        "legend_title": "#BC002D", "legend_text": "#374151",
        "hue_start": 315.0, "hue_end": 395.0, "saturation": 0.80, "lightness": 0.50,
    },
    "sakura": {
        "background": "#0F111A", "plot_background": "#1A1D2C", "text": "#F7F2EF",
        "accent": "#FF6B8B", "pulse": "#FF9EAA",
        "border_start": "#FF6B8B", "border_end": "#7C3AED",
        "legend_title": "#FF9EAA", "legend_text": "#8A94A6",
        "hue_start": 345.0, "hue_end": 200.0, "saturation": 0.75, "lightness": 0.65,
    },
    "india": {
        "background": "#0D111A", "plot_background": "#182232", "text": "#FFFFFF",
        "accent": "#FF7A00", "pulse": "#10B981",
        "border_start": "#FF7A00", "border_end": "#059669",
        "legend_title": "#FF8C00", "legend_text": "#8C9BB0",
        "hue_start": 15.0, "hue_end": 145.0, "saturation": 0.85, "lightness": 0.50,
    },
    "china": {
        "background": "#120608", "plot_background": "#240C12", "text": "#FFF5E6",
        "accent": "#FF3B30", "pulse": "#FFD700",
        "border_start": "#DE2910", "border_end": "#8B0000",
        "legend_title": "#FFD700", "legend_text": "#A68A80",
        "hue_start": 330.0, "hue_end": 440.0, "saturation": 0.80, "lightness": 0.50,
    },
    "mexico": {
        "background": "#0A140E", "plot_background": "#11231A", "text": "#FFFFFF",
        "accent": "#00C26E", "pulse": "#FF2D3F",
        "border_start": "#00A859", "border_end": "#E4002B",
        "legend_title": "#00D67E", "legend_text": "#FFFFFF",
        "hue_start": 160.0, "hue_end": -20.0, "saturation": 0.80, "lightness": 0.55,
    },
    "fiesta": {
        "background": "#170A14", "plot_background": "#2A1020", "text": "#FFE600",
        "accent": "#FF1493", "pulse": "#00E5A8",
        "border_start": "#FF1493", "border_end": "#FFB800",
        "legend_title": "#FF3FA4", "legend_text": "#FFF176",
        "hue_start": 330.0, "hue_end": 150.0, "saturation": 0.85, "lightness": 0.55,
    },
    "greece": {
        "background": "#FAFAFA", "plot_background": "#EDF3FA", "text": "#1B4F8A",
        "accent": "#0D5EAF", "pulse": "#0096C7",
        "border_start": "#0D5EAF", "border_end": "#9CC3E8",
        "legend_title": "#0D5EAF", "legend_text": "#1B4F8A",
        "hue_start": 240.0, "hue_end": 180.0, "saturation": 0.90, "lightness": 0.40,
    },
    "egypt": {
        "background": "#F7EED2", "plot_background": "#EADCA6", "text": "#2B2311",
        "accent": "#C2A42D", "pulse": "#A47A0A",
        "border_start": "#C2A42D", "border_end": "#1B4A87",
        "legend_title": "#1B4A87", "legend_text": "#1B4A87",
        "hue_start": 230.0, "hue_end": 30.0, "saturation": 0.65, "lightness": 0.55,
    },

    "neon": {
        "background": "#080811", "plot_background": "#121324", "text": "#FFFFFF",
        "accent": "#FF0055", "pulse": "#00F0FF",
        "border_start": "#FF0055", "border_end": "#7000FF",
        "legend_title": "#FF0055", "legend_text": "#FFFFFF",
        "hue_start": 340.0, "hue_end": 200.0, "saturation": 1.00, "lightness": 0.50,
    },
    "cyberpunk": {
        "background": "#0D0221", "plot_background": "#180538", "text": "#0FF0FC",
        "accent": "#FF007F", "pulse": "#00FF41",
        "border_start": "#FF007F", "border_end": "#2B00FF",
        "legend_title": "#FF007F", "legend_text": "#0FF0FC",
        "hue_start": 320.0, "hue_end": 180.0, "saturation": 1.0, "lightness": 0.50,
    },
    "steampunk": {
        "background": "#1A1512", "plot_background": "#29211D", "text": "#D4A373",
        "accent": "#B5651D", "pulse": "#E6C287",
        "border_start": "#8B4513", "border_end": "#3E2723",
        "legend_title": "#C27A2E", "legend_text": "#D4A373",
        "hue_start": 10.0, "hue_end": 80.0, "saturation": 0.60, "lightness": 0.40,
    },
    "synthwave": {
        "background": "#130026", "plot_background": "#240046", "text": "#FF71CE",
        "accent": "#05FFA1", "pulse": "#F9A11B",
        "border_start": "#7B2CBF", "border_end": "#FF006E",
        "legend_title": "#05FFA1", "legend_text": "#FF71CE",
        "hue_start": 250.0, "hue_end": 340.0, "saturation": 0.90, "lightness": 0.55,
    },
    "lofi": {
        "background": "#27273A", "plot_background": "#323247", "text": "#E2D9F3",
        "accent": "#A78BFA", "pulse": "#5EEAD4",
        "border_start": "#8B5CF6", "border_end": "#4C1D95",
        "legend_title": "#A78BFA", "legend_text": "#E2D9F3",
        "hue_start": 280.0, "hue_end": 160.0, "saturation": 0.50, "lightness": 0.65,
    },

    "dracula": {
        "background": "#282A36", "plot_background": "#343746", "text": "#F8F8F2",
        "accent": "#FF79C6", "pulse": "#8BE9FD",
        "border_start": "#50FA7B", "border_end": "#BD93F9",
        "legend_title": "#FF79C6", "legend_text": "#B8B9C9",
        "hue_start": 330.0, "hue_end": 135.0, "saturation": 0.70, "lightness": 0.65,
    },
    "mocha": {
        "background": "#1E1E2E", "plot_background": "#242438", "text": "#CDD6F4",
        "accent": "#F5C2E7", "pulse": "#94E2D5",
        "border_start": "#89DCEB", "border_end": "#CBA6F7",
        "legend_title": "#F5C2E7", "legend_text": "#A6ADC8",
        "hue_start": 215.0, "hue_end": 335.0, "saturation": 0.80, "lightness": 0.75,
    },
    "nord": {
        "background": "#2E3440", "plot_background": "#3B4252", "text": "#ECEFF4",
        "accent": "#88C0D0", "pulse": "#A3BE8C",
        "border_start": "#81A1C1", "border_end": "#434C5E",
        "legend_title": "#88C0D0", "legend_text": "#ECEFF4",
        "hue_start": 210.0, "hue_end": 90.0, "saturation": 0.45, "lightness": 0.65,
    },
    "solarizeddark": {
        "background": "#002B36", "plot_background": "#073642", "text": "#839496",
        "accent": "#B58900", "pulse": "#2AA198",
        "border_start": "#CB4B16", "border_end": "#002B36",
        "legend_title": "#B58900", "legend_text": "#839496",
        "hue_start": 30.0, "hue_end": 190.0, "saturation": 0.65, "lightness": 0.45,
    },
    "solarizedlight": {
        "background": "#FDF6E3", "plot_background": "#EEE8D5", "text": "#586E75",
        "accent": "#268BD2", "pulse": "#D33682",
        "border_start": "#2AA198", "border_end": "#CCC5B2",
        "legend_title": "#268BD2", "legend_text": "#586E75",
        "hue_start": 190.0, "hue_end": 340.0, "saturation": 0.65, "lightness": 0.50,
    },
    "atlas": {
        "background": "#0B1020", "plot_background": "#151E35", "text": "#D9E4F2",
        "accent": "#718FD8", "pulse": "#E8C878",
        "border_start": "#8299D4", "border_end": "#62528F",
        "legend_title": "#E8C878", "legend_text": "#929FB9",
        "hue_start": 180.0, "hue_end": 330.0, "saturation": 0.60, "lightness": 0.65,
    },
    "heaven": {
        "background": "#F4F9FF", "plot_background": "#E6F1FC", "text": "#3B5BA9",
        "accent": "#38BDF8", "pulse": "#FFB300",
        "border_start": "#38BDF8", "border_end": "#FFC83D",
        "legend_title": "#0B6FC2", "legend_text": "#3B5BA9",
        "hue_start": 210.0, "hue_end": 30.0, "saturation": 0.80, "lightness": 0.65,
    },
    "hell": {
        "background": "#0A0303", "plot_background": "#170505", "text": "#FF6600",
        "accent": "#CC0000", "pulse": "#FF9900",
        "border_start": "#FF3300", "border_end": "#4D0000",
        "legend_title": "#E01010", "legend_text": "#FF6600",
        "hue_start": 330.0, "hue_end": 420.0, "saturation": 0.90, "lightness": 0.45,
    },
    "abyss": {
        "background": "#010A14", "plot_background": "#021226", "text": "#64FFDA",
        "accent": "#00B4D8", "pulse": "#64FFDA",
        "border_start": "#0077B6", "border_end": "#01050A",
        "legend_title": "#00B4D8", "legend_text": "#64FFDA",
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
