import sys


class MinHeap:
    def __init__(self):
        self.queue = []

    def insert(self, item):
        self.queue.append(item)
        child_index = len(self.queue) - 1

        while child_index != 0:
            parent_index = (child_index - 1) // 2
            if self.queue[parent_index] > self.queue[child_index]:
                self.swap(parent_index, child_index)
                child_index = parent_index
            else:
                break

    def delete(self):
        if len(self.queue) == 0:
            return 0

        self.swap(0, -1)
        min_val = self.queue.pop()
        self.heapify(0)
        return min_val

    def heapify(self, idx):
        parent_index = idx
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2

        if left_child < len(self.queue) and self.queue[parent_index] > self.queue[left_child]:
            parent_index = left_child
        if right_child < len(self.queue) and self.queue[parent_index] > self.queue[right_child]:
            parent_index = right_child

        if parent_index != idx:
            self.swap(parent_index, idx)
            self.heapify(parent_index)

    def swap(self, idx1, idx2):
        self.queue[idx1], self.queue[idx2] = self.queue[idx2], self.queue[idx1]


N = int(input())
heap = MinHeap()

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        print(heap.delete())
    else:
        heap.insert(x)
