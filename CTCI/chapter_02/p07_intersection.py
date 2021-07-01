"""
Given two singly linked lists, determine if the two lists intersect. Return the intersecting node. Note the intersection is defined
based on reference, not value. That is, if the kth node of the first linked list is the exact same node by reference as the jth
node of the second linked list, then they are intersecting.
"""
from linked_list import *

def intersection(ll1, ll2):
    node1 = ll1.head
    node2 = ll2.head
    runner1 = ll1.head
    # have runner go along ll1 and compare against each element of ll2
    # only need to compare len(smaller_list) nodes for intersection
    while node2 != None:
        runner1 = node1
        while runner1 != None:
            if node2 == runner1:
                # return intersecting node
                return node2
            runner1 = runner1.next
        node2 = node2.next
    return None

def intersection_smaller(ll1, ll2):
    smaller_list = ll1 if len(ll1) < len(ll2) else ll2
    larger_list = ll1 if len(ll1) > len(ll2) else ll2

    diff = len(larger_list) - len(smaller_list)
    large_node = larger_list.head
    small_node = smaller_list.head
    # advance large list to size of small list
    for _ in range(diff):
        large_node = large_node.next

    while large_node != None and small_node != None:
        if large_node == small_node:
            return large_node
        large_node = large_node.next
        small_node = small_node.next
    return None
    
        
        

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