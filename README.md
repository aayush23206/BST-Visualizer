# BST Visualizer - Professional Desktop Application

A professional-grade **Binary Search Tree (BST) visualizer** built with Python and PyQt5. This desktop application provides real-time visualization of BST operations with an interactive GUI, perfect for learning, teaching, and showcasing on a resume.

## Features

### Core BST Operations
- **Insert** nodes with automatic tree balancing visualization
- **Delete** nodes (handles all 3 cases: leaf, one child, two children)
- **Search** with visual path highlighting
- **Tree Traversals**:
  - Inorder (Left-Root-Right)
  - Preorder (Root-Left-Right)
  - Postorder (Left-Right-Root)
  - Level-order (BFS)

### Visualization
- **Real-time animated rendering** of tree structure
- **Node highlighting** during operations
- **Step-by-step traversal animation** with adjustable speed
- **Professional canvas rendering** with PyQt5 Graphics
- **Automatic tree layout** with intelligent node positioning

### User Interface
- **Intuitive control panel** with dedicated sections for each operation
- **Live tree statistics** (node count, height, balance status)
- **Dark/Light theme toggle** for comfortable viewing
- **Operation tracking** with last operation display
- **Responsive layout** that adapts to window size

### Advanced Features
- **Undo/Redo functionality** for all operations
- **Random tree generation** with configurable size
- **Traversal output display** showing complete sequences
- **Tree state information**:
  - Total node count
  - Tree height
  - Balance status
- **Clean, professional styling** with themed colors

## Project Architecture

### Clean Separation of Concerns
```
BST Visualizer/
├── src/
│   ├── models/              # Pure data structure logic
│   │   ├── node.py         # Node class with properties
│   │   └── bst.py          # BinarySearchTree implementation
│   ├── ui/                  # User interface layer
│   │   ├── main_window.py   # Main application window
│   │   ├── styles.py        # Theme management
│   │   └── widgets/         # Reusable UI components
│   │       ├── tree_canvas.py    # Visualization engine
│   │       ├── control_panel.py  # Control interface
│   │       └── info_panel.py     # Statistics display
│   ├── utils/               # Utility modules
│   │   ├── history.py       # Undo/Redo system
│   │   ├── animations.py    # Animation engine
│   │   └── export.py        # Image export (extensible)
│   ├── config.py            # Centralized constants
│   └── main.py              # Entry point
├── requirements.txt         # Project dependencies
└── README.md               # Documentation
```

### Design Principles
1. **Object-Oriented Programming**: Proper use of classes and inheritance
2. **Separation of Concerns**: Data logic separate from UI
3. **Modularity**: Reusable, independently testable components
4. **Signal/Slot Architecture**: PyQt5 event-driven design
5. **Configuration Management**: Centralized constants for easy customization
6. **Clean Code**: Well-documented, readable, maintainable

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone or download the project:**
   ```bash
   cd "BST Visualizer2.0"
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python -m src.main
   ```

   Or on Windows:
   ```bash
   python src\main.py
   ```

## Usage Guide

### Basic Operations

#### Insert a Node
1. Enter a value (integer) in the "Insert Node" field
2. Click "Insert" or press Enter
3. The node will appear in the tree and be briefly highlighted

#### Delete a Node
1. Enter the value of the node to delete in the "Delete Node" field
2. Click "Delete"
3. The tree will automatically re-arrange

#### Search for a Node
1. Enter the value to search in the "Search Node" field
2. Click "Search"
3. Found nodes will be highlighted; a message shows the result

#### Traverse the Tree
1. Select a traversal type from the dropdown (Inorder, Preorder, etc.)
2. Optional: Check "Animate Steps" for step-by-step visualization
3. Click "Execute Traversal"
4. Result appears in the "Traversal Output" section

#### Generate Random Tree
1. Set the number of nodes using the spinner
2. Click "Generate Random Tree"
3. A random BST will be created with non-duplicate values

### Advanced Operations

#### Undo/Redo
- Use the "↶ Undo" and "↷ Redo" buttons to navigate operation history
- History supports up to 50 operations

#### Clear Tree
- Click "Clear Tree" button to remove all nodes
- A confirmation dialog will appear

#### Dark Mode
- Toggle "Dark Mode" checkbox in Settings
- Smoothly switches between light and dark themes

### Keyboard Shortcuts
- Insert input: Press **Enter** to insert
- Delete input: Press **Enter** to delete
- Search input: Press **Enter** to search

## Code Quality Features

