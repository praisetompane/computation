from impl.general.tree import Node


def test_general_tree():
    root = Node("Electronics")

    laptops = Node("Laptops")
    laptops.add_child(Node("Apple"))
    laptops.add_child(Node("HP"))
    laptops.add_child(Node("Dell"))
    root.add_child(laptops)

    tv = Node("TV")
    tv.add_child(Node("Samsung"))
    tv.add_child(Node("Panasonic"))
    tv.add_child(Node("LG"))
    root.add_child(tv)

    cell_phone = Node("Cellphone")
    cell_phone.add_child(Node("Samsung"))
    cell_phone.add_child(Node("Apple"))
    cell_phone.add_child(Node("LG"))
    root.add_child(cell_phone)

    root.print_tree_recursive()
    print("\n")
    root.print_tree_iterative()
