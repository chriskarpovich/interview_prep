"""
Write a function to determine the number of bits you would need to flip to convert integer A to integer B.
Ex: 
Input: 29 (or: 11101), 15 (or: 01111)
Output: 2
"""

def conversion(a, b):
    xor = a ^ b
    # count number of on bits
    ct = 0
    while xor != 0:
        if (xor & 1) == 1:
            ct += 1
        xor = xor >> 1
    return ct

def conversion_clean(a, b):
    xor = a ^ b
    ct = 0
    # count number of set bits by clearing least significant set bit each iteration
    # do this by doing xor & (xor - 1)
    while xor != 0:
        xor = xor & (xor - 1) 
        ct += 1
    return ct

def test_29_15() -> None:
    a = 0b11101  # 29
    b = 0b01111  # 15
    assert conversion(a, b) == 2
    assert conversion_clean(a, b) == 2

if __name__ == "__main__":
    test_29_15()