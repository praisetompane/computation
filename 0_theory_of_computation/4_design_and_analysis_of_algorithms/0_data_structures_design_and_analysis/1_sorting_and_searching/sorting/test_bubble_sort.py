from bubble_sort.impl.sort import sort


def test_sort_numbers():
    assert sort([4, 2, 3, 1, 5]) == [1, 2, 3, 4, 5]
    assert sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert sort([]) == []

def test_sort_character_arrays():
    assert sort(["a", "b", "c", "d", "e"]) == ["a", "b", "c", "d", "e"]
    assert sort(['e', 'd', 'c', 'b', 'a']) == ["a", "b", "c", "d", "e"]

def test_sort_strings():
    assert sort(['orange', 'banana', 'apple']) == ["apple", "banana", "orange"]
