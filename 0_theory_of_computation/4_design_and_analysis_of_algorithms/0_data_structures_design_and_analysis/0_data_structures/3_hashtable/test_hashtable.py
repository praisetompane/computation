from hashtable import HashTable


def test_calculate_hash():
    hash_table = HashTable()
    assert hash_table._calculate_hash("march 6") == 609


def test_adding_an_item():
    hash_table = HashTable()
    hash_table["march 6"] = 90
    assert hash_table["march 6"] == 90


def test_updating_an_item():
    hash_table = HashTable()
    hash_table["march 6"] = 90
    assert hash_table["march 6"] == 90

    hash_table["march 6"] = 91
    assert hash_table["march 6"] == 91


def test_handle_collisions_works_correctly_when_an_element_already_exists():
    hash_table = HashTable()
    expected_index = 609
    expected_existing_item = ("key", "Already Existing Item")
    hash_table._items[expected_index].append(expected_existing_item)

    hash_table["march 6"] = 90
    assert hash_table["march 6"] == 90
    assert hash_table._items[expected_index] == [
        expected_existing_item,
        ("march 6", 90),
    ]


def test_updating_an_item_works_correctly_in_a_chain():
    hash_table = HashTable()
    index = 410
    existing_items = [
        ("key 1", ["Already Existing Item 1"]),
        ("key 2", "Already Existing Item 2"),
    ]
    hash_table._items[index] = existing_items

    hash_table["key 1"] = ["Already Existing Item 3", "Already Existing Item 4"]
    expected_updated_items = [
        ("key 1", ["Already Existing Item 3", "Already Existing Item 4"]),
        ("key 2", "Already Existing Item 2"),
    ]
    assert hash_table._items[index] == expected_updated_items


def test_deleting_an_item():
    hash_table = HashTable()
    hash_table["march 7"] = 90
    assert hash_table["march 7"] == 90

    del hash_table["march 7"]
    assert hash_table["march 7"] is None


def test_deleting_an_item_in_a_chain():
    hash_table = HashTable()
    index = 411
    existing_items = [
        ("key 2", ["Existing Item 2", "Existing Item 3"]),
        ("key 1", "Existing Item 1"),
    ]
    hash_table._items[index] = existing_items

    del hash_table["key 2"]

    expected_items = [("key 1", "Existing Item 1")]
    assert hash_table._items[index] == expected_items


if __name__ == "__main__":
    test_updating_an_item_works_correctly_in_a_chain()