### 1. Comprehensive Documentation
- Module-level docstrings explaining purpose
- Class docstrings with attributes and behavior
- Method docstrings with parameters and return values
- Inline comments for complex algorithms

### 2. Type Hints
- Function parameters annotated with types
- Return types specified
- Better IDE support and error detection

### 3. Clean Architecture
- No circular dependencies
- Clear interfaces between components
- Easy to extend with new features

### 4. Error Handling
- Input validation for all user inputs
- Graceful error messages
- Confirmation dialogs for destructive operations

### 5. Maintainability
- Consistent naming conventions
- Single responsibility principle
- DRY (Don't Repeat Yourself) principles

## Extensibility

The architecture makes it easy to add new features:

### Add New Traversal Type
```python
# In BinarySearchTree class
def my_traversal(self) -> List[int]:
    """Implement new traversal algorithm"""
    result = []
    # ... implementation ...
    return result

# In main_window.py on_traversal method
elif traversal_type == "my_traversal":
    result = self.tree.my_traversal()
```

### Add New Operation
```python
# Create the operation
original_state = self._get_tree_state()

# ... perform operation ...

# Record for undo/redo
operation = Operation(
    name="My Operation",
    undo_action=undo_func,
    redo_action=redo_func
)
self.history.record_operation(operation)
```

### Add New Visualization Style
Edit `src.config.py` to customize:
- Colors (NODE_COLOR_*, EDGE_COLOR_*)
- Sizes (NODE_RADIUS, NODE_LABEL_FONT_SIZE)
- Spacing (VERTICAL_GAP, HORIZONTAL_GAP)
- Animation timing (ANIMATION_DURATION, TRAVERSAL_STEP_DELAY)

## Algorithm Complexity

### BST Operations
| Operation | Best Case | Average | Worst Case |
|-----------|-----------|---------|-----------|
| Insert    | O(log n)  | O(log n)| O(n)      |
| Delete    | O(log n)  | O(log n)| O(n)      |
| Search    | O(log n)  | O(log n)| O(n)      |
| Traversals| O(n)      | O(n)    | O(n)      |

### Space Complexity
- **Tree Storage**: O(n)
- **History Buffer**: O(h) where h is number of operations

## Performance Optimizations

1. **Node Position Caching**: Positions calculated once per redraw
2. **Efficient Scene Management**: PyQt5 scene optimization
3. **Animation Engine**: Batched updates for smooth rendering
4. **Lazy Evaluation**: Height and balance checked only when needed

## Testing the Application

### Test Cases

1. **Insert Operations**
   - Insert single node
   - Insert multiple nodes
   - Insert duplicate (should fail)
   - Insert at max value

2. **Delete Operations**
   - Delete leaf node
   - Delete node with one child
   - Delete node with two children
   - Delete root node
   - Delete non-existent node

3. **Search Operations**
   - Search existing node
   - Search non-existent node

4. **Traversals**
   - All four traversal types
   - With and without animation

5. **Tree Generation**
   - Generate random trees of various sizes
   - Verify no duplicates

6. **Undo/Redo**
   - Undo single operation
   - Redo operation
   - Multiple undo/redo sequences

7. **Theme**
   - Toggle dark/light mode
   - Verify colors apply correctly

## Resume Highlights

This project demonstrates:

✓ **Strong OOP Design**: Clean class hierarchy and object composition
✓ **GUI Development**: Professional PyQt5 application with signals/slots
✓ **Data Structures**: Complete BST implementation with all operations
✓ **Algorithm Knowledge**: Multiple traversal algorithms and deletion handling
✓ **User Experience**: Intuitive, responsive interface with real-time feedback
✓ **Code Organization**: Modular architecture suitable for large projects
✓ **Documentation**: Comprehensive comments and docstrings
✓ **Problem Solving**: Complex visualization and animation algorithms
✓ **Best Practices**: Clean code principles, design patterns, error handling

## Future Enhancement Ideas

- AVL Tree balancing with auto-rebalancing visualization
- Red-Black Tree implementation
- B-Tree visualization
- Performance benchmarking tools
- Comparison mode for different tree types
- Tree persistence (save/load)
- Animation speed control slider
- Advanced layout algorithms (Reingold-Tilford)

## License

This project is free to use for educational and portfolio purposes.

## Author Notes

This BST Visualizer demonstrates professional-level Python development with:
- Production-quality code organization
- Comprehensive feature set
- Intuitive user interface
- Extensible architecture

Perfect for:
- Portfolio projects
- Technical interviews
- Learning data structures
- Teaching algorithms

---

**Version**: 2.0  
**Last Updated**: February 2026  
**Status**: Production Ready
