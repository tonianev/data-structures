import pytest
from src.trie import Trie

def test_trie():
    trie = Trie()

    trie.insert('hello')
    assert trie.search('hello') == True
    assert trie.search('hell') == False
    assert trie.starts_with('hell') == True
    assert trie.starts_with('hello') == True
    assert trie.starts_with('hel') == True
    assert trie.starts_with('h') == True
    assert trie.starts_with('helly') == False

    trie.insert('world')
    assert trie.search('world') == True
    assert trie.search('worl') == False
    assert trie.starts_with('worl') == True
    assert trie.starts_with('world') == True
