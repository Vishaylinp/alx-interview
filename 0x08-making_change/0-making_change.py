#!/usr/bin/python3
"""Change maker"""


def makeChange(coins, total):
    """make change function"""

    val = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0

    for c in coins:
        if total % c <= total:
            val += total // c
            total = total % c

    return val if total == 0 else -1
