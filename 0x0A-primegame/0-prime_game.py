#!/usr/bin/python3
"""Spot the winner"""


def isWinner(x, nums):
    """Determine who wins the game between maria and ben."""

    if not nums or x < 1:
        return None

    highest_num = max(nums)
    check_prime = [True for _ in range(max(highest_num + 1, 2))]

    for e in range(2, int(pow(highest_num, 0.5)) + 1):
        if not check_prime[e]:
            continue

    for y in range(e * e, highest_num + 1, e):
        check_prime[y] = False

    check_prime[0] = check_prime[1] = False
    z = 0

    for c in range(len(check_prime)):
        if check_prime[c]:
            z += 1
        check_prime[c] = z

    p1 = 0
    for x in nums:
        p1 += check_prime[x] % 2 == 1
    if p1 * 2 == len(nums):
        return None
    if p1 * 2 > len(nums):
        return "Maria"
    return "Ben"
