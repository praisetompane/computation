from singly.node import Node
from collections.abc import Sequence
from typing import Any


class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self) -> int:
        """Calculates the length of the list.

        Returns:
            int: Number of elements in list
        """
        length = 0
        iterator = self.head
        while iterator:
            length = length + 1
            iterator = iterator.next
        return length

    def __repr__(self) -> str:
        """Return string representation to be used by Python's `repr`.

        Returns:
            str: String representation of the list.
        """
        if self.head is None:
            return "".join([])
        else:
            values = []
            iterator = self.head
            while iterator:
                if iterator.next:
                    values.append(iterator.data)
                else:
                    values.append(iterator.data)
                iterator = iterator.next
            return "".join(str(values))

    def _get_last_node(self) -> Node:
        """Returns last node in the list.

        Returns:
            Node: Last node in the list.
        """
        iterator = self.head
        while iterator.next:
            iterator = iterator.next

        return iterator

    def insert_at_top(self, data: Any) -> None:
        """Inserts a value to the top of the list.

        Args:
            data (Any): Data to be inserted.
        """
        self.head = Node(data, self.head)

    def insert_at_end(self, data: Any) -> None:
        """Insert a value to the end of the list.

        Args:
            data (Any): Data to be inserted at the end.
                        Use `insert_values` to insert a collection of values.
        """
        node = Node(data)
        if self.head:
            iterator = self._get_last_node()
            iterator.next = node
        else:
            self.head = node

    def insert_values(self, values: Sequence) -> None:
        """Insert values of a sequence to the end of the list.

        Args:
            values (Sequence): Sequence data to be inserted

        # O(N). N = length of current values in list
        """

        def _insert_values(start_index):
            # O(M). M = length of new values
            iterator = self._get_last_node()
            idx = start_index
            while idx < len(values):
                iterator.next = Node(values[idx])
                iterator = iterator.next
                idx += 1

        if self.head is None:
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

    def insert_after_value(self, predicate_value: Any, data: Any) -> None:
        """Insert a value after the supplied @predicate_value.

        Args:
            predicate_value (Any): Value to to insert after.
            data (Any): Data to insert.

        Raises:
            IndexError: The list is empty
        """
        if self.head is None:
            raise IndexError("The list is empty")

        iterator = self.head
        while iterator:
            if iterator.data == predicate_value:
                iterator.next = Node(data, iterator.next)
                return
            iterator = iterator.next

    def remove_from_top(self) -> Any:
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

    def remove_by_value(self, value: Any) -> None:
        """Remove a specific @value from the list.

        Args:
            value (Any): Value to be removed.
        """
        if self.head.data == value:
            self.head = self.head.next
            return

        iterator = self.head
        while iterator.next:
            if iterator.next.data == value:
                iterator.next = iterator.next.next
                return
            iterator = iterator.next

    def reverse(self) -> None:
        """Reverse the list order.

        Raises:
            ValueError: List is empty
        """
        if self.head:
            last_processed = None
            next_node_to_process = None
            iterator = self.head
            while iterator:
                next_node_to_process = iterator.next

                # NB: The key is here. we set a node's successor(i.e. next) value to be its predecessor. which is what reversal means.
                # The rest is housekeeping to remember who was next and was the previous.
                iterator.next = last_processed

                last_processed = iterator
                iterator = next_node_to_process
            self.head = last_processed
        else:
            raise ValueError("List is empty")

    # I do not think these would be useful in practice. If you want an indexed structure, then use a array/list
    # They are for demonstration and practice.
    def insert_at_index(self, index: int, data: Any) -> None:
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

        if index == 0:
            self.head = Node(data, self.head)

        idx = 0
        iterator = self.head
        while idx < size:
            if idx == index - 1:
                iterator.next = Node(data, iterator.next)
                return
            iterator = iterator.next
            idx += 1

    def remove_at_index(self, index: int) -> None:
        """Remove value at an index.

        Args:
            index (int): Index to remove.

        Raises:
            IndexError: Index of out bounds
        """
        size = len(self)
        if index < 0 or index >= size:
            raise IndexError(f"Index of out bounds: Index: {index}")

        if index == 0:
            self.head = self.head.next
            return

        idx = 0
        iterator = self.head
        while idx < size:
            if idx == index - 1:
                iterator.next = iterator.next.next
                return
            iterator = iterator.next
            idx += 1
