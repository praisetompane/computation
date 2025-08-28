from impl.edge import Edge
from impl.vertex import Vertex
from typing import List

class Graph:
    def __init__(self, edges: List[Edge]) -> None:
        self.edges = edges
        self.graph_dictionary:dict[Vertex, List[Vertex]] = {}
        for e in self.edges:
            if e.start in self.graph_dictionary:
                self.graph_dictionary[e.start].append(e.end)
            else:
                self.graph_dictionary[e.start] = [e.end]

    def add_edge(self, start: Vertex, end: Vertex, weight: int):
        self.edges.append(Edge(start, end, weight))

    def find_paths(self, start: Vertex, end: Vertex, path: List[Vertex]=[]) -> List[List[Vertex]]:
        # the path accumulator
            # add each start to the accumulated path
        path = path + [start]

        # we have reached the end, thus return the accumulated path
        if start == end:
            return [path]

        # there exists no edge with the supplied start
        if start not in self.graph_dictionary:
            return []

        paths = []
        # visit the nodes you can get to from your start
        for node in self.graph_dictionary[start]:
            # prevent duplicates in the path accumulator
            if node not in path:
                # add the current node to the path(it will be added in the next recursion call as the start value)
                    # also add the nodes we get to from the current node.
                new_paths = self.find_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def find_shortest_path(self, start: Vertex, end: Vertex):
        pass
