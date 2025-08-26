from typing import Self


class GeneralTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child) -> Self:
        child.parent = self
        self.children.append(child)
        return child

    def get_level(self) -> int:
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level

    def print_tree(self) -> None:
        indentation_space = " " * self.get_level() * 2
        prefix = f"{indentation_space} |__" if self.parent else ""
        print(f"{prefix} {self.data}")

        for child in self.children:
            child.print_tree()

    def print_tree_accumulator(self, indentation_space=" ") -> None:
        prefix = f"{indentation_space} |__" if self.parent else ""
        print(f"{prefix} {self.data}")

        for child in self.children:
            child.print_tree_accumulator(indentation_space * 2)
