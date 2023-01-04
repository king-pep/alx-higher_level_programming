#!/usr/bin/python3
 if solve(board, col + 1, p):
                return True
            board[i][col] = 0
    return False


def isSafe(board, row, col, p):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, p, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except:
        print("N must be a number")
        exit(1)
    nqueens(n)
