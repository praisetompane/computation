from impl.general_tree.tree import GeneralTreeNode


class LocationDirectoryNode(GeneralTreeNode):
    def __init__(self, location) -> None:
        super().__init__(location)

    def add_child(self, child) -> None:
        return super().add_child(LocationDirectoryNode(child))

    def print_tree(self, level):
        prefix = f"{' ' * self.get_level() * 2}"
        print(f"{prefix} {'|__' if self.parent else ''} {self.data}")

        for child in self.children:
            if child.get_level() <= level:
                child.print_tree(level)
