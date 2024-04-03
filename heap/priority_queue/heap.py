class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        while self.heap[i] < self.heap[i//2]:
            tmp = 