from typing import NamedTuple, cast
from csp import Constraint, CSP

type Grid = list[list[int]] 

class GridLocation(NamedTuple):
    row: int
    column: int


if __name__ == '__main__':
    a: GridLocation = GridLocation(1, 2)
    b: GridLocation = GridLocation(1, 2)
    print(f'{a = }')
    print(f'{b = }')
    print(f'{a == b = }')
    x, y = a #Tuples
    print(f'{x = }')
    print(f'{y = }')
    print(f'{a[0] = }')
    print(f'{a[1] = }')
    print(f'{a.row = }')
    print(f'{a.column = }')