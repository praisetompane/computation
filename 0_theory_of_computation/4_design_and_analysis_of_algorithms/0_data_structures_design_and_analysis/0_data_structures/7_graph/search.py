from queue import Queue


class Node:
    name = ""
    friends = []
    neighbours = []
    life_partner = ""
    _visited = False
    _marked = False

    def __init__(self, name, friends, neighbours):
        self.name = name
        self.friends = friends

    def add_friend(self, name):
        self.friends.append(name)

    """
        find shoertet path between s and t

        G(V,E)
        k = max E from Vi
        d = s to t shortest path length
        bfs
            1st level = O(k) nodes visited
            2nd level = O(k^2) nodes visited
            3nd level = O(k^3) nodes visited
            d level   = O(k^d)  nodes visited

        bi_bfs
            2 * bfs => bfs(s) && bfs(t§), collide at d/2(i.e. midpoint of path between s & t)
            bfs(s) => O(k^d/2) nodes visited
            bfs(t) => O(k^d/2) nodes visited
            Therefore O(2*k^d/2) = O(k^d/2) = Faster by d/2 => Twice as fast

    """

    def bi_directional_search(self, start_ndoe, end_node):
        # run bfs from start node
        # run bfs from end node
        # connection found if searches collide
        return

    """
        Why suitable for shortest path?¹
            loops through ALL current shortest paths,
                before moving to the next length

            Example:
                Given: ShortestPathRequest(from=A, to=B)
                    explores/loops all paths of length 1 from A
                    then all paths of length 2 from A
                    then all paths of length 3 from A
                    then all paths of length 4 from A
                    ... until it finds or does not find B

                    i.e. explores all the current shortest paths from A
    """

    def breadth_first_search(self, name):
        queue = Queue(maxsize=0)  # infinite
        self._marked = True
        queue.put(self)
        while not queue.empty():
            current_friend = queue.get()
            if current_friend.name == name:
                return self
            for f in current_friend.friends:
                if not f._marked:
                    queue.put(f)
                    f._marked = True
        return None

    def depth_first_search(self, name):
        self._visited = True
        if self.name == name:
            return self
        else:
            for f in self.friends:
                if not f._visited:
                    search_result = f.depth_first_search(name)
                    # Modifification of standard DFS to return a node with the
                    # search key
                    if search_result is not None:
                        return search_result
        # Modifification of standard DFS to clear state for next searches
        self._reset_visited
        return None

    def is_friends_with(self, name):
        for f in self.friends:
            if f.name == name:
                return True
        return False

    def _reset_visited(self):
        self._visited = False
        for f in self.friends:
            f._reset_visited(f)


def main():
    pitso = Node("Pitso", [], [])
    christiaan = Node("Christiaan", [], [])
    smarty = Node("Smarty", [], [])
    earl = Node("Earl", [], [])
    thato = Node("Thato", [pitso, christiaan, smarty, earl], [])
    """
        Observation: I call add for each vertice(node) in an edge(relationship)
        Should add_friend in a undirected graph also add current node
        to other node's friend list
        What are the performance implications?
    """
    pitso.add_friend(christiaan)
    christiaan.add_friend(pitso)
    pitso.add_friend(smarty)
    smarty.add_friend(pitso)
    smarty.add_friend(christiaan)
    pitso.add_friend(thato)

    smarty.add_friend(earl)
    earl.add_friend(smarty)

    print("Depth First Searchin for", smarty.name)
    result = pitso.depth_first_search(smarty.name)
    if result is not None:
        print("Found %s in %s's friend list" % (result.name, pitso.name))
    result = pitso.is_friends_with(smarty.name)
    print(result)
    if result:
        print("%s is friends with %s" % (smarty.name, pitso.name))
    else:
        print("%s not in %s's friends list" % (smarty.name, pitso.name))

    print("Breadth First Searchin for", smarty.name)
    result = pitso.breadth_first_search(smarty.name)
    if result is not None:
        print("Found %s in %s's friend list" % (result.name, pitso.name))
    result = pitso.is_friends_with(smarty.name)
    print(result)
    if result:
        print("%s is friends with %s" % (smarty.name, pitso.name))
    else:
        print("%s not in %s's friends list" % (smarty.name, pitso.name))


if __name__ == "__main__":
    main()

"""references
1. https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-videos/lecture-3-graph-theoretic-models/
"""
