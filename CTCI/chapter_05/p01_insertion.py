"""
You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to insert M into N such that M starts at bit j
and ends at bit i. You can assume that bits j through i have enough space to fit all of M. That is, if M = 10011, you can assume there
are at least 5 bits between j and i. You would not, for example, have j = 3 and i = 2, because M could not fully fit between 
bit 3 and bit 2.
Ex: 
Input:
    N = 10000000000, M = 10011, i = 2, j = 6
Output:
    N = 10001001100
"""

def bits_insertion(num, m, i, j):
    # do a linear search through the bits of M (from tail to head, right to left)
    # and if you find 1, do a bit insertion to N
    # if you find 0, clear idxth bit of N using a mask
    m_idx = 0
    for idx in range(j - i + 1):
        # if the digit is a zero, clear that bit of N using a mask
        # if the digit is not a zero, do a bit insertion to N
        if (m >> idx) & 1 != 0:
            # set bit to 1. if it was already 1 then it stays 1. need offset of i to the left to get to correct position
            mask = (1 << idx + i)
            num = num | mask
        else:
            # clear bit
            mask = ~(1 << idx + i)
            num = num & mask
    return num  

def bits_insertion_update(num, m, i, j):
    for idx in range(j - i + 1):
        # clear ith digit of num to prepare for setting, all 1's except for zero in ith position
        mask = ~(1 << idx + i)
        num = num & mask
        # get desired value from m (0 or 1)
        value = (m >> idx) & 1
        # update n's digit with this value
        # create mask with ith digit having the value and all others zero
        mask = value << (idx + i)
        num = num | mask
    return num




test_cases = [
    ((int("10000000000", 2), int("10011", 2), 2, 6), int("10001001100", 2)),
    ((int("11111111111", 2), int("10011", 2), 2, 6), int("11111001111", 2)),
]

testable_functions = [bits_insertion, bits_insertion_update]


def test_bits_insertion():
    for bits_insert in testable_functions:
        for (n, m, i, j), expected in test_cases:
            calculated = bits_insert(n, m, i, j)
            error_msg = f"{bits_insert.__name__}: {calculated:b} != {expected:b}"
            assert bits_insert(n, m, i, j) == expected, error_msg


if __name__ == "__main__":
    test_bits_insertion()