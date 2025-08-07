from insertion_sort import sort


def test_insertion_sort():
    assert sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert sort([4, 2, 3, 1, 5]) == [1, 2, 3, 4, 5]
    assert sort([]) == []
    assert sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
