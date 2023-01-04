#!/usr/bin/python3
import sys


def nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    if type(n) != int:
        print("N must be a number")
        sys.exit(1)
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    board = []
    for i in range(n):
        board.append([])
        for j in range(n):
            board[i].append(0)
    solve(board, 0, n)


def solve(board, col, n):
    if col >= n:
        print(board)
        return True
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve(board, col + 1, n) or res
            board[i][col] = 0
    return res


def is_safe(board, row, col, n):
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


if __name__ == "__main__":
    nqueens(int(sys.argv[1]))
