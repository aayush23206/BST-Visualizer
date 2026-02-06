"""
ARCHITECTURE DOCUMENTATION

This file explains the architectural design of the BST Visualizer.

## Design Pattern: Model-View-Controller (MVC)

The application follows MVC principles with clear separation:

MODEL (Data Layer):
  - src/models/node.py: Node class representing tree nodes
  - src/models/bst.py: BinarySearchTree class with all algorithms

VIEW (Presentation Layer):
  - src/ui/widgets/tree_canvas.py: Visualization rendering
  - src/ui/widgets/control_panel.py: User controls
  - src/ui/widgets/info_panel.py: Information display
  - src/ui/styles.py: Theme management

CONTROLLER (Logic Layer):
  - src/ui/main_window.py: Coordinates between model and view
  - src/utils/*: Utility services (history, animations, export)

## Signal-Slot Architecture

PyQt5's signal/slot mechanism handles all communication:

1. User Action (signal) → Button click event
2. Signal Emission → widget emits custom signal
3. Slot Connection → MainWindow slot method called
4. Model Update → Tree structure modified
5. View Update → Canvas redrawn

Example Flow:
  ControlPanel.insert_requested.emit(50)
    ↓
  MainWindow.on_insert(50)
    ↓
  BinarySearchTree.insert(50)
    ↓
  TreeCanvas.redraw()

## Component Responsibilities

### Node Class
- Stores value and child references
- Tracks visual properties (x, y, radius)
- Provides convenience methods (is_leaf, has_one_child)

### BinarySearchTree Class
- Maintains tree structure and invariants
- Implements all operations (insert, delete, search)
- Provides traversal methods
- Calculates properties (height, size, balanced)

### TreeCanvas Class
- Renders nodes and edges to screen
- Manages node positions using recursive layout algorithm
- Handles animations and highlights
- Responds to user interactions

### ControlPanel Class
- Provides input fields and buttons
- Emits signals for user actions
- Displays operation results and messages

### InfoPanel Class
- Shows tree statistics
- Displays current operation
- Provides user feedback messages

### MainWindow Class
- Orchestrates all components
- Maintains application state
- Handles operation history
- Coordinates model-view interactions

## Data Flow

Operation Insertion Flow:
  
  1. User enters value and clicks Insert
  2. ControlPanel.insert_requested signal emitted
  3. MainWindow.on_insert() slot handles signal
  4. Creates Operation object with undo/redo functions
  5. BinarySearchTree.insert() updates data
  6. Operation saved to history
  7. TreeCanvas.redraw() called
  8. InfoPanel.update_tree_info() updates statistics
  9. UI reflects new tree state

## History System (Undo/Redo)

Command Pattern Implementation:

- Each operation is a Command object with:
  - name: Description of operation
  - undo_action: Function to reverse operation
  - redo_action: Function to repeat operation
  - data: Optional associated data

- Two stacks maintain history:
  - undo_stack: Operations that can be undone
  - redo_stack: Operations that can be redone

- Using tree serialization for state management:
  - Tree state captured as list of values
  - Can be restored by clearing and reinserting

Example:
  Operation(
    name="Insert 50",
    undo_action=lambda: restore_state([30, 70, 20]),
    redo_action=lambda: restore_state([50, 30, 70, 20])
  )

## Animation System

Physics-based animation engine:

- AnimationEngine manages active animations
- Animation class handles single animation lifecycle
- Easing functions for smooth motion:
  - LINEAR: Constant speed
  - EASE_IN: Slow start, fast finish
  - EASE_OUT: Fast start, slow finish
  - EASE_IN_OUT: Slow start and finish

Flow:
  1. Animation created with duration and update callback
  2. Timer triggers update at ~60fps
  3. Progress calculated (0.0 to 1.0)
  4. Easing function applied for smoothness
  5. Update callback notified with progress
  6. Animation completes and timer stops

## Configuration System

Centralized configuration in config.py:

- Window dimensions and styling
- Colors for light/dark themes
- Node and edge rendering properties
- Animation timings
- Traversal delays
- History size limits

Benefits:
- Easy to customize appearance
- Consistent values across codebase
- Single point of theme management

## Extension Points

Easy to add new features:

1. New Traversal: Add method to BinarySearchTree
2. New Operation: Create Operation with undo/redo, call MainWindow.history.record
3. New Visualization: Subclass TreeCanvas or modify rendering
4. New Theme: Add colors to config.py and style definitions
5. New Animation: Use AnimationEngine with custom easing

## Performance Considerations

Optimizations implemented:

1. Node position caching to avoid recalculation
2. Scene optimization in PyQt5 (viewport culling)
3. Efficient tree traversal algorithms
4. Limited history size (50 operations max)
5. Lazy evaluation of properties (height, balance)

Complexity Analysis:
- Insert/Delete/Search: O(h) where h is height
- Traversals: O(n)
- Tree layout: O(n)
- Redraw: O(n)

## Testing Strategy

Key areas to test:

1. Model Layer: BST operations correctness
2. View Layer: Rendering accuracy
3. Controller Layer: Event handling and flow
4. Integration: Component communication
5. User Acceptance: Full workflow testing

Test data suggestions:
- Empty tree operations
- Single node edge cases
- Balanced and unbalanced trees
- Maximum size handling
- Extreme values (MIN/MAX)

## Code Structure Best Practices

Implemented in this project:

✓ Single Responsibility: Each class has one purpose
✓ Open/Closed: Easy to extend, closed to modification
✓ Liskov Substitution: Proper inheritance use
✓ Interface Segregation: Focused interfaces
✓ Dependency Inversion: High-level modules independent

✓ DRY: No code duplication
✓ KISS: Simple, understandable code
✓ YAGNI: No unnecessary features
✓ Comment Clarity: Clear explanations of "why"

## Summary

The architecture provides:
- Clear separation of concerns
- Easy maintenance and debugging
- Simple testing of components
- Straightforward addition of features
- Professional code organization
- Resume-worthy design patterns

This design demonstrates understanding of:
- Software architecture principles
- Design patterns (MVC, Command, Observer)
- Clean code practices
- Professional software development
"""
