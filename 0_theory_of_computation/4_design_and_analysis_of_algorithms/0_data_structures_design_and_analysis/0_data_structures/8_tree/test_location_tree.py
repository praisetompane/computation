from use_cases.general.location_tree import LocationTreeNode


def test_location_tree():
    root = LocationTreeNode("Global")

    india = LocationTreeNode("India")
    usa = LocationTreeNode("U.S.A")

    gujarat = LocationTreeNode("Gujarat")
    karnataka = LocationTreeNode("Karnataka")
    india.add_child(gujarat)
    india.add_child(karnataka)

    new_jersey = LocationTreeNode("New Jersey")
    carlifonia = LocationTreeNode("Carlifonia")
    usa.add_child(new_jersey)
    usa.add_child(carlifonia)

    ahmedabad = LocationTreeNode("Ahmedabad")
    baroda = LocationTreeNode("Baroda")
    gujarat.add_child(ahmedabad)
    gujarat.add_child(baroda)

    bangluru = LocationTreeNode("Bangluru")
    mysore = LocationTreeNode("Mysore")
    karnataka.add_child(bangluru)
    karnataka.add_child(mysore)

    princeton = LocationTreeNode("Princeton")
    trenton = LocationTreeNode("Trenton")
    new_jersey.add_child(princeton)
    new_jersey.add_child(trenton)

    san_francisco = LocationTreeNode("San Francisco")
    mountain_view = LocationTreeNode("Mountain View")
    palo_alto = LocationTreeNode("Palo Alto")
    carlifonia.add_child(san_francisco)
    carlifonia.add_child(mountain_view)
    carlifonia.add_child(palo_alto)

    root.add_child(india)
    root.add_child(usa)

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
