"""Node class for Binary Search Tree."""


class Node:
    """
    Represents a single node in the Binary Search Tree.
    
    Attributes:
        value: The integer value stored in this node
        left: Reference to the left child node
        right: Reference to the right child node
        parent: Reference to the parent node (useful for visualization)
        x, y: Visual coordinates for rendering (set by visualization engine)
    """
    
    def __init__(self, value: int, parent=None):
        """
        Initialize a node with the given value.
        
        Args:
            value: Integer value to store in the node
            parent: Parent node reference (optional)
        """
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        
        # Visual properties for rendering
        self.x = 0
        self.y = 0
        self.radius = 25
        
        # State flags for visualization
        self.is_highlighted = False
        self.is_searching = False
        self.animation_progress = 0.0
    
    def __repr__(self) -> str:
        """Return string representation of the node."""
        return f"Node({self.value})"
    
    def __eq__(self, other) -> bool:
        """Compare nodes by their values."""
        if isinstance(other, Node):
            return self.value == other.value
        return self.value == other
    
    def __lt__(self, other) -> bool:
        """Compare nodes for less than operation."""
        if isinstance(other, Node):
            return self.value < other.value
        return self.value < other
    
    def is_leaf(self) -> bool:
        """Return True if this node is a leaf node."""
        return self.left is None and self.right is None
    
    def has_one_child(self) -> bool:
        """Return True if this node has exactly one child."""
        return (self.left is None) != (self.right is None)
    
    def get_child_count(self) -> int:
        """Return the number of children this node has."""
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count
