import pytest
from src.linked_list import LinkedList, Node

def test_node():
    node = Node(5)
    assert node.data == 5
    assert node.next is None

def test_linked_list_append():
    linked_list = LinkedList()
    
    # Test appending a single element
    linked_list.append(1)
    assert linked_list.head.data == 1
    assert linked_list.head.next is None

    # Test appending a second element
    linked_list.append(2)
    assert linked_list.head.next.data == 2
    assert linked_list.head.next.next is None
