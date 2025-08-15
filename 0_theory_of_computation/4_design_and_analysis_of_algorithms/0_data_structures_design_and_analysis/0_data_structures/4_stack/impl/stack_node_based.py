class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data


class Stack:
    # O(1)
    def __init__(self):
        self.top = None

    # O(1)
    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node

    # O(1)
    def pop(self):
        if self.top is None:
            raise Exception("Stack is empty")

        item = self.top.data
        self.top = self.top.next
        return item

    # O(1)
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    # O(1)
    def is_empty(self):
        return self.top is None

    # O(N)
    def size(self):
        size = 0
        current_node = self.top
        while current_node:
            size += 1
            current_node = current_node.next
        return size
