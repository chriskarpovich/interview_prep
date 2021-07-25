"""
Given a real number between 0 and 1 (eg. 0.72), that is passed in as a double, print the binary representation. If the number cannot be 
represented accurately in binary with at most 32 characters, print "ERROR".
"""

def bin_to_string(num):
    if num < 0 or num > 1:
        return "ERROR"
    bin_string = ['.']
    decimal = None
    # we exclude the decimal point in the 32 count
    while len(bin_string) < 33 and num != 0:
        # floor division to truncate
        num *= 2
        if num >= 1:
            decimal = num - 1
            bin_string.append("1")
        else:
            decimal = num
            bin_string.append("0")
        num = decimal
    # pad string with zeros if not at 32 chars yet
    if len(bin_string) < 33:
        delta = 33 - len(bin_string)
        for _ in range(delta):
            bin_string.append('0')
    return "".join(bin_string)


def bin_to_string_sol(number):
    bit_str = "."
    if number >= 1.0 or number <= 0.0:
        good_nums = ["1"] + ["1.0" + "0" * i for i in range(32)]
        good_nums += ["0"] + ["0.0" + "0" * i for i in range(32)]
        if str(number) not in good_nums:
            return "ERROR"
    while number > 0:
        if len(bit_str) > 32:
            return bit_str
        two = number * 2
        # Testing if 1 after decimal point
        if two >= 1:
            bit_str += "1"
            number = two - 1
        else:
            bit_str += "0"
            number = two
    return bit_str.ljust(33, "0")


def example():
    for number in [1, 0.625, 0, 0.1, 0.101, 0.2, 0.5, 1, 2]:
        bit_str = bin_to_string(number)
        response = bit_str if len(bit_str) <= 33 else "ERROR"
        print(f"Number: {number}, Binary String: {response}")
        bit_str = bin_to_string_sol(number)
        response = bit_str if len(bit_str) <= 33 else "ERROR"
        print(f"Number: {number}, Binary String: {response}")
        assert bin_to_string(number) == bin_to_string_sol(number)


if __name__ == "__main__":
    example()