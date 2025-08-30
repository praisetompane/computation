from use_cases.general_tree.location_directory import LocationDirectoryNode


def test_location_tree():
    root = LocationDirectoryNode("Global")

    india = root.add_child("India")
    usa = root.add_child("U.S.A")

    gujarat = india.add_child("Gujarat")
    karnataka = india.add_child("Karnataka")

    new_jersey = usa.add_child("New Jersey")
    carlifonia = usa.add_child("Carlifonia")

    ahmedabad = gujarat.add_child("Ahmedabad")
    baroda = gujarat.add_child("Baroda")

    bangluru = karnataka.add_child("Bangluru")
    mysore = karnataka.add_child("Mysore")

    princeton = new_jersey.add_child("Princeton")
    trenton = new_jersey.add_child("Trenton")

    san_francisco = carlifonia.add_child("San Francisco")
    mountain_view = carlifonia.add_child("Mountain View")
    palo_alto = carlifonia.add_child("Palo Alto")

    root.print_tree(0)
    print("\n")

    root.print_tree(1)
    print("\n")

    root.print_tree(2)
    print("\n")

    root.print_tree(3)
    print("\n")


if __name__ == "__main__":
    test_location_tree()
