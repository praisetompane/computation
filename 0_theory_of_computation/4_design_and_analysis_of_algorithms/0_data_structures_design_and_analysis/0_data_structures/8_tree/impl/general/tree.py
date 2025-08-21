class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def _get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level

    def print_tree_iterative(self, indentation_space=" "):
        space = indentation_space * self._get_level() * 2
        prefix = space + "|__" if self.parent else ""
        print(f"{prefix} {self.data}")

        for child in self.children:
            child.print_tree_iterative()

    def print_tree_recursive(self, indentation_space=" "):
        prefix = "|__" if self.parent else ""
        print(f"{indentation_space if self.parent else ""} {prefix} {self.data}")

        for child in self.children:
            child.print_tree_recursive(indentation_space * 2)


if __name__ == "__main__":
    root = Node("Electronics")

    laptops = Node("Laptops")
    laptops.add_child(Node("Apple"))
    laptops.add_child(Node("HP"))
    laptops.add_child(Node("Dell"))
    root.add_child(laptops)

    tv = Node("TV")
    tv.add_child(Node("Samsung"))
    tv.add_child(Node("Panasonic"))
    tv.add_child(Node("LG"))
    root.add_child(tv)

    cell_phone = Node("Cellphone")
    cell_phone.add_child(Node("Samsung"))
    cell_phone.add_child(Node("Apple"))
    cell_phone.add_child(Node("LG"))
    root.add_child(cell_phone)

    root.print_tree_recursive()
    print("\n")
    root.print_tree_iterative()
