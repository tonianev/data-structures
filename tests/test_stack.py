import pytest
from src.stack import Stack

def test_stack():
    stack = Stack()

    assert stack.is_empty()
    assert stack.size() == 0

    stack.push(1)
    assert not stack.is_empty()
    assert stack.size() == 1
    assert stack.peek() == 1

    stack.push(2)
    assert stack.size() == 2
    assert stack.peek() == 2

    assert stack.pop() == 2
    assert stack.size() == 1
    assert stack.peek() == 1

    assert stack.pop() == 1
    assert stack.is_empty()
    assert stack.size() == 0

    assert stack.pop() is None
