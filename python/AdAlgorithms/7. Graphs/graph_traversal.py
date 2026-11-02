from typing import Iterator
from collections import deque

type Graph = dict[str, list[str]]

def depth_first_search(
        start: str,
        graph: Graph) -> Iterator[str]:
    stack: deque[str] = deque()
    visited: set[str] = set()
    stack.append(start)
    while stack:
        current: str = stack.pop()
        if current not in visited:
            visited.add(current)
            stack.extend(graph[current][::-1]) #this is to push them at the end of the stack, so that they are popped in reverse order. 
                            #  the :: -1 is to reverse the list of neighbors so that they are popped in the order they were added to the stack.
            yield current   # yield current node after adding it to visited, so that it is not yielded again if it is encountered again in the graph.

def breadth_first_search(
        start: str,
        graph: Graph) -> Iterator[str]:
    queue: deque[str] = deque()
    visited: set[str] = set()
    queue.append(start)
    while queue:
        current: str = queue.popleft()
        if current not in visited:
            visited.add(current)
            queue.extend(graph[current])
            yield current



if __name__ == "__main__":
    g: Graph = {
        'A': ['B', 'C', 'F'],
        'B': ['A', 'D'],
        'C': ['A', 'E', 'F'],
        'D': ['B'],
        'E': ['C', 'F'],
        'F': ['A', 'C', 'E', 'G'],
        'G': ['F']
    }

    print(list(depth_first_search('A', g)))
    print(list(breadth_first_search('A', g)))
    print()
    print(list(depth_first_search('E', g)))
    print(list(breadth_first_search('E', g)))