class MaxHeap:
    def __init__(self):
        self.heap = []

    def _priority(self, patient):
        # Create a tuple to compare priorities using these factors: (severity, age, arrival_order)
        return (-patient.severity, -patient.age, patient.arrival_order)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self._priority(self.heap[index]) < self._priority(self.heap[parent]):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        size = len(self.heap)
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < size and self._priority(self.heap[left]) < self._priority(self.heap[largest]):
            largest = left
        if right < size and self._priority(self.heap[right]) < self._priority(self.heap[largest]):
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def insert(self, patient):
        self.heap.append(patient)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def peek_max(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)
