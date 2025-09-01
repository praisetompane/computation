from linear_search.impl.linear_search import *


def test_linear_search():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert linear_search(8, numbers) == 7
    assert linear_search(11, numbers) is None


def test_linear_search_enumerate():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert linear_search_enumerate(8, numbers) == 7
    assert linear_search_enumerate(11, numbers) is None
