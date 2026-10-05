# File: fifteen_puzzle.py

from generic_search import astar, Node, node_to_path

type Frame = tuple[tuple[int,], ]


def solve_puzzle(frame: Frame) -> None:
    result: Node[Frame] | None = astar(
        frame, goal_test, successors, heuristic)
    # The rest of the function's code goes here
    


# The rest of the module's code goes here
