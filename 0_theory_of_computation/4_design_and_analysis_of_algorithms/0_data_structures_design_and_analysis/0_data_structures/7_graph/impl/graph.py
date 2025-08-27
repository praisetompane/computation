class Graph(object):
    nodes = []
    size = 0

    def __init__(self, size):
        self.size = size

    def add_node(self, node):
        self.nodes.append(node)

    def __str__(self):
        " ".join(str(self.nodes[i]) for i in range(0, self.size) )


class Node(object):
    def __init__(self, value):
        self.value = value
        self.nodes = []

    def add_neighbour(self, node):
        self.nodes.append(node)

    def __str__(self):
        return str(self.value)


def main():
    house_hold_count = 11
    town = Graph(house_hold_count)
    for i in range(0, house_hold_count):
        print("adding" + str(i))
        node = Node(i)
        if i < house_hold_count:
            node.add_neighbour(i + 1)
            node.add_neighbour(i - 1)
            town.add_node(node)
        town.add_node(node)

    print(town)


if __name__ == "__main__":
    main()
