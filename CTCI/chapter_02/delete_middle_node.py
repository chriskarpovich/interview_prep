"""
Implement an algorithm to delete a node in the middle (i.e. any node but the first and last node, not necessarily the exact middle)
of a singly linked list, given only access to that node.
Ex: Input is the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f 
"""

from linked_list import *

# def delete_middle_node(node):
#     # copy over the elements to make the list look like the final answer and make the last node None
#     while True:
#         node.value = node.next.value
#         if node.next.next == None:
#             node.next = None
#             return
#         node = node.next
#     return

def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next


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
