class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def remove_min(self):
        if not self.heap:
            return None
        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return min_value

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index < 0:
            return
        if self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index >= len(self.heap):
            return

        min_child_index = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[left_child_index]:
            min_child_index = right_child_index

        if self.heap[index] > self.heap[min_child_index]:
            self.heap[index], self.heap[min_child_index] = self.heap[min_child_index], self.heap[index]
            self._heapify_down(min_child_index)
