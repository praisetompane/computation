from typing import List


class BinarySearchTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, value) -> None:
        """Add @value to tree.

        Args:
            value (_type_): input value.

        Performance:
            Time = log(𝑁)
        """
        if self.data == value:
            return

        if value < self.data:
            if self.left:
                self.left.add_child(value)
            else:
                self.left = BinarySearchTreeNode(value)
        else:
            if self.right:
                self.right.add_child(value)
            else:
                self.right = BinarySearchTreeNode(value)

    def in_order_traversal(self) -> List:
        """Traverses the whole tree in left, root, right order

        Returns:
            List: Ascending order list

        Performance:
            Time = 𝑂(𝑁)
        """
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def search(self, value):
        """Searches for @value in tree

        Args:
            value: value to search for

        Performance:
            Time = 𝑂(log(𝑁))
        """
        if self.data == value:
            return self.data

        if value < self.data:
            if self.left:
                return self.left.search(value)
        else:
            if self.right:
                return self.right.search(value)

        return None

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def calculate_sum(self):
        total = 0
        if self.left:
            total += self.left.calculate_sum()

        total += self.data

        if self.right:
            total += self.right.calculate_sum()

        return total

    def print_tree(self) -> None:
        def render_child_tree(tree):
            return f"{self.left.data if self.left else None}, {self.right.data if self.right else None}"

        print(f"{self.data}, {render_child_tree(self)}")
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()
