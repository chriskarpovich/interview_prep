"""
Given a boolean expression consisting of the symbols 0 (False), 1 (True), & (AND), | (OR), and ^ (XOR), and a desired boolean
result value result, implement a function to count the number of ways of parenthesizing the expression such that it evaluates
to result.
EX: 
countEval("1^0|0|1", False) -> 2
countEval("0&0&0&1^1|0", True) -> 10
The expression should be fully parenthesized (e.g., (0) ^ (1)) but not extraneously (e.g., (((0)) ^ (1)) ).
"""

import unittest

def evaluate(string, exp_result):
    def helper(string, exp_result, memo):
        # base case, no operators in string
        if string == "1":
            if exp_result:
                return 1
            else:
                return 0
        if string == "0":
            if exp_result:
                return 0
            else:
                return 1

        if string not in memo:

            # total number of ways to make the expression True
            totalTrue = 0
            # total number of ways the expression can be True or False
            totalWays = 0
            i = 1
            string_len = len(string)
            while i < string_len:
                left = string[0:i]
                right = string[i+1:]
                leftTrue = helper(left, True, memo)
                leftFalse = helper(left, False, memo)
                rightTrue = helper(right, True, memo)
                rightFalse = helper(right, False, memo)
                if string[i] == "&":
                    totalTrue += (leftTrue * rightTrue)
                    totalWays += (leftTrue + leftFalse) * (rightTrue + rightFalse)
                if string[i] == "|":
                    totalTrue += (leftTrue * rightFalse) + (leftFalse * rightTrue) + (leftTrue * rightTrue)
                    totalWays += (leftTrue + leftFalse) * (rightTrue + rightFalse)
                if string[i] == "^":
                    totalTrue += (leftTrue * rightFalse) + (leftFalse * rightTrue)
                    totalWays += (leftTrue + leftFalse) * (rightTrue + rightFalse)
                i += 1
            # if desired result is True, then return totalTrue. If False, then subtract totalTrue from totalWays to get 
            # total ways to make expression False
            # store results for this string in memo
            memo[string] = (totalTrue, totalWays - totalTrue)

        if exp_result:
            return memo[string][0]
        else:
            return memo[string][1]
    # memoization for storing repeated results for certain strings so we don't have to do them again
    memo = {}
    return helper(string, exp_result, memo)
    


class Test(unittest.TestCase):
    test_cases = [("1^0|0|1", False, 2), ("0&0&0&1^1|0", True, 10)]
    testable_functions = [evaluate]

    def test_evaluate(self):
        for f in self.testable_functions:
            for [expression, result, expected] in self.test_cases:
                a = f(expression, result)
                assert a == expected


if __name__ == "__main__":
    unittest.main()