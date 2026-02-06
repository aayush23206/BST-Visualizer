"""Binary Search Tree implementation."""
from typing import Optional, List
from collections import deque
from .node import Node


class BinarySearchTree:
    """
    A Binary Search Tree implementation with support for standard operations:
    - Insert
    - Delete (with handling for leaf, one child, and two children cases)
    - Search
    - Traversals (Inorder, Preorder, Postorder, Level-order/BFS)
    
    Properties:
    - Maintains BST property: left.value < parent.value < right.value
    - Automatically updates node positions for visualization
    """
    
    def __init__(self):
        """Initialize an empty BST."""
        self.root = None
        self._size = 0
        self._height_cache = -1
    
    def insert(self, value: int) -> bool:
        """
        Insert a value into the BST.
        
        Args:
            value: Integer value to insert
            
        Returns:
            True if insertion was successful, False if value already exists
        """
        if self.root is None:
            self.root = Node(value)
            self._size = 1
            self._height_cache = -1
            return True
        
        return self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node: Node, value: int) -> bool:
        """
        Recursively insert a value into the BST.
        
        Args:
            node: Current node in the recursion
            value: Value to insert
            
        Returns:
            True if insertion was successful, False if value already exists
        """
        if value < node.value:
            if node.left is None:
                node.left = Node(value, parent=node)
                self._size += 1
                self._height_cache = -1
                return True
            return self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value, parent=node)
                self._size += 1
                self._height_cache = -1
                return True
            return self._insert_recursive(node.right, value)
        else:
            # Value already exists
            return False
    
    def search(self, value: int) -> Optional[Node]:
        """
        Search for a node with the given value.
        
        Args:
            value: Value to search for
            
        Returns:
            Node if found, None otherwise
        """
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node: Optional[Node], value: int) -> Optional[Node]:
        """
        Recursively search for a value in the BST.
        
        Args:
            node: Current node in the recursion
            value: Value to search for
            
        Returns:
            Node if found, None otherwise
        """
        if node is None:
            return None
        
        if value == node.value:
            return node
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def delete(self, value: int) -> bool:
        """
        Delete a node with the given value from the BST.
        Handles three cases:
        1. Leaf node: Simply remove it
        2. One child: Replace node with its child
        3. Two children: Replace node with in-order successor (smallest in right subtree)
        
        Args:
            value: Value to delete
            
        Returns:
            True if deletion was successful, False if value not found
        """
        if self.root is None:
            return False
        
        self.root, deleted = self._delete_recursive(self.root, value)
        if deleted:
            self._size -= 1
            self._height_cache = -1
        return deleted
    
    def _delete_recursive(self, node: Optional[Node], value: int) -> tuple:
        """
        Recursively delete a value from the BST.
        
        Args:
            node: Current node in the recursion
            value: Value to delete
            
        Returns:
            Tuple of (updated_node, was_deleted)
        """
        if node is None:
            return None, False
        
        if value < node.value:
            node.left, deleted = self._delete_recursive(node.left, value)
            if node.left:
                node.left.parent = node
            return node, deleted
        elif value > node.value:
            node.right, deleted = self._delete_recursive(node.right, value)
            if node.right:
                node.right.parent = node
            return node, deleted
        else:
            # Found the node to delete
            
            # Case 1: Leaf node
            if node.is_leaf():
                return None, True
            
            # Case 2: Only right child
            if node.left is None:
                node.right.parent = node.parent
                return node.right, True
            
            # Case 3: Only left child
            if node.right is None:
                node.left.parent = node.parent
                return node.left, True
            
            # Case 4: Two children - find in-order successor
            # In-order successor is the leftmost node in the right subtree
            successor = self._find_min_node(node.right)
            node.value = successor.value
            node.right, _ = self._delete_recursive(node.right, successor.value)
            if node.right:
                node.right.parent = node
            return node, True
    
    def _find_min_node(self, node: Optional[Node]) -> Optional[Node]:
        """
        Find the node with minimum value in a subtree.
        
        Args:
            node: Root of the subtree
            
        Returns:
            Node with minimum value
        """
        if node is None:
            return None
        while node.left:
            node = node.left
        return node
    
    def inorder_traversal(self) -> List[int]:
        """
        Perform in-order traversal (Left, Root, Right).
        Returns elements in sorted order.
        
        Returns:
            List of values in in-order sequence
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node: Optional[Node], result: List[int]):
        """Recursive helper for in-order traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self) -> List[int]:
        """
        Perform pre-order traversal (Root, Left, Right).
        Useful for copying the tree.
        
        Returns:
            List of values in pre-order sequence
        """
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node: Optional[Node], result: List[int]):
        """Recursive helper for pre-order traversal."""
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self) -> List[int]:
        """
        Perform post-order traversal (Left, Right, Root).
        Useful for deletion.
        
        Returns:
            List of values in post-order sequence
        """
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node: Optional[Node], result: List[int]):
        """Recursive helper for post-order traversal."""
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)
    
    def levelorder_traversal(self) -> List[int]:
        """
        Perform level-order traversal (BFS).
        Returns elements level by level from top to bottom.
        
        Returns:
            List of values in level-order sequence
        """
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            result.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def get_height(self) -> int:
        """
        Calculate the height of the tree.
        Height is defined as the number of edges in the longest path from root to leaf.
        
        Returns:
            Height of the tree (-1 for empty tree, 0 for single node)
        """
        return self._calculate_height(self.root)
    
    def _calculate_height(self, node: Optional[Node]) -> int:
        """
        Recursively calculate the height of a subtree.
        
        Args:
            node: Root of the subtree
            
        Returns:
            Height of the subtree
        """
        if node is None:
            return -1
        return 1 + max(self._calculate_height(node.left), 
                       self._calculate_height(node.right))
    
    def get_size(self) -> int:
        """
        Get the number of nodes in the tree.
        
        Returns:
            Total number of nodes
        """
        return self._size
    
    def is_balanced(self) -> bool:
        """
        Check if the tree is balanced.
        A balanced tree has |height(left) - height(right)| <= 1 for all nodes.
        
        Returns:
            True if the tree is balanced, False otherwise
        """
        def check_balance(node: Optional[Node]) -> tuple:
            """
            Check if subtree is balanced and return (is_balanced, height).
            """
            if node is None:
                return True, -1
            
            left_balanced, left_height = check_balance(node.left)
            if not left_balanced:
                return False, 0
            
            right_balanced, right_height = check_balance(node.right)
            if not right_balanced:
                return False, 0
            
            is_current_balanced = abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)
            
            return is_current_balanced, height
        
        balanced, _ = check_balance(self.root)
        return balanced
    
    def clear(self):
        """Clear the entire tree."""
        self.root = None
        self._size = 0
        self._height_cache = -1
    
    def is_empty(self) -> bool:
        """Return True if the tree is empty."""
        return self.root is None
    
    def get_all_nodes(self) -> List[Node]:
        """Get all nodes in the tree using level-order traversal."""
        if not self.root:
            return []
        
        nodes = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            nodes.append(node)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return nodes
