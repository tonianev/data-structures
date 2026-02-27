# Data Structures in Python

Production-style reference implementations of core data structures with unit tests.

## Status

- Active maintenance
- Intended as a clean, practical study and interview-prep reference

## Included Data Structures

- [Linked List](src/linked_list.py)
- [Doubly Linked List](src/doubly_linked_list.py)
- [Stack](src/stack.py)
- [Queue](src/queue.py)
- [Hash Map](src/hash_map.py)
- [Binary Search Tree](src/binary_search_tree.py)
- [Min Heap](src/min_heap.py)
- [Trie](src/trie.py)
- [Union Find](src/union_find.py)
- [Graph](src/graph.py)

## Project Layout

```text
data-structures/
├── src/
├── tests/
├── requirements.txt
└── setup.py
```

## Quickstart

```bash
git clone https://github.com/tonianev/data-structures.git
cd data-structures
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run Tests

```bash
python -m unittest discover -s tests -v
```

## Why this repo exists

- Provide readable, test-backed implementations for common structures
- Demonstrate clear API contracts and expected behaviors
- Keep examples lightweight and dependency-minimal

## License

MIT. See [LICENSE](LICENSE).
