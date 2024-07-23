#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for row in range(len(triangle), n):
        current_row = [1]
        for element in range(1, row):
            current_row.append
            (triangle[row - 1][element] + triangle[row - 1][element - 1])
        current_row.append(1)
        triangle.append(current_row)
    return triangle
