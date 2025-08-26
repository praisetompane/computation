from impl.binary_tree.binary_search_tree.tree import BinarySearchTreeNode


def _build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for e in elements[1:]:
        root.add_child(e)
    return root


numbers = [17, 4, 1, 20, 9, 23, 18, 34]
root = _build_tree(numbers)


def test_in_order_traversal():
    assert sorted(numbers) == root.in_order_traversal()


def test_post_order_traversal():
    assert [1, 9, 4, 18, 34, 23, 20, 17] == root.post_order_traversal()


def test_pre_order_traversal():
    assert [17, 4, 1, 9, 20, 18, 23, 34] == root.pre_order_traversal()


def test_search():
    assert 23 == root.search(23)


def test_print_tree():
    root.print_tree()


def test_find_max():
    assert 34 == root.find_max()


def test_find_min():
    assert 1 == root.find_min()


def test_calculate_sum():
    assert sum(numbers) == root.calculate_sum()


if __name__ == "__main__":
    test_in_order_traversal()
    test_search()
    test_print_tree()
    test_find_max()
    test_find_min()
    test_calculate_sum()
    test_post_order_traversal()
    test_pre_order_traversal()
