"""
ALGORITHM DOCUMENTATION

This file explains the algorithms implemented in the BST Visualizer.

## Binary Search Tree Properties

Definition:
- For every node N:
  - All values in left subtree < N.value
  - All values in right subtree > N.value
  - This property holds recursively for all subtrees

## Insert Algorithm

Time Complexity: O(h) where h = height
Space Complexity: O(h) for recursion stack

```
Insert(value):
    if root is None:
        create new node
    else:
        insert_recursive(root, value)

insert_recursive(node, value):
    if value < node.value:
        if node.left is None:
            create new left child
        else:
            insert_recursive(node.left, value)
    elif value > node.value:
        if node.right is None:
            create new right child
        else:
            insert_recursive(node.right, value)
    else:
        duplicate found, return False
```

Example: Inserting [50, 30, 70, 20, 40, 60, 80]

```
        50
       /  \
      30   70
     / \   / \
    20 40 60 80
```

## Delete Algorithm

Three cases handled:

### Case 1: Leaf Node (no children)
Simply remove the node

```
      50              50
     /  \            /  \
    30   70   →     30   70
   / \   /         / \   /
  20 40 60        20 40 60
  (delete 40)
```

### Case 2: One Child
Replace node with its child

```
      50              50
     /  \            /  \
    30   70   →     30   70
   /     /  \            /  \
  20    60  80          60  80
  (delete 40 - it's included in step 1 since it's a leaf)
```

### Case 3: Two Children
Replace with in-order successor (minimum value in right subtree)

```
      50              60
     /  \            /  \
    30   70   →     30   70
   / \   /  \      / \      \
  20 40 60  80    20 40     80
  (delete 50, replace with 60)
```

In-order successor finding:
- Start at right child
- Keep going left until no more left child
- That node is the successor

Time Complexity: O(h)
Space Complexity: O(h)

## Search Algorithm

Time Complexity: O(h)
Space Complexity: O(h)

```
Search(value):
    return search_recursive(root, value)

search_recursive(node, value):
    if node is None:
        return None
    if value == node.value:
        return node
    elif value < node.value:
        return search_recursive(node.left, value)
    else:
        return search_recursive(node.right, value)
```

Uses BST property to eliminate half of search space at each step.

## Traversal Algorithms

All traversals are O(n) time and O(h) space (recursion stack).

### 1. Inorder Traversal (Left-Root-Right)

Results in sorted order (for BST).

```
Inorder(node):
    if node is not None:
        Inorder(node.left)
        visit(node)
        Inorder(node.right)

Example tree:
        50
       /  \
      30   70
     / \   / \
    20 40 60 80

Output: 20 → 30 → 40 → 50 → 60 → 70 → 80
```

Use Cases:
- Print sorted values
- Find kth smallest element
- Checking if tree is BST

### 2. Preorder Traversal (Root-Left-Right)

Visits parent before children.

```
Preorder(node):
    if node is not None:
        visit(node)
        Preorder(node.left)
        Preorder(node.right)

Example tree:
        50
       /  \
      30   70
     / \   / \
    20 40 60 80

Output: 50 → 30 → 20 → 40 → 70 → 60 → 80
```

Use Cases:
- Copy tree structure
- Create prefix expression
- Serialize tree

### 3. Postorder Traversal (Left-Right-Root)

Visits parent after children.

```
Postorder(node):
    if node is not None:
        Postorder(node.left)
        Postorder(node.right)
        visit(node)

Example tree:
        50
       /  \
      30   70
     / \   / \
    20 40 60 80

Output: 20 → 40 → 30 → 60 → 80 → 70 → 50
```

Use Cases:
- Delete tree (children before parent)
- Postfix expression evaluation
- Tree cleanup operations

### 4. Level-Order Traversal (BFS)

Visits nodes level by level.

```
LevelOrder(root):
    queue = Queue()
    queue.enqueue(root)
    while queue is not empty:
        node = queue.dequeue()
        visit(node)
        if node.left is not None:
            queue.enqueue(node.left)
        if node.right is not None:
            queue.enqueue(node.right)

Example tree:
        50
       /  \
      30   70
     / \   / \
    20 40 60 80

Output: 50 → 30 → 70 → 20 → 40 → 60 → 80
```

Use Cases:
- Print tree level by level
- Serialization with level information
- Finding shortest path

## Height Calculation

Time Complexity: O(n)
Space Complexity: O(h) for recursion

```
Height(node):
    if node is None:
        return -1
    return 1 + max(Height(node.left), Height(node.right))

Example:
        50          height = 2
       /  \
      30   70       height = 1
     / \   / \
    20 40 60 80     height = 0
```

Heights:
- Empty tree: -1
- Single node: 0
- Example above: 2

## Balance Check Algorithm

A tree is balanced if:
- |Height(left) - Height(right)| <= 1 for every node

Time Complexity: O(n)
Space Complexity: O(h)

```
IsBalanced(node):
    if node is None:
        return (True, -1)
    
    left_balanced, left_height = IsBalanced(node.left)
    if not left_balanced:
        return (False, 0)
    
    right_balanced, right_height = IsBalanced(node.right)
    if not right_balanced:
        return (False, 0)
    
    is_current_balanced = 
        abs(left_height - right_height) <= 1
    
    return (is_current_balanced, 
            1 + max(left_height, right_height))
```

Example Balanced:
        50
       /  \
      30   70
     / \   / \
    20 40 60 80

Example Unbalanced:
        50
       /
      30
     /
    20
   /
  10

## Node Positioning Algorithm

Recursive binary tree layout for visualization.

Time Complexity: O(n)
Space Complexity: O(h)

```
CalculatePositions(node, x, y, offset):
    if node is None:
        return
    
    node.x = x
    node.y = y
    
    next_y = y + VERTICAL_GAP
    next_offset = offset / 2
    
    if node.left:
        left_x = x - offset
        CalculatePositions(node.left, 
                          left_x, next_y, 
                          next_offset)
    
    if node.right:
        right_x = x + offset
        CalculatePositions(node.right, 
                          right_x, next_y, 
                          next_offset)
```

Properties:
- Centers children below parent
- Prevents node overlap
- Exponentially decreasing offset prevents crowding
- O(n) positions calculated in single pass

## Easing Functions for Animation

Used for smooth visual transitions.

### Linear
f(t) = t
- Constant speed throughout animation

### Ease-In
f(t) = t²
- Starts slow, accelerates
- Used for emphasis on arrival

### Ease-Out
f(t) = 2t - t²
- Starts fast, decelerates
- Used for emphasis on departure

### Ease-In-Out
f(t) = 2t² (if t < 0.5) or 1 - (-2t+2)²/2 (if t >= 0.5)
- Smooth acceleration and deceleration
- Most natural feeling animation

## Complexity Summary

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Insert    | O(h) | O(h)  | Recursive stack |
| Delete    | O(h) | O(h)  | Worst: finding successor |
| Search    | O(h) | O(h)  | Using BST property |
| Inorder   | O(n) | O(h)  | DFS recursion |
| Preorder  | O(n) | O(h)  | DFS recursion |
| Postorder | O(n) | O(h)  | DFS recursion |
| Level-order | O(n) | O(w) | w = max width |
| Height    | O(n) | O(h)  | Full tree scan |
| Balanced  | O(n) | O(h)  | Early termination possible |

Where:
- h = height of tree
- n = number of nodes
- w = maximum width (nodes at any level)

## Worst Case Scenario

When tree becomes degenerate (linked list):
```
50
  \
   60
     \
      70
        \
         80
           \
            90
```

All operations become O(n) instead of O(log n).

Balanced tree:
```
        50
       /  \
      30   70
     / \   / \
    20 40 60 80
```

Operations maintain O(log n) performance.

## Algorithm Validation

The implementation includes:

✓ Correct BST property maintenance
✓ All delete cases handled properly
✓ All traversal algorithms implemented
✓ Proper recursive termination conditions
✓ Height and balance calculations
✓ Position calculations prevent overlap
✓ Animation easing functions smooth and natural

## Teaching Points

This implementation demonstrates:

1. Fundamental Data Structures
2. Tree Traversal Techniques
3. Recursive Algorithm Design
4. Algorithm Complexity Analysis
5. Software Design Patterns
6. GUI Visualization Techniques
7. Real-time Performance Optimization
8. Mathematical Concepts (easing functions)

Perfect for interviews and portfolio demonstration.
"""
