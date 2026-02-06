"""Tree visualization canvas using PyQt5."""
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QSize
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QFont, QFontMetrics
from typing import Optional, List, Set
from src.models import Node, BinarySearchTree
from src.config import (
    NODE_RADIUS, NODE_COLOR_DEFAULT_LIGHT, NODE_COLOR_HIGHLIGHTED,
    NODE_COLOR_SEARCHING, NODE_BORDER_WIDTH, NODE_BORDER_COLOR,
    EDGE_COLOR_LIGHT, EDGE_COLOR_DARK, EDGE_WIDTH, ANIMATION_STEPS,
    VERTICAL_GAP, HORIZONTAL_GAP, TOP_MARGIN, NODE_LABEL_FONT_SIZE,
    CANVAS_BACKGROUND_LIGHT, CANVAS_BACKGROUND_DARK, TEXT_COLOR_LIGHT,
    TEXT_COLOR_DARK, ANIMATION_DURATION
)
from src.utils import AnimationEngine, TransitionAnimation


class TreeCanvas(QGraphicsView):
    """
    Custom graphics canvas for rendering the Binary Search Tree.
    Handles node positioning, drawing, and animations.
    """
    
    # Signals
    node_clicked = pyqtSignal(int)  # Emits node value
    animation_started = pyqtSignal()
    animation_finished = pyqtSignal()
    
    def __init__(self, parent=None):
        """Initialize the tree canvas."""
        super().__init__(parent)
        
        # Scene setup with responsive sizing
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setStyleSheet(f"QGraphicsView{{ border: 2px solid #bdc3c7; background: white; }}")
        
        # Make canvas responsive
        self.setMinimumSize(400, 300)
        self.setDragMode(QGraphicsView.ScrollHandDrag)  # Allow panning
        
        # Tree data
        self.tree: Optional[BinarySearchTree] = None
        self.dark_mode = False
        
        # Animation
        self.animation_engine = AnimationEngine()
        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self._update_animation)
        self.last_animation_time = 0
        
        # Rendering properties
        self.node_positions = {}  # Cache for node positions
        self.highlighted_nodes: Set[int] = set()
        self.searching_nodes: Set[int] = set()
        self.traversal_path: List[int] = []
        self.current_traversal_index = 0
        
        # Node animation states
        self.node_animations = {}
        
        # Step-by-step traversal
        self.step_mode = False
        self.step_timer = QTimer()
        self.step_timer.timeout.connect(self._next_traversal_step)
        self.step_timer.setInterval(400)  # Default step delay
        
        # Enable antialiasing and smooth rendering
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)
        
        # Mouse tracking for node interaction
        self.setMouseTracking(True)
        self.hovered_node = None
    
    def set_tree(self, tree: BinarySearchTree):
        """
        Set the tree to visualize.
        
        Args:
            tree: BinarySearchTree instance to visualize
        """
        self.tree = tree
        self.redraw()
    
    def set_dark_mode(self, dark: bool):
        """
        Set dark mode for the canvas.
        
        Args:
            dark: True for dark theme, False for light theme
        """
        self.dark_mode = dark
        bg_color = CANVAS_BACKGROUND_DARK if dark else CANVAS_BACKGROUND_LIGHT
        self.scene.setBackgroundBrush(QBrush(QColor(bg_color)))
        self.redraw()
    
    def redraw(self):
        """Clear and redraw the entire tree."""
        self.scene.clear()
        self.node_positions.clear()
        
        if self.tree is None or self.tree.is_empty():
            self._draw_empty_tree_message()
            return
        
        # Calculate node positions
        self._calculate_positions(self.tree.root, 0, 0)
        
        # Draw edges
        self._draw_edges(self.tree.root)
        
        # Draw nodes
        self._draw_nodes(self.tree.root)
        
        # Fit entire tree in view with padding
        if self.scene.itemsBoundingRect().isValid():
            self.fitInView(self.scene.itemsBoundingRect(), Qt.KeepAspectRatio)
            # Add padding by scaling down slightly
            self.scale(0.85, 0.85)
    
    def _calculate_positions(self, node: Optional[Node], x: float, y: float, offset: float = 100):
        """
        Calculate positions for nodes in the tree (recursive).
        Uses a space-filling algorithm to prevent overlap.
        
        Args:
            node: Current node
            x: X position for this node
            y: Y position for this node
            offset: Horizontal spacing offset
        """
        if node is None:
            return
        
        # Store position
        self.node_positions[id(node)] = (x, y)
        node.x, node.y = x, y
        
        # Calculate offset for subtrees
        next_y = y + VERTICAL_GAP
        next_offset = offset / 2
        
        if node.left:
            left_x = x - offset
            self._calculate_positions(node.left, left_x, next_y, next_offset)
        
        if node.right:
            right_x = x + offset
            self._calculate_positions(node.right, right_x, next_y, next_offset)
    
    def _draw_edges(self, node: Optional[Node]):
        """
        Draw edges connecting nodes (recursive).
        
        Args:
            node: Current node
        """
        if node is None:
            return
        
        edge_color = EDGE_COLOR_DARK if self.dark_mode else EDGE_COLOR_LIGHT
        pen = QPen(QColor(edge_color), EDGE_WIDTH)
        
        node_x, node_y = node.x, node.y
        
        if node.left:
            left_x, left_y = node.left.x, node.left.y
            self.scene.addLine(node_x, node_y, left_x, left_y, pen)
            self._draw_edges(node.left)
        
        if node.right:
            right_x, right_y = node.right.x, node.right.y
            self.scene.addLine(node_x, node_y, right_x, right_y, pen)
            self._draw_edges(node.right)
    
    def _draw_nodes(self, node: Optional[Node]):
        """
        Draw node circles and labels (recursive).
        
        Args:
            node: Current node
        """
        if node is None:
            return
        
        # Determine node color
        if node.value in self.highlighted_nodes:
            color = NODE_COLOR_HIGHLIGHTED
        elif node.value in self.searching_nodes:
            color = NODE_COLOR_SEARCHING
        else:
            color = NODE_COLOR_DEFAULT_LIGHT
        
        # Draw circle
        brush = QBrush(QColor(color))
        pen = QPen(QColor(NODE_BORDER_COLOR), NODE_BORDER_WIDTH)
        self.scene.addEllipse(
            node.x - NODE_RADIUS,
            node.y - NODE_RADIUS,
            NODE_RADIUS * 2,
            NODE_RADIUS * 2,
            pen,
            brush
        )
        
        # Draw label
        text_color = TEXT_COLOR_DARK if self.dark_mode else TEXT_COLOR_LIGHT
        font = QFont("Segoe UI", NODE_LABEL_FONT_SIZE, QFont.Bold)
        text_item = self.scene.addText(str(node.value), font)
        text_item.setDefaultTextColor(QColor(text_color))
        
        # Center text on node
        text_rect = text_item.boundingRect()
        text_item.setPos(
            node.x - text_rect.width() / 2,
            node.y - text_rect.height() / 2
        )
        
        # Recursively draw child nodes
        self._draw_nodes(node.left)
        self._draw_nodes(node.right)
    
    def _draw_empty_tree_message(self):
        """Draw a message when the tree is empty."""
        text_color = TEXT_COLOR_DARK if self.dark_mode else TEXT_COLOR_LIGHT
        font = QFont("Segoe UI", 14)
        text_item = self.scene.addText("Tree is empty. Insert nodes to start!", font)
        text_item.setDefaultTextColor(QColor(text_color))
        
        # Center the message
        rect = self.scene.itemsBoundingRect()
        text_item.setPos(
            rect.x() + rect.width() / 2 - 150,
            rect.y() + rect.height() / 2 - 20
        )
    
    def highlight_node(self, value: int, duration: int = 500):
        """
        Highlight a node temporarily.
        
        Args:
            value: Value of node to highlight
            duration: Duration of highlight in milliseconds
        """
        self.highlighted_nodes.add(value)
        self.redraw()
        
        # Auto-unhighlight after duration
        QTimer.singleShot(duration, lambda: self._unhighlight_node(value))
    
    def _unhighlight_node(self, value: int):
        """Remove highlight from a node."""
        self.highlighted_nodes.discard(value)
        self.redraw()
    
    def show_search_path(self, path: List[int]):
        """
        Show the path taken during a search.
        
        Args:
            path: List of node values in search path
        """
        self.searching_nodes = set(path)
        self.redraw()
    
    def clear_search_path(self):
        """Clear the search path highlighting."""
        self.searching_nodes.clear()
        self.highlighted_nodes.clear()
        self.redraw()
    
    def animate_traversal(self, traversal_path: List[int], step_delay: int = 400):
        """
        Animate a tree traversal, highlighting nodes in sequence.
        
        Args:
            traversal_path: List of node values in traversal order
            step_delay: Delay between steps in milliseconds
        """
        self.traversal_path = traversal_path
        self.current_traversal_index = 0
        self.step_mode = True
        self.step_timer.setInterval(step_delay)
        self.animation_started.emit()
        self._next_traversal_step()
    
    def _next_traversal_step(self):
        """Move to next step in traversal animation."""
        if self.current_traversal_index < len(self.traversal_path):
            value = self.traversal_path[self.current_traversal_index]
            self.highlight_node(value, self.step_timer.interval())
            self.current_traversal_index += 1
            self.step_timer.start()
        else:
            self.step_timer.stop()
            self.step_mode = False
            self.animation_finished.emit()
    
    def stop_animation(self):
        """Stop current animation."""
        self.step_timer.stop()
        self.animation_timer.stop()
        self.animation_engine.stop_all()
        self.step_mode = False
        self.clear_search_path()
    
    def _update_animation(self):
        """Update animations (called by timer)."""
        self.animation_engine.update(16)  # ~60 FPS
        
        if not self.animation_engine.has_active_animations():
            self.animation_timer.stop()
            self.animation_finished.emit()
    
    def mouseMoveEvent(self, event):
        """Handle mouse move events."""
        super().mouseMoveEvent(event)
        # Could be used for node hover effects
        pos = self.mapToScene(event.pos())
        
        # Check if hovering over a node
        items = self.scene.items(pos)
        for item in items:
            if hasattr(item, 'rect'):  # It's an ellipse (node)
                pass  # Could highlight here
    
    def mousePressEvent(self, event):
        """Handle mouse click events on nodes."""
        super().mousePressEvent(event)
        pos = self.mapToScene(event.pos())
        
        # Check if clicked on a node
        items = self.scene.items(pos)
        for item in items:
            if hasattr(item, 'rect'):
                # Try to find the node value
                if self.tree:
                    for node in self.tree.get_all_nodes():
                        distance = ((node.x - pos.x())**2 + (node.y - pos.y())**2)**0.5
                        if distance <= NODE_RADIUS:
                            self.node_clicked.emit(node.value)
                            return
