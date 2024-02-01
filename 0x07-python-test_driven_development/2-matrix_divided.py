#!/usr/bin/python3
"""Defines a matrix division function."""

<<<<<<< HEAD

def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
=======
def matrix_divided(matrix, div):
    """Returns a new matrix (list of list).
>>>>>>> 16ef7107f839f934cd843d2a351906b545b9759b

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.

    Returns:
<<<<<<< HEAD
        list: A new matrix representing the result of the division.
    """
    if not isinstance(matrix, list) or not matrix or not all(isinstance(row, list) for row in matrix) or not all(isinstance(ele, (int, float)) for ele in [num for row in matrix for num in row]):
=======
        A new matrix representing the result of the division.
    """
    if (
        not isinstance(matrix, list)
        or matrix == []
        or not all(isinstance(row, list) for row in matrix)
        or not all(isinstance(ele, (int, float)) for row in matrix for ele in row)
    ):
>>>>>>> 16ef7107f839f934cd843d2a351906b545b9759b
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

<<<<<<< HEAD
    return [[round(num / div, 2) for num in row] for row in matrix]
=======
    return [
        [round(ele / div, 2) for ele in row]
        for row in matrix
    ]
>>>>>>> 16ef7107f839f934cd843d2a351906b545b9759b
