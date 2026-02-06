"""
PROJECT STRUCTURE DOCUMENTATION

BST Visualizer2.0/
│
├── src/                           # Main source code package
│   ├── __init__.py               # Package initialization
│   ├── main.py                   # Application entry point
│   ├── config.py                 # Configuration and constants
│   │
│   ├── models/                   # Data structure implementations
│   │   ├── __init__.py
│   │   ├── node.py              # Node class definition
│   │   └── bst.py               # BinarySearchTree class with all operations
│   │
│   ├── ui/                        # User interface layer
│   │   ├── __init__.py
│   │   ├── main_window.py        # Main application window
│   │   ├── styles.py             # Theme and styling system
│   │   │
│   │   └── widgets/              # Reusable UI components
│   │       ├── __init__.py
│   │       ├── tree_canvas.py    # Canvas for tree visualization
│   │       ├── control_panel.py  # Control buttons and inputs
│   │       └── info_panel.py     # Tree statistics display
│   │
│   └── utils/                     # Utility and service modules
│       ├── __init__.py
│       ├── history.py            # Undo/Redo system
│       ├── animations.py         # Animation engine
│       └── export.py             # Image export functionality
│
├── tests.py                      # Unit tests (16 test cases)
├── run.py                        # Simple launcher script
├── requirements.txt              # Python dependencies
│
├── README.md                     # Comprehensive documentation
├── QUICKSTART.txt               # Quick start guide
├── ARCHITECTURE.md              # Architecture documentation
├── ALGORITHMS.md                # Algorithm explanations
└── PROJECT_STRUCTURE.md         # This file


## FILE DESCRIPTIONS

### Source Code Files

#### models/node.py
- Node class: Represents a single BST node
  - Properties: value, left, right, parent
  - Visual properties: x, y, radius
  - Methods: is_leaf(), has_one_child(), get_child_count()

#### models/bst.py
- BinarySearchTree class: Complete BST implementation
  - Operations: insert(), delete(), search()
  - Traversals: inorder(), preorder(), postorder(), levelorder()
  - Properties: get_height(), get_size(), is_balanced()
  - Utilities: clear(), is_empty(), get_all_nodes()

#### ui/main_window.py
- MainWindow class: Orchestrates all UI components
  - Event handlers for all operations
  - History management for undo/redo
  - Theme coordination
  - Tree state management

#### ui/widgets/tree_canvas.py
- TreeCanvas class: Graphics rendering engine
  - Tree visualization with automatic layout
  - Node positioning algorithm
  - Animation support for traversals
  - User interaction handling

#### ui/widgets/control_panel.py
- ControlPanel class: User input interface
  - Insert/Delete/Search inputs
  - Traversal selector
  - Random tree generator
  - Undo/Redo buttons
  - Theme toggle

#### ui/widgets/info_panel.py
- InfoPanel class: Information display
  - Tree statistics (size, height, balance)
  - Last operation display
  - Status messages

#### ui/styles.py
- ThemeManager class: Theme management
  - Light/Dark theme support
  - Color configuration
  - StyleSheet generation

#### utils/history.py
- OperationHistory class: Undo/Redo management
  - Command pattern implementation
  - Stack-based history
  - Configurable history size

#### utils/animations.py
- AnimationEngine class: Animation management
- Animation class: Single animation lifecycle
- TransitionAnimation: Helper for position animations
- AnimationType enum: Easing function types

#### utils/export.py
- TreeExporter class: Image export functionality
- PNG/JPG/GIF export support
- Configurable scale and quality

#### config.py
- Centralized constants
- Color definitions
- Animation timings
- Layout parameters
- Validation ranges


## LOC (Lines of Code) Summary

models/         ~350 lines   - Pure data structure logic
ui/             ~600 lines   - User interface components
utils/          ~400 lines   - Utility services
config.py       ~150 lines   - Configuration constants
Total Core:    ~1500 lines

tests.py        ~300 lines   - Comprehensive unit tests
Documentation: ~1500 lines   - README, Architecture, Algorithms


## Dependencies

- PyQt5 >= 5.15.0     - GUI framework
- Python >= 3.7       - Programming language

No other external dependencies required!


## Key Features Implementation

✓ Object-Oriented Design
  - Class hierarchy with proper inheritance
  - Clear interfaces and responsibilities
  - Encapsulation of data and behavior

✓ Data Structures
  - Complete BST implementation
  - All standard operations
  - Multiple traversal algorithms

✓ GUI Components
  - Custom graphics rendering
  - Responsive layout
  - Professional styling

✓ User Experience
  - Real-time visualization
  - Smooth animations
  - Intuitive controls
  - Dark/Light theme support

✓ Code Quality
  - Comprehensive documentation
  - Type hints throughout
  - Error handling
  - Modular architecture

✓ Testing
  - 16 unit tests
  - Edge case coverage
  - Algorithm verification

✓ Professional Features
  - Undo/Redo functionality
  - Random tree generation
  - Tree state information
  - Output display


## Design Patterns Used

1. Model-View-Controller (MVC)
   - Clear separation of concerns
   - Models handle logic
   - Views handle presentation
   - Controllers coordinate

2. Command Pattern
   - OperationHistory using command objects
   - Undo/Redo implementation

3. Observer Pattern (Signal/Slot)
   - PyQt5 signals and slots
   - Loose coupling between components

4. Factory Pattern
   - Animation creation
   - Theme creation

5. Singleton Pattern
   - ThemeManager instance
   - AnimationEngine instance


## Extensibility Examples

### Add New Tree Operation
1. Implement algorithm in BinarySearchTree
2. Create handler in MainWindow.on_operation()
3. Add button to ControlPanel
4. Connect signal to handler

### Add New Theme
1. Add color definitions to config.py
2. Add theme to ThemeManager
3. Add stylesheet method in styles.py
4. Update UI

### Add New Visualization
1. Subclass TreeCanvas
2. Override rendering methods
3. Add to MainWindow


## Installation & Running

# Install dependencies
pip install -r requirements.txt

# Run application
python -m src.main
# OR
python run.py

# Run tests
python tests.py


## Performance Characteristics

Time Complexities:
- Insert: O(log n) average, O(n) worst
- Delete: O(log n) average, O(n) worst
- Search: O(log n) average, O(n) worst
- Traversals: O(n)
- Height: O(n)
- Balance check: O(n)

Space Complexities:
- Tree storage: O(n)
- History: O(min(operations, max_history))
- Visualization: O(n) for layout


## Resume Highlights

This project demonstrates:

✓ Strong data structure knowledge
✓ Algorithm implementation skills
✓ GUI development with PyQt5
✓ Software design patterns
✓ Clean code principles
✓ Object-oriented programming
✓ Professional project structure
✓ Comprehensive documentation
✓ Testing and quality assurance
✓ Problem-solving abilities


## Future Enhancement Ideas

- AVL tree with auto-balancing
- Red-Black tree visualization
- B-tree implementation
- Animation speed slider
- Export to image file
- Tree persistence (save/load)
- Comparison mode for different trees
- Advanced layout algorithms


## Contact & Version Info

Version: 2.0
Status: Production Ready
Last Updated: February 2026
Type: Desktop Application (PyQt5)
Language: Python 3.7+

This is a professional-grade project suitable for:
- Portfolio showcase
- Technical interviews
- Educational purposes
- Teaching/learning data structures
"""
