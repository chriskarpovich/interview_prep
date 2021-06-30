"""
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or 
equal to x. If x is contained within the list, the values of x only need to be after the elements less than x. The partition element
x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
Ex:
Input: 3->5->8->5->10->2->1 (partition = 5)
Output: 3->1->2->10->5->5->8
"""
from linked_list import *

def partition(ll, x):

    node = ll.head.next
    prev = ll.head
    while node != None:
        if node.value < x:
            # set next_node
            next_node = node.next
            # set prev node link to next node
            prev.next = node.next
            # check if curr node is tail and set prev node to tail
            if node.next == None:
                ll.tail = prev
            # set head to curr node and link curr node next to old head
            node.next = ll.head
            ll.head = node
        else:
            next_node = node.next
            prev = node
        node = next_node
        


def main():
    #ll = LinkedList.generate(10, 0, 99)
    ll = LinkedList(values=[25, 2])
    print(ll)
    partition(ll, ll.head.value)
    print(ll)


if __name__ == "__main__":
    main()