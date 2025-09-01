from binary_search.use_cases.find_occurences import find_occurence_indices


def test_find_occurence_indices():
    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    assert find_occurence_indices(15, numbers) == [6, 5, 7]
    assert find_occurence_indices(0, numbers) == []


test_find_occurence_indices()
