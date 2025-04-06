from doubly.node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        """Calculates the length of the list.

        Returns:
            int: Number of elements in list
        """
        length = 0
        iterator = self.head
        while (iterator):
            length += 1
            iterator = iterator.next
        return length

    def __repr__(self):
        """Return string representation to be used by Python's `repr`

        Returns:
            str: String representation of the list.
        """
        if self.head == None:
            return "".join([])
        else:
            values = []
            iterator = self.head
            while (iterator):
                values.append(str(iterator.data))
                iterator = iterator.next
            return "".join(str(values))

    def insert_at_top(self, data):
        """Inserts a value to the top of the list

        Args:
            data (Any): Data to be inserted.
        """
        new_head = Node(data, None, self.head)
        if self.head == None:
            self.head = new_head
        else:
            self.head.prev = new_head
            self.head = new_head

    def insert_at_end(self, data):
        """Insert a value to the end of the list.

        Args:
            data (Any): Data to be inserted at the end.
                        Use `insert_values` to insert a collection of values.
        """
        if self.head == None:
            self.head = Node(data)
        else:
            iterator = self.head
            while (iterator.next):
                iterator = iterator.next

            iterator.next = Node(data, iterator)

    def insert_values(self, data):
        """ Insert values of a sequence to the end of the list.

        Args:
            values (Sequence): Sequence data to be inserted
        """
        def _insert(start_index):
            iterator = self.head
            # move pointer to the last node
            while (iterator.next):
                iterator = iterator.next

            idx = start_index
            while (idx < len(data)):
                iterator.next = Node(data[idx], iterator)
                iterator = iterator.next
                idx += 1

        if self.head == None:
            self.head = Node(data[0])
            _insert(1)
        else:
            _insert(0)

    def insert_after_value(self, value, data):
        """Insert a value after the supplied @predicate_value

        Args:
            predicate_value (Any): Value to to insert after.
            data (Any): Data to insert.

        Raises:
            IndexError: The list is empty
        """
        if self.head == None:
            raise IndexError("List is empty")

        iterator = self.head
        while (iterator):
            if iterator.data == value:
                iterator.next = Node(data, iterator, iterator.next)
                return
            iterator = iterator.next

    def remove_from_top(self):
        """Removes and returns value at the head of the list.

        Raises:
            ValueError: List is empty

        Returns:
            Any: Data in the head of the list.
        """
        if self.head:
            node = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return node.data
        else:
            raise ValueError("List is empty")

    def remove_by_value(self, value):
        """Remove a specific @value from the list.

        Args:
            value (Any): Value to be removed.
        """
        if self.head == None:
            raise IndexError("List is empty")

        if self.head.data == value:
            self.head = self.head.next
            return

        iterator = self.head
        while (iterator.next):
            if iterator.next.data == value:
                iterator.next = iterator.next.next
                if iterator.next is not None:
                    iterator.next.prev = iterator
                return
            iterator = iterator.next

    def reverse(self):
        """Reverse the list order.

        Raises:
            ValueError: List is empty
        """
        if self.head == None:
            raise ValueError("List is empty")

        last_processed = None
        iterator = self.head
        next_node_to_process = None
        while (iterator):
            next_node_to_process = iterator.next

            iterator.next = last_processed
            iterator.prev = next_node_to_process

            last_processed = iterator
            iterator = next_node_to_process

        self.head = last_processed

    def print_forward(self) -> None:
        """Print list in forward order
        """
        if self.head == None:
            print("[]")
            return

        iterator = self.head
        while (iterator):
            print(iterator.data)
            iterator = iterator.next

    def print_backward(self) -> None:
        """Print list in backwards order
        """
        if self.head == None:
            print("[]")
            return

        iterator = self.head
        while (iterator):
            print(iterator.data)
            iterator = iterator.prev

    # I do not think these would be useful in practice. If you want an indexed structure, then use a array/list
    # They are for demonstration and practice.
    def insert_at_index(self, index, data) -> None:
        """Insert data at an index.

        Args:
            index (int): Index to insert the data at.
            data (Any): Data to insert.

        Raises:
            IndexError: Index out of bounds
        """
        size = len(self)
        if index < 0 or index > size:
            raise IndexError("Index out of bounds")

        if self.head == None and index != 0:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.head = Node(data, self.head, self.head.next)
            return

        iterator = self.head
        idx = 0
        while (iterator):
            if idx == index - 1:
                node = Node(data, iterator, iterator.next)
                if iterator.next:
                    iterator.next.prev = node
                iterator.next = node
                return
            idx += 1
            iterator = iterator.next

    def remove_at_index(self, index):
        """Remove value at an index.

        Args:
            index (int): Index to remove.

        Raises:
            IndexError: Index of out bounds
        """
        if index < 0 and index >= len(self):
            raise IndexError("List is empty")

        idx = 0
        iterator = self.head
        while (iterator):
            if idx == index - 1:
                iterator.next = iterator.next.next
                if iterator.next is not None:
                    iterator.next.prev = iterator
            idx += 1
            iterator = iterator.next
