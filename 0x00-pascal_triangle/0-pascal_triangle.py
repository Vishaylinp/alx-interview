#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """create a triangle"""

    if n <= 0:
        return []

    tri = []
    for num_rows in range(n):
        row = [1] * (num_rows + 1)
        for i in range(1, num_rows):
            row[i] = tri[num_rows - 1][i - 1] + tri[num_rows - 1][i]
        tri.append(row)
    return tri
