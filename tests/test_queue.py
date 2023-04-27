import pytest
from src.queue import Queue

def test_queue():
    queue = Queue()

    assert queue.is_empty()
    assert queue.size() == 0

    queue.enqueue(1)
    assert not queue.is_empty()
    assert queue.size() == 1

    queue.enqueue(2)
    assert queue.size() == 2

    assert queue.dequeue() == 1
    assert queue.size() == 1

    assert queue.dequeue() == 2
    assert queue.is_empty()
    assert queue.size() == 0

    assert queue.dequeue() is None
