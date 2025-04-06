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
        current_node = self.head
        while current_node:
            length = length + 1
            current_node = current_node.next
        return length

    def __repr__(self) -> str:
        """Return string representation to be used by Python's `repr`

        Returns:
            str: String representation of the list.
        """
        if self.head == None:
            return "".join([])
        else:
            values = []
            current_node = self.head
            while current_node:
                if current_node.next:
                    values.append(current_node.data)
                else:
                    values.append(current_node.data)
                current_node = current_node.next
            return "".join(str(values))

    def insert_at_top(self, data: Any) -> None:
        """Inserts a value to the top of the list

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
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node
        else:
            self.head = node

    def insert_values(self, values: Sequence) -> None:
        """Insert values of a sequence to the end of the list.

        Args:
            values (Sequence): Sequence data to be inserted
        """

        # O(N). N = length of current values in list
        def _insert_values(start_index):
            # O(M). M = length of new values
            current_node = self.head
            while current_node.next:
                current_node = current_node.next

            idx = start_index
            while idx < len(values):
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

    def insert_after_value(self, predicate_value: Any, data: Any) -> None:
        """Insert a value after the supplied @predicate_value

        Args:
            predicate_value (Any): Value to to insert after.
            data (Any): Data to insert.

        Raises:
            IndexError: The list is empty
        """
        if self.head == None:
            raise IndexError("The list is empty")

        current_node = self.head
        while current_node:
            if current_node.data == predicate_value:
                current_node.next = Node(data, current_node.next)
                return
            current_node = current_node.next

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

        current_node = self.head
        while current_node.next:
            if current_node.next.data == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def reverse(self) -> None:
        """Reverse the list order.

        Raises:
            ValueError: List is empty
        """
        if self.head:
            last_processed = None
            next_node_to_process = None
            current_node = self.head
            while current_node:
                next_node_to_process = current_node.next

                current_node.next = last_processed

                last_processed = current_node
                current_node = next_node_to_process
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
        current_node = self.head
        while idx < size:
            if idx == index - 1:
                current_node.next = Node(data, current_node.next)
                return
            current_node = current_node.next
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
        current_node = self.head
        while idx < size:
            if idx == index - 1:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
            idx += 1
