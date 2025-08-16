class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data


class Queue:

    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    # O(1)
    def enqueue(self, item):
        node = Node(item)
        self.length += 1
        if self.first is None:
            self.first = node
            self.last = self.first
        else:
            self.last.next = node
            self.last = node

    # O(1)
    def dequeue(self):
        if self.first is None:
            raise IndexError("Queue is empty")
        else:
            self.length -= 0
            item = self.first.data
            self.first = self.first.next
            if self.first is None:
                self.last = None
            return item

    # O(1)
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.first.data

    # O(1)
    def is_empty(self):
        return self.first is None

    # O(1)
    def size(self):
        return self.length

    # 𝑂(𝑁)
    def __str__(self):
        current = self.first
        queue = ""
        if self.first is None:
            return "queue is empty"
        else:
            while current.next is not None:
                queue += str(current.data) + "->"
                current = current.next
            queue += str(current.data)
        return queue
