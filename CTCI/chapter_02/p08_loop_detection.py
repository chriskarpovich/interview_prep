"""
Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.
A circular linked list is a linked list in which a node's next pointer points to an earlier node to make a loop in the linked list.
Ex:
A -> B -> C -> D -> E -> C (same C as earlier)
returns C
"""

from linked_list import *

def loop_detection_easy(ll):
    pass


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