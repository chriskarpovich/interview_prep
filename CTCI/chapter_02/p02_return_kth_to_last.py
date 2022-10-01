"""
Implement an algorithm to find the kth to last element of a singly linked list.
"""

from linked_list import *

def kth_to_last(llist, k):
    head = LinkedListNode(value=None)
    head.next = llist.head
    node = head.next
    length = 0
    while node:
        length += 1
        node = node.next
    node = head.next

    while node and length != k:
        length -= 1
        node = node.next
    return node
    


def main():
    test_cases = (
    # list, k, expected
    ((10, 20, 30, 40, 50), 1, 50),
    ((10, 20, 30, 40, 50), 5, 10),
    ((1,), 1, 1),
)

    for linked_list_values, k, expected in test_cases:
        ll = LinkedList(linked_list_values)
        val = kth_to_last(ll, k).value
        print(val)
        assert val == expected

if __name__ == "__main__":
    main()