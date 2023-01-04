#!/usr/bin/python3

import sys


def nqueens(n):
    if n < 4:
        print("N must be at least 4")
        return
    board = [[0 for i in range(n)] for j in range(n)]
    solve(board, 0, n)


def solve(board, col, n):
    if col >= n:
        print(board)
        return
    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 1
            solve(board, col + 1, n)
            board[i][col] = 0


def isSafe(board, row, col, n):
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
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except:
        print("N must be a number")
        sys.exit(1)
    nqueens(n)
