# Can insert, remove or replace character in string. Given two strings, write a function to check if they are one edit (or zero edits) away
def one_away(str1: str, str2: str) -> bool:
    if abs(len(str1) - len(str2)) > 1:
        return False
    i = j = 0
    if len(str1) > len(str2):
        shorter = str2
        longer = str1
    else:
        shorter = str1
        longer = str2
    edited = False
    while i < len(longer) and j < len(shorter):
        if longer[i] != shorter[j]:
            if edited:
                return False
            edited = True
            if len(longer) != len(shorter):
                i += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1

    return True



            

def main():
    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),
    ]
    for case in test_cases:
        assert(one_away(case[0], case[1]) == case[2])

if __name__ == "__main__":
    main()