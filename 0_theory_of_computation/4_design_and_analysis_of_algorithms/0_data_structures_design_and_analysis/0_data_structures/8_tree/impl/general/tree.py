class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level

    def print_tree(self):
        indentation_space = " " * self.get_level() * 2
        prefix = f"{indentation_space} |__" if self.parent else ""
        print(f"{prefix} {self.data}")

        for child in self.children:
            child.print_tree()

    def print_tree_accumulator(self, indentation_space=" "):
        prefix = f"{indentation_space} |__" if self.parent else ""
        print(f"{prefix} {self.data}")

        for child in self.children:
            child.print_tree_accumulator(indentation_space * 2)
