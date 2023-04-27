import pytest
from src.binary_search_tree import BinarySearchTree, Node

def test_node():
    node = Node(5)
    assert node.data == 5
    assert node.left is None
    assert node.right is None

def test_binary_search_tree_insert():
    bst = BinarySearchTree()

    # Test inserting a single element
    bst.insert(10)
    assert bst.root.data == 10
    assert bst.root.left is None
    assert bst.root.right is None

    # Test inserting smaller and larger elements
    bst.insert(5)
    bst.insert(15)
    assert bst.root.left.data == 5
    assert bst.root.right.data == 15
    assert bst.root.left.left is None
    assert bst.root.left.right is None
    assert bst.root.right.left is None
    assert bst.root.right.right is None

    # Test inserting elements in deeper levels
    bst.insert(12)
    bst.insert(18)
    assert bst.root.right.left.data == 12
    assert bst.root.right.right.data == 18
