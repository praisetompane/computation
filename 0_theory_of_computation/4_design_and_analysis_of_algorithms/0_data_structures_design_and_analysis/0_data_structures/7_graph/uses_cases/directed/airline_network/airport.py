from impl.vertex import Vertex


class AirPort(Vertex):
    def __init__(self, name, capacity=0) -> None:
        super().__init__(name)
        self.capacity = capacity

    def __repr__(self) -> str:
        return self.name
