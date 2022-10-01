"""
Implement a function to check if a linked list is a palindrome
"""
from linked_list import *

def palindrome(llist):
    pass
    


def main():
    test_cases = [
        ([1, 2, 3, 4, 3, 2, 1], True),
        ([1], True),
        (["a", "a"], True),
        ("aba", True),
        ([], True),
        ([1, 2, 3, 4, 5], False),
        ([1, 2], False),
        ([1, 2, 2, 1], True)
    ]
    for case in test_cases:
        assert(palindrome(LinkedList(case[0])) == case[1])
        print(palindrome(LinkedList(case[0])), case[1])

if __name__ == "__main__":
    main()