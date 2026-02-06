"""Control panel widget for user interactions."""
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QPushButton,
    QLineEdit, QLabel, QComboBox, QSpinBox, QCheckBox, QTextEdit, QScrollArea
)
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIntValidator, QFont
from src.config import MIN_NODE_VALUE, MAX_NODE_VALUE


class ControlPanel(QWidget):
    """
    Control panel for user interactions with the BST.
    Provides buttons and input fields for all operations.
    """
    
    # Signals
    insert_requested = pyqtSignal(int)
    delete_requested = pyqtSignal(int)
    search_requested = pyqtSignal(int)
    reset_requested = pyqtSignal()
    random_tree_requested = pyqtSignal(int)  # Emits number of nodes
    traversal_requested = pyqtSignal(str)  # Emits traversal type
    undo_requested = pyqtSignal()
    redo_requested = pyqtSignal()
    theme_toggled = pyqtSignal(bool)  # Emits True for dark
    
    def __init__(self, parent=None):
        """Initialize the control panel."""
        super().__init__(parent)
        # Don't set fixed width - let parent handle sizing
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface."""
        # Use scroll area for responsive, fullscreen-friendly design
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")
        
        scroll_content = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)
        
        # Title
        title = QLabel("🌳 BST Controls")
        title_font = QFont("Segoe UI", 14, QFont.Bold)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # ===== Insert Section =====
        insert_group = self._create_insert_section()
        layout.addWidget(insert_group)
        
        # ===== Delete Section =====
        delete_group = self._create_delete_section()
        layout.addWidget(delete_group)
        
        # ===== Search Section =====
        search_group = self._create_search_section()
        layout.addWidget(search_group)
        
        # ===== Traversal Section =====
        traversal_group = self._create_traversal_section()
        layout.addWidget(traversal_group)
        
        # ===== Tree Generation =====
        generation_group = self._create_tree_generation_section()
        layout.addWidget(generation_group)
        
        # ===== Tree Operations =====
        operations_group = self._create_operations_section()
        layout.addWidget(operations_group)
        
        # ===== Settings =====
        settings_group = self._create_settings_section()
        layout.addWidget(settings_group)
        
        # ===== Output Display =====
        output_group = self._create_output_section()
        layout.addWidget(output_group)
        
        # Add stretch to push everything to the top
        layout.addStretch()
        
        scroll_content.setLayout(layout)
        scroll.setWidget(scroll_content)
        
        # Main layout with scroll area
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(scroll)
        self.setLayout(main_layout)
    
    def _create_insert_section(self) -> QGroupBox:
        """Create the insert node section."""
        group = QGroupBox("📥 Insert Node")
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        # Input field
        input_label = QLabel("Node Value:")
        input_label.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.insert_input = QLineEdit()
        self.insert_input.setPlaceholderText("Enter value (e.g., 50)")
        self.insert_input.setValidator(
            QIntValidator(MIN_NODE_VALUE, MAX_NODE_VALUE)
        )
        self.insert_input.setMinimumHeight(40)
        self.insert_input.setFont(QFont("Segoe UI", 11))
        self.insert_input.returnPressed.connect(self._on_insert_clicked)
        self.insert_input.setToolTip("Enter an integer value and press Enter or click Insert")
        
        layout.addWidget(input_label)
        layout.addWidget(self.insert_input)
        
        # Insert button
        self.insert_btn = QPushButton("✓ Insert Node")
        self.insert_btn.setObjectName("successButton")
        self.insert_btn.setMinimumHeight(45)
        self.insert_btn.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.insert_btn.clicked.connect(self._on_insert_clicked)
        self.insert_btn.setToolTip("Click to insert the node into the BST")
        layout.addWidget(self.insert_btn)
        
        group.setLayout(layout)
        return group
    
    def _on_insert_clicked(self):
        """Handle insert button click."""
        try:
            value = int(self.insert_input.text())
            self.insert_requested.emit(value)
            self.insert_input.clear()
        except ValueError:
            self.insert_input.setStyleSheet("border: 2px solid red;")
    
    def _create_delete_section(self) -> QGroupBox:
        """Create the delete node section."""
        group = QGroupBox("🗑️ Delete Node")
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        # Input field
        input_label = QLabel("Node Value:")
        input_label.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.delete_input = QLineEdit()
        self.delete_input.setPlaceholderText("Enter value to delete")
        self.delete_input.setValidator(
            QIntValidator(MIN_NODE_VALUE, MAX_NODE_VALUE)
        )
        self.delete_input.setMinimumHeight(40)
        self.delete_input.setFont(QFont("Segoe UI", 11))
        self.delete_input.returnPressed.connect(self._on_delete_clicked)
        self.delete_input.setToolTip("Enter the value of node to delete")
        
        layout.addWidget(input_label)
        layout.addWidget(self.delete_input)
        
        # Delete button
        self.delete_btn = QPushButton("✕ Delete Node")
        self.delete_btn.setObjectName("dangerButton")
        self.delete_btn.setMinimumHeight(45)
        self.delete_btn.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.delete_btn.clicked.connect(self._on_delete_clicked)
        self.delete_btn.setToolTip("Click to delete the node from the BST")
        layout.addWidget(self.delete_btn)
        
        group.setLayout(layout)
        return group
    
    def _on_delete_clicked(self):
        """Handle delete button click."""
        try:
            value = int(self.delete_input.text())
            self.delete_requested.emit(value)
            self.delete_input.clear()
        except ValueError:
            self.delete_input.setStyleSheet("border: 2px solid red;")
    
    def _create_search_section(self) -> QGroupBox:
        """Create the search node section."""
        group = QGroupBox("🔍 Search Node")
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        # Input field
        input_label = QLabel("Node Value:")
        input_label.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Enter value to search")
        self.search_input.setValidator(
            QIntValidator(MIN_NODE_VALUE, MAX_NODE_VALUE)
        )
        self.search_input.setMinimumHeight(40)
        self.search_input.setFont(QFont("Segoe UI", 11))
        self.search_input.returnPressed.connect(self._on_search_clicked)
        self.search_input.setToolTip("Enter the value to search for in the tree")
        
        layout.addWidget(input_label)
        layout.addWidget(self.search_input)
        
        # Search button
        self.search_btn = QPushButton("🔎 Search")
        self.search_btn.setMinimumHeight(45)
        self.search_btn.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.search_btn.clicked.connect(self._on_search_clicked)
        self.search_btn.setToolTip("Click to search for the value in the tree")
        layout.addWidget(self.search_btn)
        
        group.setLayout(layout)
        return group
    
    def _on_search_clicked(self):
        """Handle search button click."""
        try:
            value = int(self.search_input.text())
            self.search_requested.emit(value)
        except ValueError:
            self.search_input.setStyleSheet("border: 2px solid red;")
    
    def _create_traversal_section(self) -> QGroupBox:
        """Create the traversal section."""
        group = QGroupBox("🔄 Tree Traversal")
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        # Traversal type selector
        traversal_label = QLabel("Select Type:")
        traversal_label.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.traversal_combo = QComboBox()
        self.traversal_combo.addItems([
            "Inorder (Left→Root→Right)", 
            "Preorder (Root→Left→Right)", 
            "Postorder (Left→Right→Root)", 
            "Level-order (Breadth-First)"
        ])
        self.traversal_combo.setMinimumHeight(40)
        self.traversal_combo.setFont(QFont("Segoe UI", 10))
        
        layout.addWidget(traversal_label)
        layout.addWidget(self.traversal_combo)
        
        # Animate checkbox
        self.animate_traversal_check = QCheckBox("🎬 Animate Steps")
        self.animate_traversal_check.setChecked(True)
        self.animate_traversal_check.setFont(QFont("Segoe UI", 10))
        self.animate_traversal_check.setToolTip("Enable step-by-step animation of traversal")
        layout.addWidget(self.animate_traversal_check)
        
        # Traversal button
        self.traversal_btn = QPushButton("▶ Execute Traversal")
        self.traversal_btn.setMinimumHeight(45)
        self.traversal_btn.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.traversal_btn.clicked.connect(self._on_traversal_clicked)
        self.traversal_btn.setToolTip("Click to execute the selected traversal")
        layout.addWidget(self.traversal_btn)
        
        group.setLayout(layout)
        return group
    
    def _on_traversal_clicked(self):
        """Handle traversal button click."""
        combo_text = self.traversal_combo.currentText().lower()
        
        # Extract traversal type from combo text
        if "inorder" in combo_text:
            traversal_type = "inorder"
        elif "preorder" in combo_text:
            traversal_type = "preorder"
        elif "postorder" in combo_text:
            traversal_type = "postorder"
        elif "level-order" in combo_text or "breadth" in combo_text:
            traversal_type = "level-order"
        else:
            traversal_type = "inorder"  # Default
        
        self.traversal_requested.emit(traversal_type)
    
    def _create_tree_generation_section(self) -> QGroupBox:
        """Create the random tree generation section."""
        group = QGroupBox("🎲 Generate Random Tree")
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        # Number of nodes
        count_label = QLabel("Number of Nodes:")
        count_label.setFont(QFont("Segoe UI", 11, QFont.Bold))
        count_layout = QHBoxLayout()
        self.random_count_spin = QSpinBox()
        self.random_count_spin.setMinimum(1)
        self.random_count_spin.setMaximum(50)
        self.random_count_spin.setValue(15)
        self.random_count_spin.setMinimumHeight(40)
        self.random_count_spin.setFont(QFont("Segoe UI", 11))
        count_layout.addWidget(self.random_count_spin)
        count_layout.addStretch()
        
        layout.addWidget(count_label)
        layout.addLayout(count_layout)
        
        # Generate button
        self.random_tree_btn = QPushButton("🎯 Generate Random Tree")
        self.random_tree_btn.setMinimumHeight(45)
        self.random_tree_btn.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.random_tree_btn.clicked.connect(self._on_random_tree_clicked)
        self.random_tree_btn.setToolTip("Generate a random BST with unique values")
        layout.addWidget(self.random_tree_btn)
        
        group.setLayout(layout)
        return group
    
    def _on_random_tree_clicked(self):
        """Handle random tree generation."""
        count = self.random_count_spin.value()
        self.random_tree_requested.emit(count)
    
    def _create_operations_section(self) -> QGroupBox:
        """Create the tree operations section."""
        group = QGroupBox("⚙️ Operations")
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        # Undo/Redo buttons
        undo_redo_layout = QHBoxLayout()
        undo_redo_layout.setSpacing(8)
        self.undo_btn = QPushButton("↶ Undo")
        self.undo_btn.setMinimumHeight(45)
        self.undo_btn.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.undo_btn.clicked.connect(self._on_undo_clicked)
        self.undo_btn.setToolTip("Undo last operation")
        self.redo_btn = QPushButton("↷ Redo")
        self.redo_btn.setMinimumHeight(45)
        self.redo_btn.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.redo_btn.clicked.connect(self._on_redo_clicked)
        self.redo_btn.setToolTip("Redo last undone operation")
        undo_redo_layout.addWidget(self.undo_btn)
        undo_redo_layout.addWidget(self.redo_btn)
        layout.addLayout(undo_redo_layout)
        
        # Reset button
        self.reset_btn = QPushButton("🗑️ Clear Tree")
        self.reset_btn.setObjectName("dangerButton")
        self.reset_btn.setMinimumHeight(45)
        self.reset_btn.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.reset_btn.clicked.connect(self._on_reset_clicked)
        self.reset_btn.setToolTip("Clear all nodes from the tree")
        layout.addWidget(self.reset_btn)
        
        group.setLayout(layout)
        return group
    
    def _on_undo_clicked(self):
        """Handle undo button click."""
        self.undo_requested.emit()
    
    def _on_redo_clicked(self):
        """Handle redo button click."""
        self.redo_requested.emit()
    
    def _on_reset_clicked(self):
        """Handle reset button click."""
        self.reset_requested.emit()
    
    def _create_settings_section(self) -> QGroupBox:
        """Create the settings section."""
        group = QGroupBox("🌙 Settings")
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        # Theme toggle
        self.theme_check = QCheckBox("🌙 Dark Mode")
        self.theme_check.setFont(QFont("Segoe UI", 10))
        self.theme_check.setToolTip("Toggle between light and dark themes")
        self.theme_check.toggled.connect(self._on_theme_toggled)
        layout.addWidget(self.theme_check)
        
        group.setLayout(layout)
        return group
    
    def _on_theme_toggled(self, checked: bool):
        """Handle theme toggle."""
        self.theme_toggled.emit(checked)
    
    def _create_output_section(self) -> QGroupBox:
        """Create the output display section."""
        group = QGroupBox("📊 Traversal Output")
        layout = QVBoxLayout()
        layout.setSpacing(8)
        
        # Output text display
        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)
        self.output_display.setMaximumHeight(120)
        self.output_display.setFont(QFont("Courier New", 10))
        self.output_display.setPlaceholderText("Traversal results will appear here...")
        
        layout.addWidget(self.output_display)
        
        group.setLayout(layout)
        return group
    
    def set_output(self, text: str):
        """
        Set the output display text.
        
        Args:
            text: Text to display
        """
        self.output_display.setText(text)
    
    def enable_undo(self, enabled: bool):
        """Enable/disable undo button."""
        self.undo_btn.setEnabled(enabled)
    
    def enable_redo(self, enabled: bool):
        """Enable/disable redo button."""
        self.redo_btn.setEnabled(enabled)
