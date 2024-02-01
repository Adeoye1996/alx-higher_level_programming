#!/usr/bin/python3
"""The N-queens puzzle"""

import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    return [[' ' for _ in range(n)] for _ in range(n)]


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    return [row.copy() for row in board]


def get_solution(board):
    """Return the list of lists representation in a board."""
    return [[r, c] for r, row in enumerate(board) for c, value in enumerate(row) if value == 'Q']


def xout(board, row, col):
    """X spots on a chessboard."""
    # X out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = 'x'
    # X out all backward spots
    for c in range(col - 1, -1, -1):
        board[row][c] = 'x'
    # X out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = 'x'
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = 'x'
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = 'x'
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = 'x'
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = 'x'
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = 'x'
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == ' ':
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = 'Q'
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    
    n_value = sys.argv[1]
    
    if not n_value.isdigit():
        print('N must be a number')
        sys.exit(1)
    
    n = int(n_value)
    
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    chess_board = init_board(n)
    solutions = recursive_solve(chess_board, 0, 0, [])
    
    for sol in solutions:
        print(sol)
