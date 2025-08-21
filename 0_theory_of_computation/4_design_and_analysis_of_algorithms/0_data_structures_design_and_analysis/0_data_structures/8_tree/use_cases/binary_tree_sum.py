class Node:
    data = None
    left = None
    right = None

    def __init__(self, data=None):
        self.data = data

    def sum(self):
        def _sum(root):
            if root is None:
                return 0
            else:
                total = _sum(root.left)
                total += root.data
                total += _sum(root.right)
                return total

        return _sum(self)


def main():
    root = Node(7)
    root.left = Node(5)
    root.right = Node(8)

    root.left.left = Node(3)
    root.right.right = Node(6)

    print(root.sum())


if __name__ == "__main__":
    main()
