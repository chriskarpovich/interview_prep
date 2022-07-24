# Given a string, write a function to check if it is a permutation of a palindrome. 
# Hannah -> h: 2, a: 2, n: 2
# lol -> l: 2, o: 1
# abcd -> a: 1, b: 1, c: 1, d: 1
# aaabaaa -> a: 6, b: 1

def palindrome_permute(string: str) -> bool:
    # don't consider whitespace or uppercase
    # all even or all even + 1 odd to be a permutation of a palindrome
    char_ct = dict()
    string = string.lower().replace(" ", "")
    for char in string:
        if char not in char_ct:
            char_ct[char] = 0
        char_ct[char] += 1
    seen_odd = False
    for key in char_ct:
        if char_ct[key] % 2 != 0:
            if not seen_odd:
                seen_odd = True
            else:
                return False
    return True


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