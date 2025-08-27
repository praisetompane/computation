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


def test_post_order_traversal():
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    root = _build_tree(numbers)
    assert [1, 9, 4, 18, 34, 23, 20, 17] == root.post_order_traversal()


def test_pre_order_traversal():
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    root = _build_tree(numbers)
    assert [17, 4, 1, 9, 20, 18, 23, 34] == root.pre_order_traversal()


def test_search():
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    root = _build_tree(numbers)
    assert 23 == root.search(23)


def test_print_tree():
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    root = _build_tree(numbers)
    root.print_tree()


def test_find_max():
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    root = _build_tree(numbers)
    assert 34 == root.find_max()


def test_find_min():
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    root = _build_tree(numbers)
    assert 1 == root.find_min()


def test_calculate_sum():
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    root = _build_tree(numbers)
    assert sum(numbers) == root.calculate_sum()


def test_delete_leaf():
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    root = _build_tree(numbers)
    root.delete(1)
    assert [9, 4, 18, 34, 23, 20, 17] == root.post_order_traversal()

def test_delete_subtree_with_only_left_leaf():
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 8]
    root = _build_tree(numbers)
    root.delete(9)
    assert [1, 4, 8, 17, 18, 20, 23, 34] == root.in_order_traversal()

def test_delete_leaf_subtree_with_only_right_leaft():
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    root = _build_tree(numbers)
    root.delete(23)
    assert [1, 4, 9, 17, 18, 20, 34] == root.in_order_traversal()

if __name__ == "__main__":
    test_in_order_traversal()
    test_search()
    test_print_tree()
    test_find_max()
    test_find_min()
    test_calculate_sum()
    test_post_order_traversal()
    test_pre_order_traversal()
    test_delete_leaf()
    test_delete_subtree_with_only_left_leaf()
    test_delete_leaf_subtree_with_only_right_leaft()