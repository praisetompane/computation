from doubly.linked_list import LinkedList
from doubly.node import Node


def test_construction():
    linked_list = LinkedList()
    assert linked_list.head == None


def test_length():
    linked_list = LinkedList()
    assert len(linked_list) == 0

    linked_list.insert_at_top(1)
    print(f"{len(linked_list)=}")
    assert len(linked_list) == 1


def test_string_representation():
    linked_list = LinkedList()
    linked_list.insert_values(["banana", "mango", "grapes", "orange"])

    assert repr(linked_list) == "['banana', 'mango', 'grapes', 'orange']"


def test_insert_at_top():
    linked_list = LinkedList()
    linked_list.insert_at_top(1)
    linked_list.insert_at_top(2)

    assert linked_list.head.data == 2
    assert linked_list.head.next.data == 1


def test_insert_at_end():
    linked_list = LinkedList()
    linked_list.insert_values(["banana", "mango", "grapes", "orange"])

    linked_list.insert_at_end("pie")
    assert linked_list.head.next.next.next.next.data == "pie"


def test_insert_values():
    linked_list = LinkedList()
    linked_list.insert_values(["banana", "mango", "grapes", "orange"])

    assert linked_list.head.data == "banana"
    assert linked_list.head.next.data == "mango"
    assert linked_list.head.next.next.data == "grapes"
    assert linked_list.head.next.next.next.data == "orange"


def insert_after_value():
    linked_list = LinkedList()
    linked_list.insert_at_top(1)
    linked_list.insert_at_end(5)

    linked_list.insert_after_value(5, "five")

    assert linked_list.head.next.next.data == "five"


def test_remove_from_top():
    linked_list = LinkedList()
    linked_list.insert_at_top(1)
    linked_list.insert_at_top(2)

    data = linked_list.remove_from_top()
    assert data == 2
    assert linked_list.head.data == 1

    data = linked_list.remove_from_top()
    assert data == 1
    assert linked_list.head == None

    try:
        linked_list.remove_from_top()
    except ValueError as e:
        assert e.args == ("List is empty", )


def test_remove_by_value():
    linked_list = LinkedList()
    linked_list.insert_values(["banana", "mango", "grapes", "orange"])

    linked_list.remove_by_value("grapes")
    assert linked_list.head.data == "banana"
    assert linked_list.head.next.data == "mango"
    assert linked_list.head.next.next.data == "orange"


def test_reverse():
    linked_list = LinkedList()
    linked_list.insert_values([1, 2, 3, 4])
    linked_list.reverse()

    assert linked_list.head.data == 4
    assert linked_list.head.next.data == 3
    assert linked_list.head.next.next.data == 2
    assert linked_list.head.next.next.next.data == 1


def test_insert_at_index():
    linked_list = LinkedList()
    linked_list.insert_values(["banana", "mango", "grapes", "orange"])

    linked_list.insert_at_index(2, "pie")
    assert linked_list.head.data == "banana"
    assert linked_list.head.next.data == "mango"
    assert linked_list.head.next.next.data == "pie"
    assert linked_list.head.next.next.next.data == "grapes"
    assert linked_list.head.next.next.next.next.data == "orange"


def test_remove_at_index():
    linked_list = LinkedList()
    linked_list.insert_values(["banana", "mango", "grapes", "orange"])

    linked_list.remove_at_index(2)
    assert linked_list.head.data == "banana"
    assert linked_list.head.next.data == "mango"
    assert linked_list.head.next.next.data == "orange"
