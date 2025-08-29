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

    def delete(self, data):
        def _lift_right_sub_tree():
            min_value = self.right.find_min()
            self.data = min_value
            # remove/delete the old min_value we just duplicated
            self.right = self.right.delete(min_value)

        def _lift_left_sub_tree():
            max_value = self.left.find_max()
            self.data = max_value
            # remove/delete the old max_value we just duplicated
            self.left = self.left.delete(max_value)

        if data < self.data:
            # left subtree
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            # right subtree
            if self.right:
                self.right = self.right.delete(data)
        else:
            # actual deletion happens here and propagated up the call/recursion stack
            def is_leaf(node):
                return node.left is None and node.right is None

            # deleting from a binary search tree has these 3 main cases
            # 1. handle leaf nodes
            if is_leaf(self):
                return None
            # 2. handle nodes with a single leaf node child
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            # 3. handle full subtree nodes using right subtree.
            # remark: you can do the same sing the left subtree
            _lift_right_sub_tree()
            # _lift_left_sub_tree()

        return self

    def print_tree(self) -> None:
        def render_child_tree(tree):
            return f"{self.left.data if self.left else None}, {self.right.data if self.right else None}"

        print(f"{self.data}, {render_child_tree(self)}")
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()
