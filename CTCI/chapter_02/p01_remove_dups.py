"""
Write code to remove duplicates from an unsorted linked list.
"""

from linked_list import *
import time

def remove_dups(llist: LinkedList):
    data = set()
    node = llist.head
    prev = None
    while node != None:
        if node.value in data:
            # remove node since it is a duplicate
            # check if this is the last node or not to update tail of list
            if node.next == None:
                llist.tail = prev
            # update previous pointer to have correct next pointer
            prev.next = node.next
        else:
            data.add(node.value)
            prev = node
        node = node.next
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
        for _ in range(100):
            for values, expected in test_cases:
                expected = expected.copy()
                deduped = f(LinkedList(values))
                assert deduped.values() == expected

                deduped.add(5)
                expected.append(5)
                assert deduped.values() == expected

        duration = time.perf_counter() - start
        print(f"{f.__name__} {duration * 1000:.1f}ms")

if __name__ == "__main__":
    main()