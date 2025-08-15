from collections import deque


class Stack:
    # O(1)
    def __init__(self):
        self.items = deque()

    # O(1)
    def push(self, items):
        self.items.append(items)

    # O(1)
    def pop(self):
        if len(self.items) == 0:
            raise IndexError("Stack is empty")
        return self.items.pop()

    # O(1)
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.items[-1]

    # O(1)
    def is_empty(self):
        return len(self.items) <= 0

    # O(1)
    def size(self):
        return len(self.items)
