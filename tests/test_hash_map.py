import pytest
from src.hash_map import HashMap

def test_hash_map():
    hmap = HashMap()

    hmap.put('apple', 5)
    hmap.put('banana', 10)

    assert hmap.get('apple') == 5
    assert hmap.get('banana') == 10
    assert hmap.get('orange') is None

    hmap.put('apple', 15)
    assert hmap.get('apple') == 15

    assert hmap.remove('apple') == True
    assert hmap.get('apple') is None
    assert hmap.remove('apple') == False
    assert hmap.get('banana') == 10
