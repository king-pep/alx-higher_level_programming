#!/usr/bin/python3
import sys


def nqueens(p):
    if p < 4:
        print("N must be at least 4")
        exit(1)
    board = [[0 for i in range(p)] for j in range(p)]
    solve(board, 0, p)
    return board


def solve(board, col, p):
    if col >= p:
        print(board)
        return True
    for i in range(p):
        if isSafe(board, i, col, p):
            board[i][col] = 1
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
