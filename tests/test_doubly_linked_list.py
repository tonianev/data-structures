import pytest
from src.doubly_linked_list import DoublyLinkedList, Node

def test_node():
    node = Node(5)
    assert node.data == 5
    assert node.next is None
    assert node.prev is None

def test_doubly_linked_list_append():
    doubly_linked_list = DoublyLinkedList()

    # Test appending a single element
    doubly_linked_list.append(1)
    assert doubly_linked_list.head.data == 1
    assert doubly_linked_list.head.next is None
    assert doubly_linked_list.head.prev is None
    assert doubly_linked_list.tail.data == 1

    # Test appending a second element
    doubly_linked_list.append(2)
    assert doubly_linked_list.head.next.data == 2
    assert doubly_linked_list.head.next.prev.data == 1
    assert doubly_linked_list.tail.data == 2
