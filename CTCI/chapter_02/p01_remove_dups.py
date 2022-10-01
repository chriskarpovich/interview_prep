"""
Write code to remove duplicates from an unsorted linked list.
"""

from linked_list import *
import time

def remove_dups(llist: LinkedList):
    seen = dict()
    head = LinkedListNode(value=None)
    head.next = llist.head
    node = head

    while node and node.next:
        if node.next.value in seen:
            node.next = node.next.next
        else:
            seen[node.next.value] = node.next.value
            node = node.next
    llist.head = head.next
    return llist


testable_functions = [remove_dups]

test_cases = (
    ([], []),
    ([1, 1, 1, 1, 1, 1], [1]),
    ([1, 2, 3, 2], [1, 2, 3]),
    ([1, 2, 2, 3], [1, 2, 3]),
    ([1, 1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [1, 2, 3]),
)   

def main():
    

    for f in testable_functions:
        start = time.perf_counter()
        for _ in range(1):
            for values, expected in test_cases:
                expected = expected.copy()

                deduped = f(LinkedList(values))
                print(deduped.values())
                assert deduped.values() == expected

                # deduped.add(5)
                # expected.append(5)
                # print(deduped.values())
                # assert deduped.values() == expected

        duration = time.perf_counter() - start
        print(f"{f.__name__} {duration * 1000:.1f}ms")

if __name__ == "__main__":
    main()