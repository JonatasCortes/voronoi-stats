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
        "background": "#120803", "plot_background": "#200D05", "text": "#FFDDBB",
        "accent": "#FF7700", "pulse": "#FFAA44",
        "border_start": "#E65C00", "border_end": "#802B00",
        "legend_title": "#FF7700", "legend_text": "#FFDDBB",
        "hue_start": 5.0, "hue_end": 80.0, "saturation": 0.90, "lightness": 0.55,
    },
    "yellow": {
        "background": "#141205", "plot_background": "#242009", "text": "#FEF3C7",
        "accent": "#F59E0B", "pulse": "#FCD34D",
        "border_start": "#D97706", "border_end": "#78350F",
        "legend_title": "#F59E0B", "legend_text": "#FEF3C7",
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
        "background": "#050B14", "plot_background": "#0A1429", "text": "#BFDBFE",
        "accent": "#3B82F6", "pulse": "#60A5FA",
        "border_start": "#2563EB", "border_end": "#1E3A8A",
        "legend_title": "#3B82F6", "legend_text": "#BFDBFE",
        "hue_start": 250.0, "hue_end": 150.0, "saturation": 0.85, "lightness": 0.55,
    },
    "purple": {
        "background": "#0B0514", "plot_background": "#140A29", "text": "#E9D5FF",
        "accent": "#A855F7", "pulse": "#C084FC",
        "border_start": "#9333EA", "border_end": "#4C1D95",
        "legend_title": "#A855F7", "legend_text": "#E9D5FF",
        "hue_start": 250.0, "hue_end": 340.0, "saturation": 0.80, "lightness": 0.60,
    },
    "obsidian": {
        "background": "#050505", "plot_background": "#0F0F0F", "text": "#A3A3A3",
        "accent": "#FAFAFA", "pulse": "#737373",
        "border_start": "#525252", "border_end": "#171717",
        "legend_title": "#FAFAFA", "legend_text": "#A3A3A3",
        "hue_start": 200.0, "hue_end": 280.0, "saturation": 0.35, "lightness": 0.45,
    },

    "mint": {
        "background": "#F0FDF4", "plot_background": "#DCFCE7", "text": "#064E3B",
        "accent": "#10B981", "pulse": "#34D399",
        "border_start": "#059669", "border_end": "#A7F3D0",
        "legend_title": "#059669", "legend_text": "#064E3B",
        "hue_start": 180.0, "hue_end": 60.0, "saturation": 0.60, "lightness": 0.60,
    },
    "chocomint": {
        "background": "#F0FDF4", "plot_background": "#DCFCE7", "text": "#4A3628",
        "accent": "#A06B4B", "pulse": "#8C5A3C",
        "border_start": "#A06B4B", "border_end": "#10B981",
        "legend_title": "#A06B4B", "legend_text": "#4A3628",
        "hue_start": 180.0, "hue_end": 40.0, "saturation": 0.60, "lightness": 0.65,
    },
    "lavender": {
        "background": "#EFF1F5", "plot_background": "#E6E9EF", "text": "#4C4F69",
        "accent": "#8839EF", "pulse": "#1E66F5",
        "border_start": "#D20F39", "border_end": "#CCD0DA",
        "legend_title": "#8839EF", "legend_text": "#4C4F69",
        "hue_start": 290.0, "hue_end": 210.0, "saturation": 0.70, "lightness": 0.60,
    },
    "peach": {
        "background": "#FFF1F2", "plot_background": "#FFE4E6", "text": "#881337",
        "accent": "#F43F5E", "pulse": "#FB7185",
        "border_start": "#E11D48", "border_end": "#FECDD3",
        "legend_title": "#E11D48", "legend_text": "#881337",
        "hue_start": 310.0, "hue_end": 390.0, "saturation": 0.70, "lightness": 0.75,
    },
    "sky": {
        "background": "#F0F9FF", "plot_background": "#E0F2FE", "text": "#0C4A6E",
        "accent": "#0EA5E9", "pulse": "#38BDF8",
        "border_start": "#0284C7", "border_end": "#BAE6FD",
        "legend_title": "#0284C7", "legend_text": "#0C4A6E",
        "hue_start": 240.0, "hue_end": 170.0, "saturation": 0.65, "lightness": 0.75,
    },

    "spring": {
        "background": "#F7FBEF", "plot_background": "#E8F5D6", "text": "#274E13",
        "accent": "#7CB342", "pulse": "#F48FB1",
        "border_start": "#558B2F", "border_end": "#C5E1A5",
        "legend_title": "#558B2F", "legend_text": "#274E13",
        "hue_start": 90.0, "hue_end": 330.0, "saturation": 0.55, "lightness": 0.60,
    },
    "summer": {
        "background": "#FEFAED", "plot_background": "#FDF0D5", "text": "#78350F",
        "accent": "#F59E0B", "pulse": "#06B6D4",
        "border_start": "#F97316", "border_end": "#0284C7",
        "legend_title": "#EA580C", "legend_text": "#78350F",
        "hue_start": 35.0, "hue_end": 190.0, "saturation": 0.85, "lightness": 0.60,
    },
    "autumn": {
        "background": "#241009", "plot_background": "#36180D", "text": "#FDE68A",
        "accent": "#EA580C", "pulse": "#DC2626",
        "border_start": "#C2410C", "border_end": "#7F1D1D",
        "legend_title": "#EA580C", "legend_text": "#FDE68A",
        "hue_start": 45.0, "hue_end": -35.0, "saturation": 0.75, "lightness": 0.45,
    },
    "winter": {
        "background": "#0D1321", "plot_background": "#172033", "text": "#E2E8F0",
        "accent": "#38BDF8", "pulse": "#818CF8",
        "border_start": "#3B82F6", "border_end": "#1E293B",
        "legend_title": "#38BDF8", "legend_text": "#E2E8F0",
        "hue_start": 190.0, "hue_end": 270.0, "saturation": 0.60, "lightness": 0.60,
    },

    "wine": {
        "background": "#14050A", "plot_background": "#260912", "text": "#F5E1E6",
        "accent": "#9F1239", "pulse": "#E11D48",
        "border_start": "#881337", "border_end": "#4C0519",
        "legend_title": "#9F1239", "legend_text": "#F5E1E6",
        "hue_start": 310.0, "hue_end": 390.0, "saturation": 0.65, "lightness": 0.45,
    },
    "beer": {
        "background": "#17110A", "plot_background": "#291E12", "text": "#FEF3C7",
        "accent": "#F59E0B", "pulse": "#FCD34D",
        "border_start": "#D97706", "border_end": "#78350F",
        "legend_title": "#F59E0B", "legend_text": "#FEF3C7",
        "hue_start": 20.0, "hue_end": 100.0, "saturation": 0.85, "lightness": 0.50,
    },
    "coffee": {
        "background": "#1C1411", "plot_background": "#2C201C", "text": "#EADDD7",
        "accent": "#A67B5B", "pulse": "#CDB3A0",
        "border_start": "#8C6046", "border_end": "#4A3326",
        "legend_title": "#A67B5B", "legend_text": "#EADDD7",
        "hue_start": 10.0, "hue_end": 90.0, "saturation": 0.40, "lightness": 0.45,
    },
    "matcha": {
        "background": "#F4F6F0", "plot_background": "#E5E9DD", "text": "#3D4C35",
        "accent": "#748C61", "pulse": "#9CB38A",
        "border_start": "#5B704C", "border_end": "#D2DAC7",
        "legend_title": "#5B704C", "legend_text": "#3D4C35",
        "hue_start": 160.0, "hue_end": 20.0, "saturation": 0.40, "lightness": 0.65,
    },
    "berrymatcha": {
        "background": "#F4F6F0", "plot_background": "#E5E9DD", "text": "#3D4C35",
        "accent": "#E63946", "pulse": "#FF4D6D",
        "border_start": "#E63946", "border_end": "#5B704C",
        "legend_title": "#E63946", "legend_text": "#3D4C35",
        "hue_start": 130.0, "hue_end": -20.0, "saturation": 0.65, "lightness": 0.60,
    },
    "latte": {
        "background": "#FDFBF7", "plot_background": "#F4EFEA", "text": "#4A3B32",
        "accent": "#C19A6B", "pulse": "#8C6239",
        "border_start": "#D4B895", "border_end": "#5C4033",
        "legend_title": "#8C6239", "legend_text": "#5C4435",
        "hue_start": 10.0, "hue_end": 90.0, "saturation": 0.40, "lightness": 0.55,
    },
    "brazil": {
        "background": "#071A12", "plot_background": "#0B2B1E", "text": "#FEF08A",
        "accent": "#22C55E", "pulse": "#3B82F6",
        "border_start": "#EAB308", "border_end": "#166534",
        "legend_title": "#EAB308", "legend_text": "#FEF08A",
        "hue_start": 170.0, "hue_end": 40.0, "saturation": 0.80, "lightness": 0.45,
    },
    "usa": {
        "background": "#080F1F", "plot_background": "#0D1833", "text": "#F8FAFC",
        "accent": "#3B82F6", "pulse": "#EF4444",
        "border_start": "#2563EB", "border_end": "#991B1B",
        "legend_title": "#3B82F6", "legend_text": "#F8FAFC",
        "hue_start": 210.0, "hue_end": 360.0, "saturation": 0.75, "lightness": 0.50,
    },
    "miami": {
        "background": "#001B2E", "plot_background": "#002845", "text": "#FFD166",
        "accent": "#EF476F", "pulse": "#06D6A0",
        "border_start": "#118AB2", "border_end": "#073B4C",
        "legend_title": "#EF476F", "legend_text": "#FFD166",
        "hue_start": 340.0, "hue_end": 160.0, "saturation": 0.80, "lightness": 0.55,
    },
    "france": {
        "background": "#171A21", "plot_background": "#222630", "text": "#F1F5F9",
        "accent": "#EF4135", "pulse": "#0055A4",
        "border_start": "#EF4135", "border_end": "#002B54",
        "legend_title": "#EF4135", "legend_text": "#F1F5F9",
        "hue_start": 370.0, "hue_end": 210.0, "saturation": 0.70, "lightness": 0.55,
    },
    "japan_dark": {
        "background": "#000000", "plot_background": "#0A0A0A", "text": "#FFFFFF",
        "accent": "#E60033", "pulse": "#FFFFFF",
        "border_start": "#BC002D", "border_end": "#333333",
        "legend_title": "#E60033", "legend_text": "#FFFFFF",
        "hue_start": 315.0, "hue_end": 395.0, "saturation": 0.90, "lightness": 0.45,
    },
    "japan_light": {
        "background": "#FCFAF5", "plot_background": "#F4F0E6", "text": "#1A1A1A",
        "accent": "#BC002D", "pulse": "#E60033",
        "border_start": "#990022", "border_end": "#D6CFC1",
        "legend_title": "#BC002D", "legend_text": "#1A1A1A",
        "hue_start": 315.0, "hue_end": 395.0, "saturation": 0.80, "lightness": 0.50,
    },
    "india": {
        "background": "#170B14", "plot_background": "#291323", "text": "#FEF08A",
        "accent": "#FF9933", "pulse": "#138808",
        "border_start": "#D97706", "border_end": "#831843",
        "legend_title": "#FF9933", "legend_text": "#FEF08A",
        "hue_start": 15.0, "hue_end": 145.0, "saturation": 0.85, "lightness": 0.50,
    },
    "mexico": {
        "background": "#0C120E", "plot_background": "#152019", "text": "#FFFFFF",
        "accent": "#009959", "pulse": "#CE1126",
        "border_start": "#009959", "border_end": "#8B0015",
        "legend_title": "#009959", "legend_text": "#FFFFFF",
        "hue_start": 160.0, "hue_end": -20.0, "saturation": 0.80, "lightness": 0.55,
    },
    "fiesta": {
        "background": "#141011", "plot_background": "#241A1E", "text": "#FDE047",
        "accent": "#E4007C", "pulse": "#10B981",
        "border_start": "#E4007C", "border_end": "#047857",
        "legend_title": "#E4007C", "legend_text": "#FEF08A",
        "hue_start": 330.0, "hue_end": 150.0, "saturation": 0.85, "lightness": 0.55,
    },
    "greece": {
        "background": "#FAFAFA", "plot_background": "#F0F0F0", "text": "#004C98",
        "accent": "#004C98", "pulse": "#00BFFF",
        "border_start": "#003366", "border_end": "#CCCCCC",
        "legend_title": "#004C98", "legend_text": "#004C98",
        "hue_start": 240.0, "hue_end": 180.0, "saturation": 0.90, "lightness": 0.40,
    },
    "egypt": {
        "background": "#F7EED2", "plot_background": "#EADCA6", "text": "#2B2311",
        "accent": "#1B4A87", "pulse": "#C2A42D",
        "border_start": "#C2A42D", "border_end": "#B5A475",
        "legend_title": "#1B4A87", "legend_text": "#2B2311",
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
        "legend_title": "#B5651D", "legend_text": "#D4A373",
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
        "border_start": "#BD93F9", "border_end": "#44475A",
        "legend_title": "#FF79C6", "legend_text": "#F8F8F2",
        "hue_start": 330.0, "hue_end": 135.0, "saturation": 0.70, "lightness": 0.65,
    },
    "mocha": {
        "background": "#1E1E2E", "plot_background": "#242438", "text": "#CDD6F4",
        "accent": "#CBA6F7", "pulse": "#94E2D5",
        "border_start": "#89B4FA", "border_end": "#45475A",
        "legend_title": "#CBA6F7", "legend_text": "#CDD6F4",
        "hue_start": 215.0, "hue_end": 335.0, "saturation": 0.80, "lightness": 0.75,
    },
    "nord": {
        "background": "#2E3440", "plot_background": "#3B4252", "text": "#ECEFF4",
        "accent": "#88C0D0", "pulse": "#A3BE8C",
        "border_start": "#81A1C1", "border_end": "#434C5E",
        "legend_title": "#88C0D0", "legend_text": "#ECEFF4",
        "hue_start": 210.0, "hue_end": 90.0, "saturation": 0.45, "lightness": 0.65,
    },
    "solarized_dark": {
        "background": "#002B36", "plot_background": "#073642", "text": "#839496",
        "accent": "#B58900", "pulse": "#2AA198",
        "border_start": "#CB4B16", "border_end": "#002B36",
        "legend_title": "#B58900", "legend_text": "#839496",
        "hue_start": 30.0, "hue_end": 190.0, "saturation": 0.65, "lightness": 0.45,
    },
    "solarized_light": {
        "background": "#FDF6E3", "plot_background": "#EEE8D5", "text": "#657B83",
        "accent": "#268BD2", "pulse": "#D33682",
        "border_start": "#2AA198", "border_end": "#CCC5B2",
        "legend_title": "#268BD2", "legend_text": "#657B83",
        "hue_start": 190.0, "hue_end": 340.0, "saturation": 0.65, "lightness": 0.50,
    },
    "heaven": {
        "background": "#F8FAFC", "plot_background": "#F1F5F9", "text": "#334155",
        "accent": "#0EA5E9", "pulse": "#F59E0B",
        "border_start": "#38BDF8", "border_end": "#FBBF24",
        "legend_title": "#0284C7", "legend_text": "#475569",
        "hue_start": 210.0, "hue_end": 30.0, "saturation": 0.80, "lightness": 0.65,
    },
    "hell": {
        "background": "#0A0303", "plot_background": "#170505", "text": "#FF6600",
        "accent": "#CC0000", "pulse": "#FF9900",
        "border_start": "#FF3300", "border_end": "#4D0000",
        "legend_title": "#CC0000", "legend_text": "#FF6600",
        "hue_start": 330.0, "hue_end": 420.0, "saturation": 0.90, "lightness": 0.45,
    },
    "abyss": {
        "background": "#010A14", "plot_background": "#021226", "text": "#64FFDA",
        "accent": "#00B4D8", "pulse": "#03045E",
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
