from singly.node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        length = 0
        current_node = self.head
        while (current_node):
            length = length + 1
            current_node = current_node.next
        return length

    def insert_at_top(self, data):
        node = Node(data)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    def insert_values(self, values: list):
        """
            Insert iterable of values to the end
        """
        # O(N). N = length of current values in list

        def _insert_values(start_index):
            # O(M). M = length of new values
            current_node = self.head
            while (current_node.next):
                current_node = current_node.next

            idx = start_index
            while (idx < len(values)):
                current_node.next = Node(values[idx])
                current_node = current_node.next
                idx += 1

        if self.head == None:
            self.head = Node(values[0])
            _insert_values(1)
        else:
            _insert_values(0)

        # Total = O(N + M) = O(N) | O(M) depending on which is longer. Therefore Linear = O(N)

        # alternative
        # for v in values:
        #     self.insert(v)
        # O(N * M)
            # N = length of current values in list
            # M = length of new values
            # if M = N, then O(N*N) = O(N^2)

    def remove_from_top(self):
        if self.head:
            node = self.head
            self.head = self.head.next
            return node.data
        else:
            raise ValueError("List is empty")

    def insert_at_end(self, data):
        node = Node(data)
        if self.head:
            current_node = self.head
            while (current_node.next):
                current_node = current_node.next
            current_node.next = node
        else:
            self.head = node

    def insert_after_value(self, predicate_value, data):
        if self.head == None:
            raise IndexError("The list is empty")

        current_node = self.head
        while (current_node):
            if current_node.data == predicate_value:
                current_node.next = Node(data, current_node.next)
                return
            current_node = current_node.next

    def remove_by_value(self, value):
        if self.head.data == value:
            self.head = self.head.next
            return

        current_node = self.head
        while (current_node.next):
            if current_node.next.data == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    # I do not think these would be useful in practice. If you want an indexed structure, then use a array/list
    def insert_at_index(self, index, data):
        size = len(self)
        if index < 0 or index > size:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.head = Node(data, self.head)

        idx = 0
        current_node = self.head
        while (idx < size):
            if idx == index - 1:
                current_node.next = Node(data, current_node.next)
                return
            current_node = current_node.next
            idx += 1

    def remove_at_index(self, index):
        size = len(self)
        if index < 0 or index >= size:
            raise IndexError(f"Index of out bounds: Index: {index}")

        if index == 0:
            self.head = self.head.next
            return

        idx = 0
        current_node = self.head
        while (idx < size):
            if idx == index - 1:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
            idx += 1

    def __repr__(self):
        values = []
        if self.head:
            current_node = self.head
            while (current_node):
                if (current_node.next):
                    values.append(current_node.data)
                else:
                    values.append(current_node.data)
                current_node = current_node.next
            return "".join(str(values))
        else:
            return "".join(values)

    def reverse(self):
        if self.head:
            last_processed = None
            next_node_to_process = None
            current_node = self.head
            while (current_node):
                next_node_to_process = current_node.next

                current_node.next = last_processed

                last_processed = current_node
                current_node = next_node_to_process
            self.head = last_processed
        else:
            raise ValueError("List is empty")
