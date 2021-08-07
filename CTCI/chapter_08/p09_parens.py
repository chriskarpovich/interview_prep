"""
Implement an algorithm to print all valid (e.g., properly opened and closed) combinations of n pairs of parentheses.
E.g. 
Input: 3
Output: ((())), (()()), (())(), ()(()), ()()()
"""
import unittest
from copy import deepcopy

def generate_parentheses_permutations_recursive_1(num):
    def helper(open_remaining, closed_remaining, string, result):
        # base case: num_open and num_closed are zero
        # append to result
        if open_remaining == 0 and closed_remaining == 0:
            result.append("".join(string))
            return
        # can only put a closed parenthesis if closed_remaining > open_remaining
        # if closed <= open can only put open
        if closed_remaining > 0 and closed_remaining > open_remaining:
            # place closed
            new_string = deepcopy(string)
            new_string.append(')')
            helper(open_remaining, closed_remaining-1, new_string, result)
        # place open regardless
        if open_remaining > 0:
            new_string = deepcopy(string)
            new_string.append('(')
            helper(open_remaining-1, closed_remaining, new_string, result)
        return
    result = []
    open_remaining = num
    closed_remaining = num
    helper(open_remaining, closed_remaining, [], result)
    return result

testable_functions = [
    #generate_parentheses_permutations_brute_force,
    generate_parentheses_permutations_recursive_1,
    #generate_parentheses_permutations_recursive_2,
]

test_cases = [
    (0, [""]),
    (1, ["()"]),
    (2, sorted(["()()", "(())"])),
    (3, sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])),
]


class TestSuite(unittest.TestCase):
    def test_generate_parentheses_permutations(self):
        for f in testable_functions:
            for num, expected in test_cases:
                assert sorted(f(num)) == expected, f"{f.__name__} {num} failed"


def example():
    print(generate_parentheses_permutations_recursive_1(0))
    #print(generate_parentheses_permutations_brute_force(3))
    #print(generate_parentheses_permutations_recursive_2(3))


if __name__ == "__main__":
    # for f in testable_functions:
    #     for num, expected in test_cases:
    #         assert sorted(f(num)) == expected, f"{f.__name__} {num} failed"
    example()