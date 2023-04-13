#!/usr/bin/python3
"""Defines a matrix divided function."""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix.
    Args:
        matrix (list): A lists of lists of integers/floats
        div (int/float): The divisor.
    Raises:
        TypeError: If matrix is non numbers
        TypeError: If matrix contains rows of different sizes
        TypeError: If div is not int/float
        ZeroDivisionError: If div is not equal to 0
    Returns:
        A new matrix representing the result of division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])