#!/usr/bin/python3
"""Rotate 2D matric"""

def rotate_2d_matrix(matrix):
    """transpose and reverse"""

    for x in range(len(matrix)):
        for y in range(x, len(matrix)):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

    for r in range(len(matrix)):
        matrix[r].reverse()
