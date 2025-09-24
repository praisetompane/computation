from binary_search.use_cases.find_occurences import find_occurence_indices


def test_find_occurence_indices_on_sorted_list():
    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    assert find_occurence_indices(15, numbers) == [6, 5, 7]
    assert find_occurence_indices(0, numbers) == []


def test_find_occurence_indices_on_empty_list():
    numbers = []
    assert find_occurence_indices(0, numbers) == []


def test_find_occurence_indices_on_unsorted_list():
    numbers = [15, 1, 17, 21, 34, 56, 4, 6, 15, 15, 34, 9, 11]
    assert find_occurence_indices(15, numbers) == [6, 5, 7]
    assert find_occurence_indices(34, numbers) == [10, 11]
