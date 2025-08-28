from uses_cases.airline_network.airline_network import AirlineNetwork
from uses_cases.airline_network.airport import AirPort
from impl.edge import Edge

def test_initialize_graph():
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
        Edge(ny, tr, 2000)
    ]

    airline_network = AirlineNetwork(routes)

    paths = airline_network.find_paths(mb, ny)
    assert [[mb, pr, ny], [mb, pr, db, ny], [mb, db, ny]] == paths

if __name__ == "__main__":
    test_initialize_graph()
