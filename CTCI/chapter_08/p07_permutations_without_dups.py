"""
Write a method to compute all permutations of a string of unique characters.
"""
from copy import deepcopy
def get_perms(string):
    def helper(chars, string, result):
        # base case, no chars left to add, 
        if not chars:
            result.append("".join(string))
            return
        length = len(chars)
        for i in range(length):
            string_new = deepcopy(string)
            string_new.append(chars[i])
            chars_new = chars[:i] + chars[i+1:]
            helper(chars_new, string_new, result)
    chars = list(string)
    result = []
    helper(chars, [], result)
    return result


if __name__ == "__main__":
    print(get_perms("abc"))
    print(len(get_perms("abc")))
