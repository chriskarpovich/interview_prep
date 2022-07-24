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
    return isSubstring(s1, s2+s2)

def string_rotation_2(s1, s2):
    if len(s1) != len(s2):
        return False
    j = 0
    while j < len(s2):
        i = 0
        k = j
        while i < len(s1) and s1[i] == s2[k]:
            i += 1
            k += 1
            k = k % len(s2)
        if i == len(s1):
            return True
        j += 1
    return False
def string_rotation_3(s1, s2):
    if len(s1) != len(s2):
        return False
    
    i = 0
    while i < len(s1):
        # walk along s1 first
        if isSubstring(s1[i:], s2):
            # find end index of current string
            new_ind = len(s1) - i
            # walk along s2 now
            l = 0
            for j in range(new_ind, len(s2)):
                if s2[j] != s1[l]:
                    break
                l += 1
            if l == i:
                return True
        i += 1
    return False


def main():
    test_cases = [
        ("waterbottle", "erbottlewat", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False),
        ("treetoo", "ootreet", True),
    ]
    for case in test_cases:
        assert(string_rotation(case[0], case[1]) == case[2])
        assert(string_rotation_2(case[0], case[1]) == case[2])
        assert(string_rotation_3(case[0], case[1]) == case[2])

if __name__ == "__main__":
    main()
        