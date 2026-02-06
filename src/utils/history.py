"""Undo/Redo history management for BST operations."""
from typing import List, Any, Callable
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class Operation:
    """Represents a single operation that can be undone/redone."""
    name: str
    undo_action: Callable
    redo_action: Callable
    data: Any = None


class OperationHistory:
    """
    Manages undo/redo functionality for BST operations.
    Uses a command pattern to store and replay operations.
    """
    
    def __init__(self, max_size: int = 50):
        """
        Initialize the operation history.
        
        Args:
            max_size: Maximum number of operations to keep in history
        """
        self.max_size = max_size
        self.undo_stack: List[Operation] = []
        self.redo_stack: List[Operation] = []
    
    def record_operation(self, operation: Operation):
        """
        Record a new operation.
        Clears the redo stack when a new operation is performed.
        
        Args:
            operation: Operation to record
        """
        self.undo_stack.append(operation)
        self.redo_stack.clear()
        
        # Maintain max history size
        if len(self.undo_stack) > self.max_size:
            self.undo_stack.pop(0)
    
    def undo(self) -> bool:
        """
        Undo the last operation.
        
        Returns:
            True if undo was successful, False if nothing to undo
        """
        if not self.undo_stack:
            return False
        
        operation = self.undo_stack.pop()
        operation.undo_action()
        
        # Create a reverse operation for redo
        redo_op = Operation(
            name=operation.name,
            undo_action=operation.redo_action,
            redo_action=operation.undo_action,
            data=operation.data
        )
        self.redo_stack.append(redo_op)
        return True
    
    def redo(self) -> bool:
        """
        Redo the last undone operation.
        
        Returns:
            True if redo was successful, False if nothing to redo
        """
        if not self.redo_stack:
            return False
        
        operation = self.redo_stack.pop()
        operation.redo_action()
        self.undo_stack.append(operation)
        return True
    
    def can_undo(self) -> bool:
        """Return True if there are operations to undo."""
        return len(self.undo_stack) > 0
    
    def can_redo(self) -> bool:
        """Return True if there are operations to redo."""
        return len(self.redo_stack) > 0
    
    def get_undo_description(self) -> str:
        """Get description of the operation that would be undone."""
        if self.undo_stack:
            return f"Undo {self.undo_stack[-1].name}"
        return "Nothing to undo"
    
    def get_redo_description(self) -> str:
        """Get description of the operation that would be redone."""
        if self.redo_stack:
            return f"Redo {self.redo_stack[-1].name}"
        return "Nothing to redo"
    
    def clear(self):
        """Clear all history."""
        self.undo_stack.clear()
        self.redo_stack.clear()
    
    def get_history_size(self) -> tuple:
        """Get current history size (undo_count, redo_count)."""
        return len(self.undo_stack), len(self.redo_stack)
