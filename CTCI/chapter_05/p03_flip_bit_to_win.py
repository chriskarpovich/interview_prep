"""
You have an integer and you can flip exactly one bit from 0 to 1. Write code to find the length of the longest sequence of 1s you could create.
Ex:
    Input: 1775 (11011101111)
    Output: 8
"""

def flip_bit_to_win(num):
    max_count = 0
    for idx in range(12):
        # get bit by making mask with 000100 and then comparing AND num to zero
        mask = 1 << idx 
        if (num & mask) == 0:
            # we have a 0 in that digit
            # flip bit from 0 to 1 by making mask like 0001000 and then OR with num
            # count number of ones in a row
            flipped_num = num | mask

            counter = 0
            for idx_2 in range(12):
                mask_iter = 1 << idx_2
                if (flipped_num & mask_iter) == 0:
                    # we have a 0, save max value and restart the counter
                    if counter > max_count:
                        max_count = counter
                    counter = 0
                else:
                    # we have a 1, add 1 to counter
                    counter += 1
    return max_count


def flip_bit_to_win_str(number):
    number_str = bin(number)[2:]
    max_cnt, cnt, cnt0 = 0, 0, 0
    i = len(number_str)  # start index
    while i:
        if number_str[i - 1] == '1':
            cnt += 1
        else:
            if cnt0 == 0: # first 0
                temp_i = i
                cnt0 = 1
            else:  # second 0
                max_cnt = cnt
                i = temp_i  # rewind
                cnt0 = 0
                cnt = 0
        i -= 1

    max_cnt = max(cnt, max_cnt)

    return max_cnt + 1

def flip_bit_to_win_alt(num):
    longest, current_segment, past_segment = 1, 0, 0
    while num != 0:
        if num & 1:  # Current bit is 1
            current_segment += 1
        else:  # Current bit is 0
            past_segment = 0 if (num & 2 is True) else current_segment
            current_segment = 0
        longest = max(current_segment + past_segment + 1, longest)
        num >>= 1  # Move 1 bit to the right
    return longest


test_cases = [(0b0, 1), (0b111, 4), (0b10011100111, 4), (0b11011101111, 8)]
testable_functions = [flip_bit_to_win, flip_bit_to_win_str]


def test_flip_bit_to_win():
    for fli_bit in testable_functions:
        for num, expected in test_cases:
            result = fli_bit(num)
            print(result)
            assert result == expected


if __name__ == "__main__":
    test_flip_bit_to_win()