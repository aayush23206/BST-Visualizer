"""
Unit tests for BST Visualizer components.
Run with: python tests.py
"""

import sys
sys.path.insert(0, '.')

from src.models import BinarySearchTree, Node


def test_node_creation():
    """Test node creation and properties."""
    print("Testing Node Creation...", end=" ")
    node = Node(50)
    assert node.value == 50
    assert node.left is None
    assert node.right is None
    assert node.is_leaf()
    print("✓")


def test_bst_insert():
    """Test BST insertion."""
    print("Testing BST Insert...", end=" ")
    bst = BinarySearchTree()
    assert bst.insert(50)
    assert bst.insert(30)
    assert bst.insert(70)
    assert bst.insert(20)
    assert not bst.insert(50)  # Duplicate
    assert bst.get_size() == 4
    print("✓")


def test_bst_search():
    """Test BST search."""
    print("Testing BST Search...", end=" ")
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    
    assert bst.search(50) is not None
    assert bst.search(30) is not None
    assert bst.search(99) is None
    print("✓")


def test_bst_delete_leaf():
    """Test deleting a leaf node."""
    print("Testing Delete Leaf...", end=" ")
    bst = BinarySearchTree()
    for val in [50, 30, 70, 20, 40]:
        bst.insert(val)
    
    assert bst.delete(20)
    assert bst.search(20) is None
    assert bst.get_size() == 4
    print("✓")


def test_bst_delete_one_child():
    """Test deleting a node with one child."""
    print("Testing Delete One Child...", end=" ")
    bst = BinarySearchTree()
    for val in [50, 30, 70, 20]:
        bst.insert(val)
    
    assert bst.delete(30)
    assert bst.search(30) is None
    assert bst.search(20) is not None
    print("✓")


def test_bst_delete_two_children():
    """Test deleting a node with two children."""
    print("Testing Delete Two Children...", end=" ")
    bst = BinarySearchTree()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)
    
    assert bst.delete(30)
    assert bst.search(30) is None
    # Confirm tree structure is maintained
    result = bst.inorder_traversal()
    assert result == [20, 40, 50, 60, 70, 80]
    print("✓")


def test_bst_inorder():
    """Test inorder traversal."""
    print("Testing Inorder Traversal...", end=" ")
    bst = BinarySearchTree()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)
    
    result = bst.inorder_traversal()
    assert result == [20, 30, 40, 50, 60, 70, 80]
    print("✓")


def test_bst_preorder():
    """Test preorder traversal."""
    print("Testing Preorder Traversal...", end=" ")
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    
    result = bst.preorder_traversal()
    assert result == [50, 30, 70]
    print("✓")


def test_bst_postorder():
    """Test postorder traversal."""
    print("Testing Postorder Traversal...", end=" ")
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    
    result = bst.postorder_traversal()
    assert result == [30, 70, 50]
    print("✓")


def test_bst_levelorder():
    """Test level-order traversal."""
    print("Testing Level-order Traversal...", end=" ")
    bst = BinarySearchTree()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)
    
    result = bst.levelorder_traversal()
    assert result == [50, 30, 70, 20, 40, 60, 80]
    print("✓")


def test_bst_height():
    """Test height calculation."""
    print("Testing Height Calculation...", end=" ")
    bst = BinarySearchTree()
    assert bst.get_height() == -1  # Empty tree
    
    bst.insert(50)
    assert bst.get_height() == 0  # Single node
    
    bst.insert(30)
    bst.insert(70)
    assert bst.get_height() == 1  # Balanced tree
    
    bst.insert(20)
    assert bst.get_height() == 2
    print("✓")


def test_bst_balanced():
    """Test balanced tree check."""
    print("Testing Balance Check...", end=" ")
    
    # Balanced tree
    bst = BinarySearchTree()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)
    assert bst.is_balanced()
    
    # Unbalanced tree (linked list)
    bst2 = BinarySearchTree()
    for val in [10, 20, 30, 40, 50]:
        bst2.insert(val)
    assert not bst2.is_balanced()
    print("✓")


def test_operation_history():
    """Test undo/redo history."""
    print("Testing Operation History...", end=" ")
    from src.utils import OperationHistory, Operation
    
    history = OperationHistory()
    
    # Create and record operations
    def undo1(): pass
    def redo1(): pass
    
    op1 = Operation(name="Op1", undo_action=undo1, redo_action=redo1)
    history.record_operation(op1)
    
    assert history.can_undo()
    assert not history.can_redo()
    
    # Test undo
    assert history.undo()
    assert not history.can_undo()
    assert history.can_redo()
    
    # Test redo
    assert history.redo()
    assert history.can_undo()
    assert not history.can_redo()
    print("✓")


def test_animation():
    """Test animation engine."""
    print("Testing Animation Engine...", end=" ")
    from src.utils import AnimationEngine, AnimationType
    
    engine = AnimationEngine()
    progress_values = []
    
    def on_update(progress):
        progress_values.append(progress)
    
    anim = engine.create_animation(
        duration=100,
        on_update=on_update,
        animation_type=AnimationType.LINEAR
    )
    
    # Simulate updates
    engine.update(50)  # 50ms
    assert len(progress_values) > 0
    assert progress_values[-1] == 0.5
    
    engine.update(50)  # 100ms total
    assert progress_values[-1] >= 0.99
    assert anim.is_complete
    print("✓")


def test_tree_properties():
    """Test various tree properties."""
    print("Testing Tree Properties...", end=" ")
    bst = BinarySearchTree()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)
    
    assert bst.get_size() == 7
    assert not bst.is_empty()
    assert bst.get_height() == 2
    
    bst.clear()
    assert bst.is_empty()
    assert bst.get_size() == 0
    print("✓")


def test_edge_cases():
    """Test edge cases."""
    print("Testing Edge Cases...", end=" ")
    
    # Single node tree
    bst = BinarySearchTree()
    bst.insert(50)
    assert bst.delete(50)
    assert bst.is_empty()
    
    # Delete non-existent
    bst2 = BinarySearchTree()
    bst2.insert(50)
    assert not bst2.delete(99)
    
    # Large tree
    bst3 = BinarySearchTree()
    for i in range(1, 101):
        bst3.insert(i)
    assert bst3.get_size() == 100
    print("✓")


def run_all_tests():
    """Run all unit tests."""
    print("\n" + "="*50)
    print("BST Visualizer - Unit Tests")
    print("="*50 + "\n")
    
    tests = [
        test_node_creation,
        test_bst_insert,
        test_bst_search,
        test_bst_delete_leaf,
        test_bst_delete_one_child,
        test_bst_delete_two_children,
        test_bst_inorder,
        test_bst_preorder,
        test_bst_postorder,
        test_bst_levelorder,
        test_bst_height,
        test_bst_balanced,
        test_operation_history,
        test_animation,
        test_tree_properties,
        test_edge_cases,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ ERROR: {e}")
            failed += 1
    
    print("\n" + "="*50)
    print(f"Results: {passed} passed, {failed} failed")
    print("="*50 + "\n")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
