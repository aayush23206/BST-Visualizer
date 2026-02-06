"""Main application window."""
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QIcon
import random
from typing import List, Optional

from src.models import BinarySearchTree
from src.ui.widgets import TreeCanvas, ControlPanel, InfoPanel
from src.ui.styles import ThemeManager
from src.utils import OperationHistory, Operation, TreeExporter
from src.config import (
    WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, MAX_TREE_SIZE,
    MAX_NODE_VALUE, MIN_NODE_VALUE
)


class MainWindow(QMainWindow):
    """
    Main application window combining all components.
    Manages user interactions and coordinates between BST model and UI.
    """
    
    def __init__(self):
        """Initialize the main window."""
        super().__init__()
        
        # Initialize components
        self.tree = BinarySearchTree()
        self.history = OperationHistory()
        self.theme_manager = ThemeManager()
        self.exporter = TreeExporter()
        
        # Track original tree state for undo/redo
        self.operation_in_progress = False
        
        # Setup UI
        self.init_ui()
        
        # Connect signals
        self.connect_signals()
        
        # Show welcome message
        self.info_panel.set_message("Welcome to BST Visualizer! Insert nodes to get started.")
    
    def init_ui(self):
        """Initialize the user interface."""
        # Set window properties
        self.setWindowTitle(WINDOW_TITLE)
        self.setGeometry(50, 50, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setMinimumSize(1200, 700)  # Minimum size for usability
        
        # Create central widget with layout
        central_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(12, 12, 12, 12)
        main_layout.setSpacing(12)
        
        # Create canvas with better styling and scaling
        self.canvas = TreeCanvas()
        self.canvas.set_tree(self.tree)
        self.canvas.setStyleSheet("border: 3px solid #3498db; border-radius: 8px;")
        main_layout.addWidget(self.canvas, 2)  # Takes 2/3 of space
        
        # Create side panel with two columns in vertical stack
        side_layout = QVBoxLayout()
        side_layout.setContentsMargins(0, 0, 0, 0)
        side_layout.setSpacing(12)
        
        self.control_panel = ControlPanel()
        self.info_panel = InfoPanel()
        
        side_layout.addWidget(self.control_panel, 1)  # Takes 50% of side panel
        side_layout.addWidget(self.info_panel, 1)     # Takes 50% of side panel
        
        side_widget = QWidget()
        side_widget.setLayout(side_layout)
        side_widget.setMinimumWidth(400)  # Minimum for usability
        side_widget.setMaximumWidth(600)  # Maximum to prevent stretching too wide
        
        main_layout.addWidget(side_widget, 1)  # Takes 1/3 of space
        
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        
        # Apply theme
        self.apply_theme()
    
    def resizeEvent(self, event):
        """Handle window resize events for responsive layout."""
        super().resizeEvent(event)
        # Redraw the tree to fit the new window size
        if self.tree and not self.tree.is_empty():
            self.canvas.redraw()
    
    def connect_signals(self):
        """Connect signals from widgets to slots."""
        # Control panel signals
        self.control_panel.insert_requested.connect(self.on_insert)
        self.control_panel.delete_requested.connect(self.on_delete)
        self.control_panel.search_requested.connect(self.on_search)
        self.control_panel.reset_requested.connect(self.on_reset)
        self.control_panel.random_tree_requested.connect(self.on_generate_random_tree)
        self.control_panel.traversal_requested.connect(self.on_traversal)
        self.control_panel.undo_requested.connect(self.on_undo)
        self.control_panel.redo_requested.connect(self.on_redo)
        self.control_panel.theme_toggled.connect(self.on_theme_toggle)
        
        # Canvas signals
        self.canvas.node_clicked.connect(self.on_node_clicked)
    
    @pyqtSlot(int)
    def on_insert(self, value: int):
        """
        Handle node insertion.
        
        Args:
            value: Node value to insert
        """
        if self.tree.get_size() >= MAX_TREE_SIZE:
            self.info_panel.set_message(f"Error: Maximum tree size ({MAX_TREE_SIZE}) reached!")
            return
        
        # Create operation for undo/redo
        original_tree_state = self._get_tree_state()
        
        def undo_action():
            self._restore_tree_state(original_tree_state)
            self.update_display()
        
        if self.tree.insert(value):
            new_tree_state = self._get_tree_state()
            
            def redo_action():
                self._restore_tree_state(new_tree_state)
                self.update_display()
            
            # Record operation
            operation = Operation(
                name=f"Insert {value}",
                undo_action=undo_action,
                redo_action=redo_action
            )
            self.history.record_operation(operation)
            
            # Highlight the inserted node
            self.canvas.highlight_node(value, 600)
            self.info_panel.set_last_operation(f"Inserted node: {value}")
            self.info_panel.set_message(f"Successfully inserted {value}")
        else:
            self.info_panel.set_message(f"Error: {value} already exists in the tree!")
            return
        
        self.update_display()
    
    @pyqtSlot(int)
    def on_delete(self, value: int):
        """
        Handle node deletion.
        
        Args:
            value: Node value to delete
        """
        original_tree_state = self._get_tree_state()
        
        def undo_action():
            self._restore_tree_state(original_tree_state)
            self.update_display()
        
        if self.tree.delete(value):
            new_tree_state = self._get_tree_state()
            
            def redo_action():
                self._restore_tree_state(new_tree_state)
                self.update_display()
            
            operation = Operation(
                name=f"Delete {value}",
                undo_action=undo_action,
                redo_action=redo_action
            )
            self.history.record_operation(operation)
            
            self.info_panel.set_last_operation(f"Deleted node: {value}")
            self.info_panel.set_message(f"Successfully deleted {value}")
        else:
            self.info_panel.set_message(f"Error: {value} not found in the tree!")
            return
        
        self.update_display()
    
    @pyqtSlot(int)
    def on_search(self, value: int):
        """
        Handle node search.
        
        Args:
            value: Node value to search for
        """
        result = self.tree.search(value)
        
        if result:
            self.canvas.highlight_node(value, 1000)
            self.info_panel.set_message(f"Found: {value} in the tree! ✓")
            self.info_panel.set_last_operation(f"Search successful: {value}")
        else:
            self.info_panel.set_message(f"Not found: {value} is not in the tree!")
            self.info_panel.set_last_operation(f"Search failed: {value}")
        
        self.canvas.redraw()
    
    @pyqtSlot()
    def on_reset(self):
        """Handle tree reset/clear."""
        if self.tree.is_empty():
            self.info_panel.set_message("Tree is already empty!")
            return
        
        # Confirmation dialog
        reply = QMessageBox.question(
            self,
            "Clear Tree",
            "Are you sure you want to clear the entire tree?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            original_tree_state = self._get_tree_state()
            
            def undo_action():
                self._restore_tree_state(original_tree_state)
                self.update_display()
            
            self.tree.clear()
            self.history.clear()
            
            new_tree_state = self._get_tree_state()
            
            def redo_action():
                self._restore_tree_state(new_tree_state)
                self.update_display()
            
            operation = Operation(
                name="Clear tree",
                undo_action=undo_action,
                redo_action=redo_action
            )
            self.history.record_operation(operation)
            
            self.info_panel.clear()
            self.info_panel.set_message("Tree cleared!")
            self.update_display()
    
    @pyqtSlot(int)
    def on_generate_random_tree(self, count: int):
        """
        Generate a random tree.
        
        Args:
            count: Number of nodes to generate
        """
        original_tree_state = self._get_tree_state()
        
        def undo_action():
            self._restore_tree_state(original_tree_state)
            self.update_display()
        
        self.tree.clear()
        
        # Generate random values
        values = []
        while len(values) < count:
            val = random.randint(MIN_NODE_VALUE, MAX_NODE_VALUE)
            if val not in values:
                values.append(val)
        
        # Insert values
        for val in values:
            self.tree.insert(val)
        
        new_tree_state = self._get_tree_state()
        
        def redo_action():
            self._restore_tree_state(new_tree_state)
            self.update_display()
        
        operation = Operation(
            name=f"Generate random tree ({count} nodes)",
            undo_action=undo_action,
            redo_action=redo_action
        )
        self.history.record_operation(operation)
        
        self.info_panel.set_message(f"Generated random tree with {count} nodes!")
        self.update_display()
    
    @pyqtSlot(str)
    def on_traversal(self, traversal_type: str):
        """
        Perform tree traversal.
        
        Args:
            traversal_type: Type of traversal (inorder, preorder, postorder, level-order)
        """
        if self.tree.is_empty():
            self.info_panel.set_message("Error: Cannot traverse empty tree!")
            return
        
        # Get traversal result
        if traversal_type == "inorder":
            result = self.tree.inorder_traversal()
        elif traversal_type == "preorder":
            result = self.tree.preorder_traversal()
        elif traversal_type == "postorder":
            result = self.tree.postorder_traversal()
        elif traversal_type == "level-order":
            result = self.tree.levelorder_traversal()
        else:
            return
        
        # Display result
        result_str = " → ".join(map(str, result))
        self.control_panel.set_output(result_str)
        self.info_panel.set_last_operation(f"{traversal_type.title()} traversal")
        
        # Animate if checkbox is checked
        if self.control_panel.animate_traversal_check.isChecked():
            self.canvas.animate_traversal(result)
        else:
            self.canvas.clear_search_path()
    
    @pyqtSlot()
    def on_undo(self):
        """Handle undo operation."""
        if self.history.undo():
            self.info_panel.set_message("Undone!")
            self.update_display()
        else:
            self.info_panel.set_message("Nothing to undo!")
    
    @pyqtSlot()
    def on_redo(self):
        """Handle redo operation."""
        if self.history.redo():
            self.info_panel.set_message("Redone!")
            self.update_display()
        else:
            self.info_panel.set_message("Nothing to redo!")
    
    @pyqtSlot(bool)
    def on_theme_toggle(self, dark: bool):
        """
        Handle theme toggle.
        
        Args:
            dark: True for dark theme, False for light
        """
        self.theme_manager.set_theme("dark" if dark else "light")
        self.apply_theme()
    
    @pyqtSlot(int)
    def on_node_clicked(self, value: int):
        """
        Handle node click in canvas.
        
        Args:
            value: Clicked node value
        """
        self.info_panel.set_message(f"Clicked node: {value}")
    
    def apply_theme(self):
        """Apply current theme to the application."""
        stylesheet = self.theme_manager.get_stylesheet()
        self.setStyleSheet(stylesheet)
        self.canvas.set_dark_mode(self.theme_manager.is_dark_theme())
    
    def update_display(self):
        """Update all display elements."""
        # Redraw canvas
        self.canvas.redraw()
        
        # Update tree info
        size = self.tree.get_size()
        height = self.tree.get_height()
        is_balanced = self.tree.is_balanced()
        
        self.info_panel.update_tree_info(size, height, is_balanced)
        
        # Update undo/redo button states
        self.control_panel.enable_undo(self.history.can_undo())
        self.control_panel.enable_redo(self.history.can_redo())
    
    def _get_tree_state(self) -> List[int]:
        """
        Get the current state of the tree as a serializable list.
        
        Returns:
            List of node values in pre-order traversal
        """
        return self.tree.preorder_traversal()
    
    def _restore_tree_state(self, state: List[int]):
        """
        Restore the tree to a previous state.
        
        Args:
            state: List of node values to restore
        """
        self.tree.clear()
        for value in state:
            self.tree.insert(value)
    
    def closeEvent(self, event):
        """Handle application close event."""
        if not self.tree.is_empty():
            reply = QMessageBox.question(
                self,
                "Confirm Exit",
                "Are you sure you want to exit? Unsaved changes will be lost.",
                QMessageBox.Yes | QMessageBox.No
            )
            
            if reply == QMessageBox.No:
                event.ignore()
                return
        
        event.accept()
