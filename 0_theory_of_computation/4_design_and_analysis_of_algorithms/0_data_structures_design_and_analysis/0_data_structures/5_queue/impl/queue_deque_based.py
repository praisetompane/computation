from collections import deque


class Queue:
    # O(1)
    def __init__(self):
        self.items = deque()

    # O(1)
    def enqueue(self, item):
        self.items.appendleft(item)

    # O(1)
    def dequeue(self):
        if len(self.items) == 0:
            raise IndexError("Queue is empty")
        else:
            return self.items.pop()

    # O(1)
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    # O(1)
    def is_empty(self):
        return len(self.items) <= 0

    # O(1)
    def size(self):
        return len(self.items)

    # 𝑂(𝑁)
    def __str__(self):
        return " ,".join([str(i) for i in self.items])
