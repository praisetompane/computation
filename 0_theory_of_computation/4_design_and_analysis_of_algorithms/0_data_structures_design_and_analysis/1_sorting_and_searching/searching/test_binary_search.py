from binary_search.impl.binary_search import *


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_binary_search_recursive():
    assert binary_search_recursive(1, numbers) == 0
    assert binary_search_recursive(0, numbers) == -1
    assert binary_search_recursive(10, numbers) == 9


def test_binary_search_iterative():
    assert binary_search_iterative(1, numbers) == 0
    assert binary_search_iterative(0, numbers) == -1
    assert binary_search_iterative(10, numbers) == 9


def test_binary_search_iterative_mutate_search_space():
    assert binary_search_iterative_mutate_search_space(1, numbers) == 0
    assert binary_search_iterative_mutate_search_space(0, numbers) == -1
    assert binary_search_iterative_mutate_search_space(10, numbers) == 1
