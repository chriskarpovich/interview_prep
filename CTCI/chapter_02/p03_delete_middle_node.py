"""
Implement an algorithm to delete a node in the middle (i.e. any node but the first and last node, not necessarily the exact middle)
of a singly linked list, given only access to that node.
Ex: Input is the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f 
"""

from linked_list import *

def delete_middle_node(node):
    # change the value of the node
    while node.next:
        node.value = node.next.value
        # delete the last node, since it's not necessary
        if not node.next.next:
            node.next = None
        else:
            node = node.next


def main():
    ll = LinkedList()
    ll.add_multiple([1])
    middle_node = ll.add(5)
    ll.add_multiple([7, 8])

    print(ll)
    delete_middle_node(middle_node)
    print(ll)


if __name__ == "__main__":
    main()
