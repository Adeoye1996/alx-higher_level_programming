#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Compute the square of each element in a matrix."""
    new_matrix = [[x ** 2 for x in row] for row in matrix]
    return new_matrix
