from impl.general.tree import Node


class Personnel:
    def __init__(self, designation, name) -> None:
        self.designation = designation
        self.name = name

    def __str__(self) -> str:
        return f"{self.name} ({self.designation})"


class OrganizationChartNode(Node):
    def __init__(self, person) -> None:
        super().__init__(person)

    def print_tree(self, data_part):
        indentation_space = " " * self.get_level() * 2
        prefix = f"{indentation_space} |__" if self.parent else ""
        tree_value = ""

        match data_part:
            case "designation":
                tree_value = f"{prefix} {self.data.designation}"
            case "name":
                tree_value = f"{prefix} {self.data.name}"
            case "both":
                tree_value = f"{prefix} {str(self.data)}"

        print(tree_value)
        for child in self.children:
            child.print_tree(data_part)
