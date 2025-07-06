from open_addressing.linear_probing.hash_table import HashTableLinearProbing


def test_calculate_hash():
    hash_table = HashTableLinearProbing()
    assert hash_table._calculate_hash("march 6") == 609


def test_adding_an_item():
    hash_table = HashTableLinearProbing()
    hash_table["march 6"] = 90
    assert hash_table["march 6"] == 90


def test_adding_an_item_to_full_hash_table():
    hash_table = HashTableLinearProbing()
    for i in range(0, hash_table._MAX):
        hash_table._items[i] = (str(i), i)

    hash_table["march 6"] = 90
    assert hash_table["march 6"] == 90


def test_updating_an_item():
    hash_table = HashTableLinearProbing()
    hash_table["march 6"] = 90
    assert hash_table["march 6"] == 90

    hash_table["march 6"] = 91
    assert hash_table["march 6"] == 91


def test_handle_collisions_works_correctly_when_an_element_already_exists():
    hash_table = HashTableLinearProbing()
    expected_index = 609
    expected_existing_item = ("key", "Already Existing Item")
    hash_table._items[expected_index] = expected_existing_item

    hash_table["march 6"] = 90
    assert hash_table["march 6"] == 90
    assert hash_table._items[609] == expected_existing_item
    assert hash_table._items[610] == ("march 6", 90)


def test_deleting_an_item():
    hash_table = HashTableLinearProbing()
    hash_table["march 7"] = 90
    assert hash_table["march 7"] == 90

    del hash_table["march 7"]
    assert hash_table["march 7"] is None


def test_deleting_an_item_in_a_linear_probed_index():
    hash_table = HashTableLinearProbing()
    expected_index = 609
    expected_existing_item = ("key", "Already Existing Item")
    hash_table._items[expected_index] = expected_existing_item

    hash_table["march 6"] = 90
    assert hash_table["march 6"] == 90
    assert hash_table._items[610] == ("march 6", 90)

    del hash_table["march 6"]
    assert hash_table._items[610] is None


if __name__ == "__main__":
    test_adding_an_item_to_full_hash_table()
