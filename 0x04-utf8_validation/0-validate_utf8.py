#!/usr/bin/python3
"""checks if the valid data is UTF8 valid or not
"""


def validUTF8(data):
    """checks if data is UTF-8 valid encoded

    Args:
        data (_type_): data to process
    """
    remaining_bytes = 0

    for byte in data:
        if remaining_bytes > 0:
            if (byte & 0b11000000) != 0b10000000:
                return False
            remaining_bytes -= 1
        else:
            while (byte & 0b11000000) == 0b11000000:
                remaining_bytes += 1
                byte <<= 1

            if remaining_bytes > 3 or remaining_bytes == 1:
                return False

    return remaining_bytes == 0
