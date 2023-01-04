#!/usr/bin/python3

import sys


def nqueens(n):
    """Solves the N queens problem"""
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0 for i in range(n)] for j in range(n)]
    solutions = []
    solve(board, 0, solutions)
    for solution in solutions:
        print(solution)


def solve(board, col, solutions):
    """Recursive function to solve the N queens problem"""
    if col == len(board):
        solutions.append(format_solution(board))
        return
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve(board, col + 1, solutions)
            board[i][col] = 0


def is_safe(board, row, col):
    """Checks if a queen can be placed in the given cell"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def format_solution(board):
    """Formats the solution"""
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
    return solution


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    nqueens(n)
