"""
Given a positive integer, print the next smallest and the next largest number that have the same number of 1 bits in their
binary representation.
"""

def next_larger(num):
    # find least significant pattern of 1's in the number
    # move left most digit up one spot and move rest down to the right most spots possible
    # e.g. 10110 --> 11001
    if num == 0:
        return 1

    # find first one's position
    zeros = 0
    while not (num & (1 << zeros)):
        zeros += 1
    # find number of ones until we hit another zero
    ones = 0
    while num & (1 << (zeros + ones)):
        ones += 1
    
    # flip rightmost non-trailing 0 to 1
    non_trailing_zero = 1 << (zeros + ones)
    num = num | non_trailing_zero

    # clear all bits below the flipped bit
    # create mask of 1111100000 and then and it with num
    mask = (~0 << zeros + ones)
    num = num & mask
    # flip ones - 1 bits starting from the least significant bit
    for i in range(ones - 1):
        num = num | (1 << i)
    return num

def next_smaller(num):
    # find rightmost non-trailing one and move it and all ones below it to one spot below
    # e.g. 10110 --> 10011, 10110001 --> 10101100
    if num == 0:
        return None
    # count trailing ones
    temp = num
    trailing_ones = 0
    while (temp & 1 == 1):
        trailing_ones += 1
        temp = temp >> 1
    # check if num was entirely ones, which in case we can't make it smaller
    if temp == 0:
        return None
    # find rightmost non-trailing one by counting zeros between trailing ones and non-trailing one
    zeros = 0
    while not (num & (1 << zeros)):
        zeros += 1
    # zero out everything at or below position of rightmost non-trailing ones

    mask = ~0 << (zeros + trailing_ones + 1)

    num = num & mask

    # put in trailing_ones + 1 ones directly below where the trailing one used to be
    mask = (1 << (trailing_ones + 1)) - 1
    mask = mask << (zeros - 1)
    num = num | mask
    return num



def test_next_smaller_than_0b11111() -> None:
    assert next_smaller(0b11111) is None
def test_next_larger_than_0b11111() -> None:
    result = next_larger(0b11111)
    print(bin(result))
    assert result is None


def test_next_smaller_than_0b10110() -> None:
    assert next_smaller(0b10110) == 0b10101


def test_next_larger_than_0b10110() -> None:
    result = next_larger(0b10110)
    assert result == 0b11001


if __name__ == "__main__":
    x = int(input("Enter a positive integer: "))
    while x < 0:
        x = int(input(str(x) + " is not positive. Please try again: "))
    print("Next smaller: ", next_smaller(x))
    print("Next larger: ", next_larger(x))
    test_next_larger_than_0b10110()
    test_next_smaller_than_0b10110()
    test_next_smaller_than_0b11111()