"""
COMPREHENSIVE FEATURE GUIDE

This guide covers all features and how to use them.

## CORE FEATURES

### 1. INSERT NODE
What it does:
  - Adds a new node to the BST
  - Maintains BST property (left < root < right)
  - Highlights the new node briefly

How to use:
  1. Enter an integer value in "Node Value" field
  2. Click "Insert" or press Enter
  3. Node appears in tree and flashes red

Edge cases:
  - Duplicate values are rejected
  - Maximum value constraints enforced
  - Empty tree handled correctly

Example:
  Insert: 50, 30, 70, 20, 40, 60, 80
  Result tree:
         50
        /  \
       30   70
      / \   / \
     20 40 60 80


### 2. DELETE NODE
What it does:
  - Removes node from tree
  - Handles all three deletion cases
  - Tree structure is automatically reorganized

How to use:
  1. Enter node value in "Node Value" field
  2. Click "Delete"
  3. Tree updates automatically

Handles:
  - Leaf nodes (no children) - simple removal
  - One child - replace with child
  - Two children - replace with in-order successor

Example flows:
  Delete 20: Removes leaf node
  Delete 30: Replaces with right subtree (single child)
  Delete 50: Replaces with 60 (in-order successor)


### 3. SEARCH NODE
What it does:
  - Finds a node in the tree
  - Highlights found node
  - Shows success/failure message

How to use:
  1. Enter search value
  2. Click "Search"
  3. Node highlights if found (yellow) or message if not found

Speed:
  - Average: O(log n) - balanced tree
  - Worst: O(n) - unbalanced tree


### 4. TREE TRAVERSALS

#### Inorder (Left-Root-Right)
  - Results in SORTED order
  - Example: 20, 30, 40, 50, 60, 70, 80
  - Use: When sorted values needed

#### Preorder (Root-Left-Right)
  - Root visited first
  - Example: 50, 30, 20, 40, 70, 60, 80
  - Use: Copying/serializing tree

#### Postorder (Left-Right-Root)
  - Root visited last
  - Example: 20, 40, 30, 60, 80, 70, 50
  - Use: Deleting tree structure

#### Level-Order (BFS)
  - Level by level from top
  - Example: 50, 30, 70, 20, 40, 60, 80
  - Use: Breadth-first search

How to use:
  1. Select traversal type from dropdown
  2. (Optional) Check "Animate Steps" for visualization
  3. Click "Execute Traversal"
  4. Result appears in "Traversal Output" section


### 5. TREE VISUALIZATION

Features:
  - Automatic node layout prevents overlap
  - Nodes drawn as circles with values
  - Edges connect parent to children
  - Real-time updates after operations

Interaction:
  - Click on nodes for information
  - Hover for visual feedback
  - Smooth redraws after operations

Colors:
  - Blue: Normal nodes
  - Red: Highlighted nodes (insert/delete)
  - Yellow: Nodes in search path
  - During traversal: Flash effect


### 6. STATISTICS PANEL

Shows:
  - Node Count: Total nodes in tree
  - Height: Longest path from root to leaf
  - Balance Status: Is tree balanced?

Interpretation:
  - Height 2, 7 nodes = balanced tree
  - Height 6, 7 nodes = unbalanced tree
  - Balanced trees have better performance

Example:
  Tree: 50, 30, 70, 20, 40, 60, 80
  Stats:
    Nodes: 7
    Height: 2
    Balanced: Yes


### 7. UNDO/REDO

Features:
  - Remembers last 50 operations
  - Reverts tree to any previous state
  - Works with all operations

How to use:
  1. Make some operations (insert, delete, etc.)
  2. Click "↶ Undo" to go back
  3. Click "↷ Redo" to go forward
  4. Buttons disabled when no history available

Supported operations:
  ✓ Insert node
  ✓ Delete node
  ✓ Clear tree
  ✓ Generate random tree


### 8. RANDOM TREE GENERATION

What it does:
  - Creates tree with random non-duplicate values
  - Useful for testing and experimentation

How to use:
  1. Set number of nodes (1-50) with spinner
  2. Click "Generate Random Tree"
  3. Fully populated tree appears instantly

Example:
  Generate 10 nodes
  Result: Tree with 10 random unique values


### 9. CLEAR TREE

What it does:
  - Removes all nodes
  - Confirmation dialog prevents accidents
  - Can be undone

How to use:
  1. Click "Clear Tree" button
  2. Confirm in dialog
  3. All nodes removed


### 10. DARK/LIGHT MODE

What it does:
  - Switches visual theme
  - Changes colors for comfortable viewing
  - Applies to entire application

Light Theme:
  - White background
  - Dark text and borders
  - Blue accent colors

Dark Theme:
  - Dark background
  - Light text
  - Blue accent colors

How to use:
  - Check/uncheck "Dark Mode" in Settings
  - Changes apply immediately


## WORKFLOW EXAMPLES

### Example 1: Build Manual Tree
1. Insert 50
2. Insert 30
3. Insert 70
4. Insert 20
5. Insert 40
6. Insert 60
7. Insert 80
Result: Balanced tree with 7 nodes

### Example 2: Test Deletions
1. Generate random tree (15 nodes)
2. Search for a node (to see it)
3. Delete that node
4. Verify with inorder traversal
5. Undo if not satisfied
6. Try again

### Example 3: Understand Traversals
1. Insert: 50, 30, 70, 20, 40, 60, 80
2. Execute Inorder → See sorted values
3. Execute Preorder → See root-first order
4. Execute Postorder → See root-last order
5. Execute Level-order → See breadth-first order


## KEYBOARD SHORTCUTS

In numeric input fields:
  - Press ENTER to execute operation
  - Works for Insert, Delete, Search

In Tree Canvas:
  - Click nodes for information
  - No other shortcuts (use buttons)


## ERROR MESSAGES & SOLUTIONS

"Error: Maximum tree size reached"
  → Solution: Clear tree and start fresh

"Error: [value] already exists"
  → Solution: Use unique values for insert

"Error: [value] not found in tree"
  → Solution: Tree doesn't contain value

"Error: Cannot traverse empty tree"
  → Solution: Insert some nodes first

"Nothing to undo"
  → Solution: No operations have been performed

"Nothing to redo"
  → Solution: No undone operations to redo


## PERFORMANCE TIPS

For best performance:
  ✓ Keep trees balanced (height ~log n)
  ✓ Use appropriate operations
  ✓ Don't create extremely large trees (50+ nodes gets crowded)
  ✓ Use animations for learning, not for speed

Unbalanced trees (linked list) are:
  ✗ Slow for search/insert/delete
  ✗ Hard to visualize (all on one side)
  ✗ Poor learning examples


## TESTING YOUR KNOWLEDGE

Try these exercises:

1. Binary Search Tree Properties
   - Insert: 15, 10, 20, 5, 12, 17, 25
   - Verify each value is correct position
   - Check height is minimal

2. Deletion Cases
   - Create tree with 10 nodes
   - Delete a leaf (1st test)
   - Delete node with 1 child (2nd test)
   - Delete node with 2 children (3rd test)
   - Verify tree structure maintained

3. Traversal Understanding
   - Create small tree (7 nodes)
   - Run each traversal to understand
   - Predict output before running

4. Balance Understanding
   - Generate random tree
   - Check if balanced
   - Generate unbalanced tree (1, 2, 3, ...)
   - Compare statistics

5. History System
   - Make 5 operations
   - Undo 3 times
   - Redo 2 times
   - Verify tree state


## TIPS FOR EFFECTIVE USE

1. Start Small
   - Begin with 5-7 nodes
   - Learn operations first
   - Scale up gradually

2. Use Animations
   - Enable for learning
   - See step-by-step visualization
   - Understand flow better

3. Check Statistics
   - After each operation
   - Understand height impact
   - Verify balance status

4. Use Undo/Redo
   - Experiment safely
   - Revert mistakes instantly
   - Test hypotheses

5. Generate Random Trees
   - Test with different sizes
   - See how operations scale
   - Understand average vs worst case


## ADVANCED USAGE

Exploring Algorithm Behavior:
  1. Create unbalanced tree (1, 2, 3, 4, 5)
  2. Note height is high (4)
  3. Search takes longer
  4. Clear and create balanced tree
  5. Note height is low (2)
  6. Search is faster

Measuring Operations:
  1. Count mouse clicks per operation
  2. Time traversal animations
  3. Estimate algorithm efficiency
  4. Compare with theory O(n) vs O(log n)

Teaching Others:
  1. Create example tree
  2. Use animations for clarity
  3. Show statistics changing
  4. Demonstrate impact on performance


## ACCESSIBILITY

- Works with keyboard (Enter in fields)
- Click to interact with nodes
- Color highlighting for visibility
- Dark mode for eye protection
- All buttons clearly labeled
- Status messages for feedback


## TROUBLESHOOTING

Application won't start:
  → Check Python 3.7+ installed
  → Check PyQt5 installed (pip install PyQt5)
  → Run from project directory

Tree doesn't draw:
  → Close and reopen application
  → Ensure window is not minimized
  → Try clearing tree and inserting nodes

Buttons don't work:
  → Click once (double-click not needed)
  → Wait for animation to complete
  → Check input fields for valid values

Undo/Redo disabled:
  → No operations performed yet
  → At history boundary (nothing to undo/redo)
  → This is normal behavior


## SUMMARY

This BST Visualizer provides:
✓ Complete tree operations
✓ Real-time visualization
✓ Interactive learning
✓ Professional interface
✓ Comprehensive features
✓ Educational value

Perfect for:
- Learning data structures
- Teaching BST concepts
- Portfolio projects
- Interview preparation
- Algorithm visualization

Enjoy exploring Binary Search Trees!
"""
