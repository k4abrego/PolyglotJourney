from generic_search import astar, Node, node_to_path

type Frame = tuple[tuple[int, ...], ...]

GOAL = ((1, 2, 3, 4),
        (5, 6, 7, 8),
        (9, 10, 11, 12),
 (13, 14, 15, 0))


def goal_test(frame: Frame) -> bool:
    return frame == GOAL



def successors(frame: Frame) -> list[Frame]:
    # encuentra la posición donde está el 0
    empty_row = 0
    empty_col = 0

    for row in range(4):
        for col in range(4):
            if frame[row][col] == 0:
                empty_row = row
                empty_col = col

    next_frames = []

    # list of frame configurations in the following movement order: [Up ,Down, Left, Right]
    movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for row_change, col_change in movements:
        new_row = empty_row + row_change
        new_col = empty_col + col_change

        if 0 <= new_row < 4 and 0 <= new_col < 4:
            # convertir las tuplas en listas para mover las fichas
            new_frame = [list(row) for row in frame]

            # intercambiar el 0 con la ficha correspondiente
            new_frame[empty_row][empty_col] = new_frame[new_row][new_col]
            new_frame[new_row][new_col] = 0

            new_frame = tuple(tuple(row) for row in new_frame)
            next_frames.append(new_frame)

    return next_frames



def heuristic(frame: Frame) -> float:
    #aquí debería de contar la cantidad de números que no están en su lugar, incluyendo 0
    return float(sum(
        frame[r][c] != GOAL[r][c]
        for r in range(4)
        for c in range(4)
))


def solve_puzzle(frame: Frame) -> None:
    result: Node[Frame] | None = astar(
        frame, goal_test, successors, heuristic
    )

    if result is None:
        print("no solution found")
        return

    path = node_to_path(result)
    steps = len(path) - 1

    print(f"Solution requires {steps} {'step' if steps == 1 else 'steps'}")

    for index, (before, after) in enumerate(
        zip(path, path[1:]), start=1
    ):
        old_empty = next(
            (r, c)
            for r in range(4)
            for c in range(4)
            if before[r][c] == 0
        )

        new_empty = next(
            (r, c)
            for r in range(4)
            for c in range(4)
            if after[r][c] == 0
        )

        moved_tile = before[new_empty[0]][new_empty[1]]

        row_change = old_empty[0] - new_empty[0]
        col_change = old_empty[1] - new_empty[1]

        if row_change == -1:
            direction = "up"
        elif row_change == 1:
            direction = "down"
        elif col_change == -1:
            direction = "left"
        else:
            direction = "right"

        print(f"Step {index}: Move {moved_tile} {direction}")



if __name__ == "__main__":
    solve_puzzle((((2, 3, 4, 8),
                   (1, 5, 7, 11),
                   (9, 6, 12, 0),
                   (13, 14, 10, 15))))

    print()

    print(heuristic(((2, 3, 4, 8),
                  (1, 5, 7, 11),
                  (9, 6, 12, 0),
                  (13, 14, 10, 15))))
