class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.map = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        for pair in self.map[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.map[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.map[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.map[index]):
            if pair[0] == key:
                del self.map[index][i]
                return True
        return False
