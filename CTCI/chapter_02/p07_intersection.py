"""
Given two singly linked lists, determine if the two lists intersect. Return the intersecting node. Note the intersection is defined
based on reference, not value. That is, if the kth node of the first linked list is the exact same node by reference as the jth
node of the second linked list, then they are intersecting.
"""
from linked_list import *

def intersection(ll1, ll2):
    pass
    
        
        

def main():
    shared = LinkedList()
    shared.add_multiple([1, 2, 3, 4])

    a = LinkedList([10, 11, 12, 13, 14, 15])
    b = LinkedList([20, 21, 22])

    a.tail.next = shared.head
    a.tail = shared.tail
    b.tail.next = shared.head
    b.tail = shared.tail
    # results in a-->shared and b-->shared so both linked to head of shared

    # should be 1
    assert intersection_smaller(a, b).value == 1
    print(intersection_smaller(a, b).value)

if __name__ == "__main__":
    main()