from impl.general.tree import Node


class LocationTreeNode(Node):
    def __init__(self, location) -> None:
        super().__init__(location)

    def print_tree(self, level):
        prefix = f"{' ' * self.get_level() * 2}"
        print(f"{prefix} {'|__' if self.parent else ''} {self.data}")

        for child in self.children:
            if child.get_level() <= level:
                child.print_tree(level)
