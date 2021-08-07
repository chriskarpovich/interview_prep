"""
Write a method to compute all permutations of a string whose characters are not necessarily unique. The list of permutations should
not have duplicates.
"""
from copy import deepcopy
def get_perms(string):
    def helper(chars, string, result):
        # base case, no chars left to add
        if not chars:
            result.append("".join(string))
            return
        length = len(chars)

        # find duplicate letters in chars
        seen_chars = {}
        for i in range(length):
            # check if duplicate char
            # if it is a duplicate, then only look at it once
            # that means not calling helper more than once for it
            if chars[i] in seen_chars:
                continue
            seen_chars[chars[i]] = 1
            string_new = deepcopy(string)
            string_new.append(chars[i])
            chars_new = chars[:i] + chars[i+1:]
            helper(chars_new, string_new, result)
    chars = list(string)
    result = []
    helper(chars, [], result)
    return result

if __name__ == "__main__":
    print(get_perms("aaa"))
    print(len(set(get_perms("aaa"))))