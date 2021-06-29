# Assume you havea method isSubstring which checks if one word is a substring of another. Given two strings, s1, and s2,
# write code to check if s2 is a rotation of s1 using only one call to isSubstring.
# Ex: waterbottle is a rotation of erbottlewat.

def isSubstring(s1, s2):
    if s1 in s2:
        return True
    else:
        return False
# s2 is the rotated string, s1 is normal
def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    # walk along s1 first
    for i in range(len(s1)):
        if s1[i] != s2[0] and isSubstring(s1[i:], s2):
            new_ind = len(s1) - i
            # walk along s2 now
            for j in range(new_ind, len(s1)):
                if s1[0] != s2[j]:
                    break
            return True
    return False

def string_rotation_easier(s1, s2):
    if len(s1) == len(s2) != 0:
        return s2 in s1 * 2
    return False



def main():
    test_cases = [
        ("waterbottle", "erbottlewat", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False),
    ]
    for case in test_cases:
        assert(string_rotation(case[0], case[1]) == case[2])

if __name__ == "__main__":
    main()
        