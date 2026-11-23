type Board = list[list[bool]]


def is_safe(board: Board, row: int, col: int) -> bool:
    #Is there another queen in the same row?
    for i in range(col):
        if board[row][i]:
            return False


    # Is there another queen in the upper left diagonal?
    for i, j in zip(range(row - 1, -1, -1),
                    range(col - 1, -1, -1)):
        if board[i][j]:
            return False
    
    # Is there another queen in the lower left diagonal?
    for i, j in zip(range(row + 1, len(board)),
                    range(col - 1, -1, -1)):
        if board[i][j]:
            return False

    #If no queens are found, then it is safe to place a queen at (row, col)
    return True


def solve(board: Board, col: int) -> bool:
    # Base case: If all queens are placed, return True
    if col == len(board):
        return board
    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = True  # Place queen cause it is safe
            result: Board | None = solve(board, col + 1) #to check the next column, thats whyv we increment col by 1 thats the rule
            if result:
                return result
            board[row][col] = False  # Backtrack if placing queen doesn't lead to a solution
    return None  # No valid position found in this column