# Can insert, remove or replace character in string. Given two strings, write a function to check if they are one edit (or zero edits) away

def one_away(str1: str, str2: str) -> bool:
    if str1 == str2:
        return True
    # check if they differ by more than one character
    elif abs(len(str1) - len(str2)) > 1:
        return False

    # substitution of a character
    if len(str1) == len(str2):
        wrong = 0
        for ind in range(len(str1)):
            if str1[ind] != str2[ind]:
                wrong += 1
        if wrong > 1:
            return False
        else:
            return True
    
    # insertion/deletion of a character
    if len(str1) > len(str2):
        print(str1, str2)
        i, j = 0, 0
        edited = False
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                i += 1
                j += 1
            else:
                i += 1
                if edited:
                    return False
                edited = True
        return True

    elif len(str2) > len(str1):
        print(str1, str2)
        i, j = 0, 0
        edited = False
        while i < len(str2) and j < len(str1):
            if str2[i] == str1[j]:
                i += 1
                j += 1
            else:
                i += 1
                if edited:
                    return False
                edited = True
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