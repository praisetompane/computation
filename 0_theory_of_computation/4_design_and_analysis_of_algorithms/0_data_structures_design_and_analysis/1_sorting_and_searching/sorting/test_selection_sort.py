from selection_sort.impl.sort import sort, sort_explicit, SORT_DIRECTION


def test_sort():
    assert sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert sort([4, 2, 3, 1, 5]) == [1, 2, 3, 4, 5]
    assert sort([]) == []
    assert sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_bubble_sort_ascending():
    assert sort_explicit([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert sort_explicit([4, 2, 3, 1, 5]) == [1, 2, 3, 4, 5]
    assert sort_explicit([]) == []
    assert sort_explicit([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_bubble_sort_descending():
    assert sort_explicit([3, 2, 1, 4, 5], SORT_DIRECTION.DESC) == [5, 4, 3, 2, 1]
    assert sort_explicit([5, 4, 3, 2, 1], SORT_DIRECTION.DESC) == [5, 4, 3, 2, 1]
    assert sort_explicit([]) == []
    assert sort_explicit([1, 2, 3, 4, 5], SORT_DIRECTION.DESC) == [5, 4, 3, 2, 1]
