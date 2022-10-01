"""
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or 
equal to x. If x is contained within the list, the values of x only need to be after the elements less than x. The partition element
x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
You should preserve the original relative order of the nodes in each of the two partitions.
Ex:
Input: 3->5->8->5->10->2->1 (partition = 5)
Output: 3->1->2->10->5->5->8
"""
from linked_list import *

def partition(ll, x):
    
        


def main():
    #ll = LinkedList.generate(10, 0, 99)
    ll = LinkedList(values=[25, 2])
    print(ll)
    partition(ll, ll.head.value)
    print(ll)


if __name__ == "__main__":
    main()