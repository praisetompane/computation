from impl.graph import Graph
from impl.edge import Edge
from typing import List

class AirlineNetwork(Graph):
    def __init__(self, edges: List[Edge]) -> None:
        super().__init__(edges)