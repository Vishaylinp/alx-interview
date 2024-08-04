#!/usr/bin/python3
"""Locked boxes"""


def canUnlockAll(boxes):
    """Unlock box"""

    n = len(boxes)
    boxopen = set()
    boxopen.add(0)
    stack = [0]

    while stack:
        curr_box = stack.pop()
        for ky in boxes[curr_box]:
            if ky not in boxopen and ky < n:
                boxopen.add(ky)
                stack.append(ky)
    return len(boxopen) == n
