"""
Write a recursive function to multiply two positive integers without using the * operator. You can use addition, subtraction, and bit shifting, but
you should minimize the number of those operations.
"""
# can also do this recursively
def multiply_add(a, b):
    result = 0
    for i in range(b):
        result += a
    return result

def multiply_bit_based(a, b):
    b_bin = bin(b)[2:]
    # O(b_bin)
    result = 0
    for i in range(len(b_bin)):
        if int(b_bin[-i-1]):
            result += (a << i)
    return result

def min_product(a, b):
    smaller = a if a < b else b
    larger = a if a > b else b
    def min_product_helper(smaller, larger):
        # base cases
        if smaller == 1:
            return larger # larger * 1 = larger
        if smaller == 0:
            return 0 # larger * 0 = 0
        # divide smaller by 2 gradually and sum left and right areas.
        s = smaller // 2
        side_1 = min_product_helper(s, larger)
        if smaller % 2 == 0:
            # divisible by 2, just return side_1 * 2
            return side_1 + side_1
        else:
            return side_1 + side_1 + larger
    return min_product_helper(smaller, larger)
    

def min_product_recursion(a, b):
    smaller = a if a < b else b
    larger = a if a > b else b
    def min_product_helper(smaller, larger):
        # base cases
        if smaller == 1:
            return larger # larger * 1 = larger
        if smaller == 0:
            return 0 # larger * 0 = 0
        # divide smaller by 2 gradually and sum left and right areas.
        s = smaller // 2
        side_1 = min_product_helper(s, larger)
        side_2 = side_1
        if smaller % 2 != 0:
            side_2 = min_product_helper(smaller-s, larger)
        return side_1 + side_2
    return min_product_helper(smaller, larger)

def min_product_memo(a, b):
    smaller = a if a < b else b
    larger = a if a > b else b
    memo = {}
    def min_product_helper(smaller, larger, memo):
        # base cases
        if smaller == 1:
            return larger # larger * 1 = larger
        if smaller == 0:
            return 0 # larger * 0 = 0
        # divide smaller by 2 gradually and sum left and right areas.
        s = smaller // 2
        # memo to store result of min_product_helper(s, larger)
        # e.g. (17, 23) --> (9, 23) + (8, 23) --> (5, 23) + (4, 23) + (4, 23) + (4, 23)
        if s not in memo:
            memo[s] = min_product_helper(s, larger, memo)
        side_1 = memo[s]
        side_2 = side_1
        if smaller % 2 != 0:
            if smaller-s not in memo:
                memo[smaller-s] = min_product_helper(smaller-s, larger, memo)
            side_2 = memo[smaller-s]
        return side_1 + side_2
    return min_product_helper(smaller, larger, memo)
    




test_cases = [(5, 6), (28, 89), (1234, 245334)]
#testable_functions = [multiply_add, multiply_bit_based, min_product]
testable_functions = [min_product_memo]


def test_min_product():
    for min_prod in testable_functions:
        for a, b in test_cases:
            print(min_prod(a, b))
            assert min_prod(a, b) == a * b


if __name__ == "__main__":
    test_min_product()