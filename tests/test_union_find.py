import pytest
from src.data_structures.union_find import UnionFind

def test_union_find():
    uf = UnionFind(5)

    assert uf.union(0, 1)
    assert uf.find(0) == uf.find(1)

    assert uf.union(2, 3)
    assert uf.find(2) == uf.find(3)

    assert not uf.union(0, 1)
    assert not uf.union(2, 3)

    assert uf.union(1, 2)
    assert uf.find(0) == uf.find(2)
    assert uf.find(1) == uf.find(3)
