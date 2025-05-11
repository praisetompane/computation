from hash_table import HashTable

hash_table = HashTable()


def test_calculate_hash():
    assert hash_table._calculate_hash("march 6") == 609


def test_adding_an_item():
    hash_table["march 6"] = 90
    assert hash_table["march 6"] == 90


def test_updating_an_item():
    hash_table["march 6"] = 91
    assert hash_table["march 6"] == 91
