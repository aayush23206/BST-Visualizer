"""Professional styling for BST Visualizer UI."""
from src.config import COLORS_LIGHT, COLORS_DARK


def get_light_theme_stylesheet() -> str:
    """Get the light theme stylesheet."""
    return f"""
    QMainWindow {{
        background-color: {COLORS_LIGHT['background']};
    }}
    
    QWidget {{
        background-color: {COLORS_LIGHT['background']};
        color: {COLORS_LIGHT['text']};
    }}
    
    QGroupBox {{
        border: 2px solid {COLORS_LIGHT['primary']};
        border-radius: 8px;
        margin-top: 12px;
        padding-top: 12px;
        font-weight: bold;
        font-size: 12px;
        color: {COLORS_LIGHT['text']};
    }}
    
    QGroupBox::title {{
        subcontrol-origin: margin;
        left: 15px;
        padding: 0 5px 0 5px;
    }}
    
    QPushButton {{
        background-color: {COLORS_LIGHT['primary']};
        color: white;
        border: none;
        border-radius: 6px;
        padding: 10px 20px;
        font-weight: bold;
        font-size: 12px;
        min-height: 40px;
    }}
    
    QPushButton:hover {{
        background-color: #2980b9;
        transform: scale(1.02);
    }}
    
    QPushButton:pressed {{
        background-color: #2471a3;
    }}
    
    QPushButton:disabled {{
        background-color: #bdc3c7;
        color: #95a5a6;
    }}
    
    QPushButton#dangerButton {{
        background-color: {COLORS_LIGHT['danger']};
    }}
    
    QPushButton#dangerButton:hover {{
        background-color: #c0392b;
    }}
    
    QPushButton#successButton {{
        background-color: {COLORS_LIGHT['success']};
    }}
    
    QPushButton#successButton:hover {{
        background-color: #27ae60;
    }}
    
    QLineEdit {{
        border: 2px solid {COLORS_LIGHT['border']};
        border-radius: 6px;
        padding: 10px;
        background-color: {COLORS_LIGHT['background']};
        color: {COLORS_LIGHT['text']};
        font-size: 12px;
        min-height: 38px;
    }}
    
    QLineEdit:focus {{
        border: 2px solid {COLORS_LIGHT['primary']};
    }}
    
    QLabel {{
        color: {COLORS_LIGHT['text']};
        font-size: 12px;
    }}
    
    QComboBox {{
        border: 2px solid {COLORS_LIGHT['border']};
        border-radius: 5px;
        padding: 6px;
        background-color: {COLORS_LIGHT['background']};
        color: {COLORS_LIGHT['text']};
    }}
    
    QComboBox:focus {{
        border: 2px solid {COLORS_LIGHT['primary']};
    }}
    
    QSpinBox {{
        border: 2px solid {COLORS_LIGHT['border']};
        border-radius: 5px;
        padding: 6px;
        background-color: {COLORS_LIGHT['background']};
        color: {COLORS_LIGHT['text']};
    }}
    
    QTextEdit {{
        border: 2px solid {COLORS_LIGHT['border']};
        border-radius: 5px;
        padding: 8px;
        background-color: {COLORS_LIGHT['background']};
        color: {COLORS_LIGHT['text']};
        font-family: Courier New;
        font-size: 10px;
    }}
    
    QSlider::groove:horizontal {{
        border: 1px solid {COLORS_LIGHT['border']};
        height: 8px;
        background: {COLORS_LIGHT['light']};
        border-radius: 4px;
    }}
    
    QSlider::handle:horizontal {{
        background: {COLORS_LIGHT['primary']};
        border: 1px solid {COLORS_LIGHT['primary']};
        width: 18px;
        margin: -5px 0;
        border-radius: 9px;
    }}
    
    QSlider::handle:horizontal:hover {{
        background: #2980b9;
    }}
    
    QCheckBox {{
        color: {COLORS_LIGHT['text']};
        font-size: 11px;
    }}
    
    QCheckBox::indicator {{
        width: 18px;
        height: 18px;
    }}
    
    QCheckBox::indicator:unchecked {{
        background-color: {COLORS_LIGHT['background']};
        border: 2px solid {COLORS_LIGHT['border']};
        border-radius: 3px;
    }}
    
    QCheckBox::indicator:checked {{
        background-color: {COLORS_LIGHT['primary']};
        border: 2px solid {COLORS_LIGHT['primary']};
        border-radius: 3px;
    }}
    
    QStatusBar {{
        background-color: {COLORS_LIGHT['background']};
        color: {COLORS_LIGHT['text']};
        border-top: 1px solid {COLORS_LIGHT['border']};
    }}
    
    QMenuBar {{
        background-color: {COLORS_LIGHT['background']};
        color: {COLORS_LIGHT['text']};
        border-bottom: 1px solid {COLORS_LIGHT['border']};
    }}
    
    QMenu {{
        background-color: {COLORS_LIGHT['background']};
        color: {COLORS_LIGHT['text']};
        border: 1px solid {COLORS_LIGHT['border']};
    }}
    
    QMenu::item:selected {{
        background-color: {COLORS_LIGHT['primary']};
        color: white;
    }}
    """


