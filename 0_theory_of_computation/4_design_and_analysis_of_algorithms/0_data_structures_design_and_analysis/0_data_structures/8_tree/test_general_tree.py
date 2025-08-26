from impl.general_tree.tree import GeneralTreeNode


def test_general_tree():
    root = GeneralTreeNode("Electronics")

    laptops = GeneralTreeNode("Laptops")
    laptops.add_child(GeneralTreeNode("Apple"))
    laptops.add_child(GeneralTreeNode("HP"))
    laptops.add_child(GeneralTreeNode("Dell"))
    root.add_child(laptops)

    tv = GeneralTreeNode("TV")
    tv.add_child(GeneralTreeNode("Samsung"))
    tv.add_child(GeneralTreeNode("Panasonic"))
    tv.add_child(GeneralTreeNode("LG"))
    root.add_child(tv)

    cell_phone = GeneralTreeNode("Cellphone")
    cell_phone.add_child(GeneralTreeNode("Samsung"))
    cell_phone.add_child(GeneralTreeNode("Apple"))
    cell_phone.add_child(GeneralTreeNode("LG"))
    root.add_child(cell_phone)

    root.print_tree_accumulator()
    print("\n")
    root.print_tree()


if __name__ == "__main__":
    test_general_tree()
