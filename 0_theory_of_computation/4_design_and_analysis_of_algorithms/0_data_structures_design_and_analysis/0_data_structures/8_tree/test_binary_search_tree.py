from impl.binary_tree.binary_search_tree.tree import BinarySearchTreeNode


def _build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for e in elements[1:]:
        root.add_child(e)
    return root


def test_in_order_traversal():
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    root = _build_tree(numbers)
    assert sorted(numbers) == root.in_order_traversal()


def test_search():
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    root = _build_tree(numbers)
    assert 23 == root.search(23)


def test_print_tree():
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    root = _build_tree(numbers)
    root.print_tree()


if __name__ == "__main__":
    test_in_order_traversal()
    test_search()
    test_print_tree()
