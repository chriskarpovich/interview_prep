# Given a string, write a function to check if it is a permutation of a palindrome. 
# Hannah -> h: 2, a: 2, n: 2
# lol -> l: 2, o: 1
# abcd -> a: 1, b: 1, c: 1, d: 1
# aaabaaa -> a: 6, b: 1

def palindrome_permute(string: str) -> bool:
    string = string.lower().replace(" ", "")
    char_dict = {}
    for char in string:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    if len([x for x in char_dict.values() if x % 2 != 0]) <= 1:
        return True
    else:
        return False


def main():
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]
    for case in test_cases:
        assert(case[1] == palindrome_permute(case[0]))

if __name__ == "__main__":
    main()