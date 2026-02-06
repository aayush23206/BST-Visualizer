"""Information panel for displaying tree statistics."""
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QLabel, QHBoxLayout, QScrollArea
from PyQt5.QtGui import QFont


class InfoPanel(QWidget):
    """
    Displays information about the current tree state.
    Shows size, height, balance status, etc.
    """
    
    def __init__(self, parent=None):
        """Initialize the info panel."""
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface."""
        # Use scroll area for responsive design
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; }")
        
        scroll_content = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)
        
        # Title
        title = QLabel("📈 Tree Statistics")
        title_font = QFont("Segoe UI", 12, QFont.Bold)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # ===== Tree Info Group =====
        info_group = QGroupBox("🌳 Tree Info")
        info_layout = QVBoxLayout()
        info_layout.setSpacing(8)
        
        self.size_label = QLabel("🔢 Nodes: 0")
        self.size_label.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.height_label = QLabel("📏 Height: -1")
        self.height_label.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.balance_label = QLabel("⚖️ Balanced: -")
        self.balance_label.setFont(QFont("Segoe UI", 11, QFont.Bold))
        
        info_layout.addWidget(self.size_label)
        info_layout.addWidget(self.height_label)
        info_layout.addWidget(self.balance_label)
        
        info_group.setLayout(info_layout)
        layout.addWidget(info_group)
        
        # ===== Last Operation =====
        operation_group = QGroupBox("✓ Last Operation")
        operation_layout = QVBoxLayout()
        operation_layout.setSpacing(5)
        
        self.operation_label = QLabel("None")
        self.operation_label.setFont(QFont("Segoe UI", 10))
        self.operation_label.setWordWrap(True)
        operation_layout.addWidget(self.operation_label)
        
        operation_group.setLayout(operation_layout)
        layout.addWidget(operation_group)
        
        # ===== Messages =====
        message_group = QGroupBox("💬 Status")
        message_layout = QVBoxLayout()
        message_layout.setSpacing(5)
        
        self.message_label = QLabel("Ready")
        self.message_label.setFont(QFont("Segoe UI", 10))
        self.message_label.setWordWrap(True)
        message_layout.addWidget(self.message_label)
        
        message_group.setLayout(message_layout)
        layout.addWidget(message_group)
        
        layout.addStretch()
        
        scroll_content.setLayout(layout)
        scroll.setWidget(scroll_content)
        
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(scroll)
        self.setLayout(main_layout)
    
    def update_tree_info(self, size: int, height: int, is_balanced: bool):
        """
        Update tree statistics display.
        
        Args:
            size: Number of nodes
            height: Height of tree
            is_balanced: Whether tree is balanced
        """
        self.size_label.setText(f"Nodes: {size}")
        self.height_label.setText(f"Height: {height}")
        
        balance_text = "Yes" if is_balanced else "No"
        self.balance_label.setText(f"Balanced: {balance_text}")
    
    def set_last_operation(self, text: str):
        """
        Set the last operation display.
        
        Args:
            text: Operation description
        """
        self.operation_label.setText(text)
    
    def set_message(self, text: str):
        """
        Set a message in the info panel.
        
        Args:
            text: Message to display
        """
        self.message_label.setText(text)
    
    def clear(self):
        """Clear all information."""
        self.size_label.setText("Nodes: 0")
        self.height_label.setText("Height: -1")
        self.balance_label.setText("Balanced: -")
        self.operation_label.setText("None")
        self.message_label.setText("Tree cleared")
