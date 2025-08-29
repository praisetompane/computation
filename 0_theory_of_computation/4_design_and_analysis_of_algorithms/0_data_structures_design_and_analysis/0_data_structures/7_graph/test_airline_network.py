from uses_cases.directed.airline_network.airline_network import AirlineNetwork
from uses_cases.directed.airline_network.airport import AirPort
from impl.edge import Edge, Vertex


mb = AirPort("Mumbai", 1000)
pr = AirPort("Paris", 600)
db = AirPort("Dubai", 1000)
ny = AirPort("New York", 250)
tr = AirPort("Toronto", 250)

routes = [
    Edge(mb, pr, 1000),
    Edge(mb, db, 900),
    Edge(pr, ny, 800),
    Edge(pr, db, 800),
    Edge(db, ny, 1500),
    Edge(ny, tr, 2000),
]
airline_network = AirlineNetwork(routes)


def test_initialize_graph():
    edges_dictionary = {
        AirPort("Mumbai"): [AirPort("Paris"), AirPort("Dubai")],
        AirPort("Paris"): [AirPort("New York"), AirPort("Dubai")],
        AirPort("Dubai"): [AirPort("New York")],
        AirPort("New York"): [AirPort("Toronto")],
    }
    assert routes == airline_network.edges
    # assert edges_dictionary == airline_network.edges_dictionary


def test_find_paths():
    paths = airline_network.find_paths(mb, ny)
    assert [[mb, pr, ny], [mb, pr, db, ny], [mb, db, ny]] == paths


def test_find_shortest_path():
    assert [mb, pr, ny] == airline_network.find_shortest_path(mb, ny)
    assert [pr, ny] == airline_network.find_shortest_path(pr, ny)
    assert [ny] == airline_network.find_shortest_path(ny, ny)


if __name__ == "__main__":
    test_initialize_graph()
    test_find_paths()
    test_find_shortest_path()
