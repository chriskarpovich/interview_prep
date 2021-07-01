"""
Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.
A circular linked list is a linked list in which a node's next pointer points to an earlier node to make a loop in the linked list.
Ex:
A -> B -> C -> D -> E -> C (same C as earlier)
returns C
"""

from linked_list import *

def loop_detection_easy(ll):
    if ll.tail == None or ll.tail.next == None:
        return None
    else:
        return ll.tail.next

def loop_detection(ll):
    fast = slow = ll.head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break

    if fast is None or fast.next is None:
        return None

    slow = ll.head
    while fast is not slow:
        fast = fast.next
        slow = slow.next

    return fast


def main():
    looped_list = LinkedList(["A", "B", "C", "D", "E"])
    loop_start_node = looped_list.head.next.next
    looped_list.tail.next = loop_start_node
    tests = [
        (LinkedList(), None),
        ((LinkedList((1, 2, 3))), None),
        (looped_list, loop_start_node),
    ]

    for ll, expected in tests:
        assert loop_detection(ll) == expected

if __name__ == "__main__":
    main()