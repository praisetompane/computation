from singly.node import Node


def test_construction():
    n = Node(0)
    node = Node(1, n)

    assert node.data == 1
    assert node.next == n


def test_representation():
    node = Node(3)
    assert repr(node) == "3"
