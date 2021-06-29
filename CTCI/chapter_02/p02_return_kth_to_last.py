"""
Implement an algorithm to find the kth to last element of a singly linked list.
"""

from linked_list import *

def kth_to_last(llist, k):
    node = llist.head
    i = 0
    kth_index = len(llist) - k
    while node != None:
        if i == kth_index:
            return node
        node = node.next
        i += 1
    return None


def main():
    test_cases = (
    # list, k, expected
    ((10, 20, 30, 40, 50), 1, 50),
    ((10, 20, 30, 40, 50), 5, 10),
)

    for linked_list_values, k, expected in test_cases:
        ll = LinkedList(linked_list_values)
        assert kth_to_last(ll, k).value == expected

if __name__ == "__main__":
    main()