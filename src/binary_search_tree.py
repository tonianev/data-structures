class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if not node.left:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if not node.right:
                node.right = Node(data)
            else:
                self._insert(data, node.right)
