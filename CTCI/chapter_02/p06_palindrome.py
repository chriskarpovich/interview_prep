"""
Implement a function to check if a linked list is a palindrome
"""
from linked_list import *

def palindrome(llist):
    values = llist.values()
    i = 0
    j = len(values) - 1
    while i <= j:
        if values[i] != values[j]:
            return False
        i += 1
        j -= 1
    return True

def is_palindrome_runner(ll):
    fast = slow = ll.head
    stack = []

    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        top = stack.pop()

        if top != slow.value:
            return False

        slow = slow.next

    return True
    


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