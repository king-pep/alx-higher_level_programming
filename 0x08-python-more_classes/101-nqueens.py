#!/usr/bin/python3

"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./101-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""

import sys

board = []
solutions = []


def isSafe(row, col):
    for i in range(col):
        if board[row][i]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def solveNQUtil(col):
    if col >= len(board):
        solutions.append([i for i in board])
        return True

    res = False
    for i in range(len(board)):
        if isSafe(i, col):
            board[i][col] = 1
            res = solveNQUtil(col + 1) or res
            board[i][col] = 0

    return res


def solveNQ():
    if not solveNQUtil(0):
        print("No solution exists")

    for solution in solutions:
        print([[row, col] for col in range(len(board)) for row in range(len(board)) if solution[row][col]])


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        exit(1)
    board = [[0 for i in range(N)] for j in range(N)]
    solveNQ()
