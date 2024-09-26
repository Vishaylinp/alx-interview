#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """compute the perimeter"""

    perim = 0

    for x in range(0, len(grid)):
        for y in range(0, len(grid[x])):
            if grid[x][y] == 1:
                perim += 4
                if x > 0 and grid[x - 1][y]:
                    perim -= 2
                if y > 0 and grid[x][y - 1]:
                    perim -= 2
    return perim
