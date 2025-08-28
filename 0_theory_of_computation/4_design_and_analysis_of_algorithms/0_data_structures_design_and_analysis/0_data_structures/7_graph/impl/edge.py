from impl.vertex import Vertex

class Edge:
    def __init__(self, start: Vertex, end: Vertex, weight: int) -> None:
        self.start = start
        self.end = end
        self.weight = weight

    def __repr__(self) -> str:
        return f"{self.start.name} -> {self.start.name} weight: {self.weight}"