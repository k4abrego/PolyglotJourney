from typing import NamedTuple
from collections import deque


type WeightedGraph = dict[str, set[tuple[str, int]]]

class Edge(NamedTuple):
    weight: int
    u: str
    v: str

    def __eq__(self, other: object) -> bool:    #eq is for
        if not isinstance(other, Edge):
            return False
        return (self.weight == other.weight
                and ((self.u == other.u and self.v == other.v)
                    or (self.u == other.v and self.v == other.u)))

    def __hash__(self):
        return hash(self.weight) + hash(self.u) + hash(self.v)


def sort_edges(graph: WeightedGraph) -> deque[Edge]:
    result: set[Edge] = set()
    for u, neighbours in graph.items(): # neighbours: a set tuple, each tuple contains an number, int
        for v, weight in neighbours:
            result.add(Edge(weight, u, v))
    return deque(sorted(list(result)))

def add_edge(graph: WeightedGraph, edge: Edge) -> None:
    weight, u, v = edge
    graph[u].add((v, weight)) 
    graph[v].add((u, weight))

def remove_edge(graph: WeightedGraph, edge: Edge) -> None:
    weight, u, v = edge
    graph[u].remove((v, weight))
    graph[v].remove((u, weight))

def has_cycle(
        initial: str,
        graph: WeightedGraph,
        visited: set[str] | None = None,
        parent: str | None = None) -> bool: #we need because the visited set is the parent of the current node, so we don't want to go back to the parent node. a cycle needs at least 3 vertices 
    if visited is None:
        visited = set()
    visited.add(initial)
    for v, _ in graph[initial]: #this part is to check if the current node has a neighbour that is already visited and is not the parent of the current node, then there is a cycle. creates a dictionary of the current node and its neighbours, then check if any of the neighbours is already visited and is not the parent of the current node. if so, return True. if not, recursively call has_cycle on the neighbour. if any of the recursive calls return True, return True. if none of the recursive calls return True, return False.
        if v in visited:
            if v != parent:
                return True
        elif has_cycle(v, graph, visited, initial):
            return True
    return False

def kruskal_mst(graph: WeightedGraph) -> tuple[int, WeightedGraph]:
    queue: deque[Edge] = sort_edges(graph)
    result: WeightedGraph = {v: set() for v in graph}
    total: int = 0
    visited: set[str] = set()
    remaining_edges: int = len(graph) - 1   #wee need to keep as the formula n -1 
    while remaining_edges:
        edge: Edge = queue.popleft()
        add_edge(result, edge)
        if (edge.u in visited
                and edge.v in visited
                and has_cycle(edge.u, result)):
            remove_edge(result, edge)
        else:
            visited.add(edge.u)
            visited.add(edge.v)
            total += edge.weight
            remaining_edges -= 1

    return (total, result)


if __name__ == '__main__':
    g1: WeightedGraph = {
        'A': {('B', 2), ('C', 6), ('D', 5)},
        'B': {('A', 2), ('C', 8), ('D', 11)},
        'C': {('A', 6), ('B', 8), ('D', 1)},
        'D': {('A', 5), ('B', 11), ('C', 1)}
    }
    # g2: WeightedGraph = {
    #     'A': {('B', 1), ('D', 12), ('F', 6)},
    #     'B': {('A', 1), ('C', 15), ('D', 13), ('E', 9)},
    #     'C': {('B', 15), ('E', 3), ('G', 7)},
    #     'D': {('A', 12), ('B', 13), ('F', 14), ('G', 2)},
    #     'E': {('B', 9), ('C', 3), ('F', 10), ('G', 8)},
    #     'F': {('A', 6), ('D', 14), ('E', 10), ('G', 11), ('H', 4)},
    #     'G': {('C', 7), ('D', 2), ('E', 8), ('F', 11), ('H', 5)},
    #     'H': {('F', 4), ('G', 5)}
    # }

    g2: WeightedGraph = {
        'A': {('B', 1), ('D', 12), ('F', 10)},
        'B': {('A', 1), ('C', 15), ('D', 13), ('E', 9)},
        'C': {('B', 15), ('E', 3), ('G', 2)},
        'D': {('A', 12), ('B', 13), ('F', 14), ('G', 2)},
        'E': {('B', 9), ('C', 3), ('F', 10), ('G', 8)},
        'F': {('A', 10), ('D', 14), ('E', 10), ('G', 11), ('H', 4)},
        'G': {('C', 2), ('D', 2), ('E', 8), ('F', 11), ('H', 5)},
        'H': {('F', 4), ('G', 5)}
    }

    # e1: Edge = Edge(10, 'A', 'B')
    # e2: Edge = Edge(10, 'B', 'A')
    # print(e1)
    # print(e2)
    # print(e1 == e2)


    from pprint import pprint
    # pprint(sort_edges(g1))
    # print()
    # pprint(sort_edges(g2))


    # g: WeightedGraph = {
    #     'A': set(), 
    #     'B': set(),
    #     'C': set(),}
    # e: Edge = Edge(10, 'A', 'B')
    # pprint(g)
    # add_edge(g, e)
    # pprint(g)
    # add_edge(g, Edge(15, 'A', 'C'))
    # pprint(g)

    # remove_edge(g, e)
    # pprint(g)

    # g: WeightedGraph = {
    #     'A': set(), 
    #     'B': set(),
    #     'C': set(),}

    # e1: Edge = Edge(1, 'A', 'B')
    # e2: Edge = Edge(2, 'B', 'C')
    # e3: Edge = Edge(3, 'C', 'A')
    # add_edge(g, e1)
    # add_edge(g, e2)
    # # add_edge(g, e3)
    # pprint(g)
    # print(has_cycle('A', g))
    # print(has_cycle('B', g))

    pprint(kruskal_mst(g1))
    print()
    pprint(kruskal_mst(g2))
