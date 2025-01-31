class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, email):
        self.heap.append(email)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) > 1:
            self._swap(0, len(self.heap) - 1)
            email = self.heap.pop()
            self._heapify_down(0)
            return email
        elif self.heap:
            return self.heap.pop()
        return None

    def peek(self):
        if self.heap:
            return self.heap[0]
        return None

    def count(self):
        return len(self.heap)


    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self._priority(self.heap[index]) < self._priority(self.heap[parent]):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index
            if left < size and self.heap[left] < self.heap[largest]:
                largest = left
            if right < size and self.heap[right] < self.heap[largest]:
                largest = right
            if largest == index:
                break
            self._swap(index, largest)
            index = largest

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def peek_max(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)
