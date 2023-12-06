def check_safety(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def display_solution(board):
    for row in board:
        print("".join("|Q|" if cell == 1 else "|-|" for cell in row))
    print()

def slove_problem(board, col, n):
    if col == n:
        display_solution(board)
        return True

    res = False
    for i in range(n):
        if check_safety(board, i, col, n):
            board[i][col] = 1
            res = slove_problem(board, col + 1, n) or res
            board[i][col] = 0

    return res

def start_solution(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not slove_problem(board, 0, n):
        print(f"No solution exists for {n}-Queens problem.")

n = 4
start_solution(n)
