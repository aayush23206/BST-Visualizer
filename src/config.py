"""Configuration and constants for BST Visualizer."""

# Window configuration
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 1000
WINDOW_TITLE = "BST Visualizer - Professional Edition"

# Canvas configuration (responsive - these are just defaults)
CANVAS_WIDTH = 1100
CANVAS_HEIGHT = 900
CANVAS_BACKGROUND_LIGHT = "#ffffff"
CANVAS_BACKGROUND_DARK = "#2b2b2b"

# Node visualization
NODE_RADIUS = 25
NODE_LABEL_FONT_SIZE = 11
NODE_COLOR_DEFAULT_LIGHT = "#3498db"
NODE_COLOR_DEFAULT_DARK = "#3498db"
NODE_COLOR_HIGHLIGHTED = "#e74c3c"
NODE_COLOR_SEARCHING = "#f39c12"
NODE_BORDER_WIDTH = 2
NODE_BORDER_COLOR = "#2c3e50"

# Edge visualization
EDGE_COLOR_LIGHT = "#34495e"
EDGE_COLOR_DARK = "#95a5a6"
EDGE_WIDTH = 2

# Text colors
TEXT_COLOR_LIGHT = "#2c3e50"
TEXT_COLOR_DARK = "#ecf0f1"

# Animation configuration
ANIMATION_DURATION = 500  # milliseconds
ANIMATION_STEPS = 20
HIGHLIGHT_DURATION = 800  # milliseconds
TRAVERSAL_STEP_DELAY = 400  # milliseconds

# Spacing
VERTICAL_GAP = 120
HORIZONTAL_GAP = 100
TOP_MARGIN = 60

# Button styling
BUTTON_PADDING = "12px 24px"
BUTTON_BORDER_RADIUS = "6px"
BUTTON_FONT_SIZE = 12

# Colors - Light Theme
COLORS_LIGHT = {
    "primary": "#3498db",
    "success": "#2ecc71",
    "warning": "#f39c12",
    "danger": "#e74c3c",
    "dark": "#2c3e50",
    "light": "#ecf0f1",
    "border": "#bdc3c7",
    "text": "#2c3e50",
    "background": "#ffffff",
}

# Colors - Dark Theme
COLORS_DARK = {
    "primary": "#3498db",
    "success": "#2ecc71",
    "warning": "#f39c12",
    "danger": "#e74c3c",
    "dark": "#1a1a1a",
    "light": "#ecf0f1",
    "border": "#444444",
    "text": "#ecf0f1",
    "background": "#2b2b2b",
}

# Traversal colors
TRAVERSAL_COLORS = {
    "inorder": "#9b59b6",
    "preorder": "#1abc9c",
    "postorder": "#e67e22",
    "levelorder": "#c0392b",
}

# UI Layout
CONTROL_PANEL_WIDTH = 400
CONTROL_PANEL_HEIGHT = 950

# Input validation
MIN_NODE_VALUE = -9999
MAX_NODE_VALUE = 9999
MAX_TREE_SIZE = 100

# History (Undo/Redo)
MAX_HISTORY_SIZE = 50

# Export settings
EXPORT_IMAGE_SCALE = 2
EXPORT_IMAGE_QUALITY = 95
