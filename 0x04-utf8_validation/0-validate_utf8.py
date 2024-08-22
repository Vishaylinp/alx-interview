#!/usr/bin/python3
"""valid"""


def validUTF8(data):
    """Check if data follows UTF-8"""

    count_bytes = 0
    bitmask1 = 1 << 7
    bitmask2 = 1 << 6

    for byte in data:
        byte = byte & 0xFF

        if count_bytes == 0:
            mask = 1 << 7
            while mask & byte:
                count_bytes = count_bytes + 1
                mask = mask >> 1

            if count_bytes == 0:
                continue
            if count_bytes == 1 or count_bytes > 4:
                return False
        else:
            if not (byte & bitmask1 and not (byte & bitmask2)):
                return False

        count_bytes = count_bytes - 1

    return count_bytes == 0