def get_dark_theme_stylesheet() -> str:
    """Get the dark theme stylesheet."""
    return f"""
    QMainWindow {{
        background-color: {COLORS_DARK['background']};
    }}
    
    QWidget {{
        background-color: {COLORS_DARK['background']};
        color: {COLORS_DARK['text']};
    }}
    
    QGroupBox {{
        border: 2px solid {COLORS_DARK['primary']};
        border-radius: 8px;
        margin-top: 12px;
        padding-top: 12px;
        font-weight: bold;
        font-size: 12px;
        color: {COLORS_DARK['text']};
    }}
    
    QGroupBox::title {{
        subcontrol-origin: margin;
        left: 15px;
        padding: 0 5px 0 5px;
    }}
    
    QPushButton {{
        background-color: {COLORS_DARK['primary']};
        color: white;
        border: none;
        border-radius: 6px;
        padding: 10px 20px;
        font-weight: bold;
        font-size: 12px;
        min-height: 40px;
    }}
    
    QPushButton:hover {{
        background-color: #2980b9;
    }}
    
    QPushButton:pressed {{
        background-color: #1f618d;
    }}
    
    QPushButton:disabled {{
        background-color: #555555;
        color: #888888;
    }}
    
    QPushButton#dangerButton {{
        background-color: {COLORS_DARK['danger']};
    }}
    
    QPushButton#dangerButton:hover {{
        background-color: #a93226;
    }}
    
    QPushButton#successButton {{
        background-color: {COLORS_DARK['success']};
    }}
    
    QPushButton#successButton:hover {{
        background-color: #28a745;
    }}
    
    QLineEdit {{
        border: 2px solid {COLORS_DARK['border']};
        border-radius: 6px;
        padding: 10px;
        background-color: #1a1a1a;
        color: {COLORS_DARK['text']};
        font-size: 12px;
        min-height: 38px;
    }}
    
    QLineEdit:focus {{
        border: 2px solid {COLORS_DARK['primary']};
    }}
    
    QLabel {{
        color: {COLORS_DARK['text']};
        font-size: 12px;
    }}
    
    QComboBox {{
        border: 2px solid {COLORS_DARK['border']};
        border-radius: 5px;
        padding: 6px;
        background-color: #1a1a1a;
        color: {COLORS_DARK['text']};
    }}
    
    QComboBox:focus {{
        border: 2px solid {COLORS_DARK['primary']};
    }}
    
    QSpinBox {{
        border: 2px solid {COLORS_DARK['border']};
        border-radius: 5px;
        padding: 6px;
        background-color: #1a1a1a;
        color: {COLORS_DARK['text']};
    }}
    
    QTextEdit {{
        border: 2px solid {COLORS_DARK['border']};
        border-radius: 5px;
        padding: 8px;
        background-color: #1a1a1a;
        color: {COLORS_DARK['text']};
        font-family: Courier New;
        font-size: 10px;
    }}
    
    QSlider::groove:horizontal {{
        border: 1px solid {COLORS_DARK['border']};
        height: 8px;
        background: #444444;
        border-radius: 4px;
    }}
    
    QSlider::handle:horizontal {{
        background: {COLORS_DARK['primary']};
        border: 1px solid {COLORS_DARK['primary']};
        width: 18px;
        margin: -5px 0;
        border-radius: 9px;
    }}
    
    QSlider::handle:horizontal:hover {{
        background: #2980b9;
    }}
    
    QCheckBox {{
        color: {COLORS_DARK['text']};
        font-size: 11px;
    }}
    
    QCheckBox::indicator {{
        width: 18px;
        height: 18px;
    }}
    
    QCheckBox::indicator:unchecked {{
        background-color: #1a1a1a;
        border: 2px solid {COLORS_DARK['border']};
        border-radius: 3px;
    }}
    
    QCheckBox::indicator:checked {{
        background-color: {COLORS_DARK['primary']};
        border: 2px solid {COLORS_DARK['primary']};
        border-radius: 3px;
    }}
    
    QStatusBar {{
        background-color: {COLORS_DARK['background']};
        color: {COLORS_DARK['text']};
        border-top: 1px solid {COLORS_DARK['border']};
    }}
    
    QMenuBar {{
        background-color: {COLORS_DARK['background']};
        color: {COLORS_DARK['text']};
        border-bottom: 1px solid {COLORS_DARK['border']};
    }}
    
    QMenu {{
        background-color: {COLORS_DARK['background']};
        color: {COLORS_DARK['text']};
        border: 1px solid {COLORS_DARK['border']};
    }}
    
    QMenu::item:selected {{
        background-color: {COLORS_DARK['primary']};
        color: white;
    }}
    """


class ThemeManager:
    """Manages application themes (light/dark)."""
    
    LIGHT = "light"
    DARK = "dark"
    
    def __init__(self):
        """Initialize theme manager with light theme."""
        self.current_theme = self.LIGHT
    
    def get_stylesheet(self) -> str:
        """Get the current theme stylesheet."""
        if self.current_theme == self.DARK:
            return get_dark_theme_stylesheet()
        return get_light_theme_stylesheet()
    
    def toggle_theme(self):
        """Toggle between light and dark themes."""
        self.current_theme = self.DARK if self.current_theme == self.LIGHT else self.LIGHT
    
    def set_theme(self, theme: str):
        """
        Set the current theme.
        
        Args:
            theme: Theme name (LIGHT or DARK)
        """
        if theme in [self.LIGHT, self.DARK]:
            self.current_theme = theme
    
    def is_dark_theme(self) -> bool:
        """Return True if current theme is dark."""
        return self.current_theme == self.DARK
