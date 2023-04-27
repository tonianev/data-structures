import pytest
from src.min_heap import MinHeap

def test_min_heap():
    heap = MinHeap()

    heap.insert(5)
    assert heap.heap == [5]

    heap.insert(3)
    assert heap.heap == [3, 5]

    heap.insert(7)
    assert heap.heap == [3, 5, 7]

    heap.insert(1)
    assert heap.heap == [1, 3, 7, 5]

    min_value = heap.remove_min()
    assert min_value == 1
    assert heap.heap == [3, 5, 7]

    min_value = heap.remove_min()
    assert min_value == 3
    assert heap.heap == [5, 7]

    min_value = heap.remove_min()
    assert min_value == 5
    assert heap.heap == [7]
