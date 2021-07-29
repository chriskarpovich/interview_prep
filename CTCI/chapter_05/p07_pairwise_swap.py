"""
Write a program to swap odd and even bits in an integer with as few instructions as possible (e.g., bit 0 and bit 1 are swapped,
bit 2 and bit 3 are swapped, etc.)
"""

def pairwise_swap(num):
    num_up_shifted = num << 1 # 1, 3, 5, ...
    num_down_shifted = num >> 1 # 0, 2, 4, ...
    idx = 0
    swapped_num = 0
    for i in range(64):
        if idx % 2 == 0:
            val = num_down_shifted & (1 << idx)
        else:
            val = num_up_shifted & (1 << idx)
        swapped_num = swapped_num | val
        idx += 1

    return swapped_num

def pairwise_swap(number):
    mask_10 = 0xAAAAAAAA  # 32 bits
    mask_01 = 0x55555555  # 32 bits
    num_evn = number & mask_10
    num_odd = number & mask_01
    swp_num = (num_evn >> 1) | (num_odd << 1)
    return swp_num

def test_pairwise_swap():
    view_output = 1
    for number, exp_output in zip([123, 781, 278], [183, 782, 553]):
        swap_num = pairwise_swap(number)
        if view_output:
            print(f"Number:  {bin(number)}")
            print(f"Swapped: {bin(swap_num)}")
            print(bin(exp_output))
        assert swap_num == exp_output


if __name__ == "__main__":
    test_pairwise_swap()