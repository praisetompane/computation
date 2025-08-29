from impl.edge import Edge
from impl.vertex import Vertex
from typing import List


class Graph:
    def __init__(self, edges: List[Edge]) -> None:
        self.edges = edges
        self.edges_dictionary: dict[Vertex, List[Vertex]] = {}
        for e in self.edges:
            if e.start in self.edges_dictionary:
                self.edges_dictionary[e.start].append(e.end)
            else:
                self.edges_dictionary[e.start] = [e.end]

    def add_edge(self, start: Vertex, end: Vertex, weight: int):
        self.edges.append(Edge(start, end, weight))

    def find_paths(
        self, start: Vertex, end: Vertex, path: List[Vertex] = []
    ) -> List[List[Vertex]]:
        # the path accumulator
        # add each start to the accumulated path
        path = path + [start]

        # we have reached the end, thus return the accumulated path
        if start == end:
            return [path]

        # there exists no edge with the supplied start
        if start not in self.edges_dictionary:
            return []

        paths = []
        # visit the nodes you can get to from your start
        for node in self.edges_dictionary[start]:
            # prevent duplicates in the path accumulator
            if node not in path:
                # add the current node to the path(it will be added in the next recursion call as the start value)
                # also add the nodes we get to from the current node.
                new_paths = self.find_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def find_shortest_path(self, start: Vertex, end: Vertex, path=[]):
        # approach 1
        # generate all paths using find_paths already implemented
        # return the shortest based on predicate value(number of verticees, weight, etc)
        # implementation:
        # paths = self.find_paths(start, end)
        # path_lengths = [len(path) for path in paths]
        # path_lengths_indices = enumerate(path_lengths)
        # shorest_path_lengths_index = min(path_lengths_indices, key = lambda x: x[1])

        # return paths[shorest_path_lengths_index[0]]

        # approach 2
        # keep track of shortest path across all explored paths
        path = path + [start]

        if start == end:
            return path

        if start not in self.edges_dictionary:
            return None

        shortest_path = None
        for node in self.edges_dictionary[start]:
            if node not in path:
                new_path = self.find_shortest_path(node, end, path)

                if new_path:
                    if shortest_path is None or len(new_path) < len(shortest_path):
                        shortest_path = new_path

        return shortest_path
