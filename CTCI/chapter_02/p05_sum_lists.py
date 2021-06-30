"""
You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order,
such that the 1's digit is at the head of the list. Write a function that adds th two numbers and returns the sum as a 
linked list.
Ex: 
Input: (7->1->6) + (5->9->2), so 617 + 295
Output: 2->1->9, so 912.

Follow-up: suppose the digits are stored in forward order. Repeat the above problem.
Ex:
Input: (6->1->7) + (2->9->5)
Output: (9->1->2)
"""
from linked_list import *

def sum_lists(ll_a, ll_b, reverse = False):
    ll_sum = LinkedList()
    if reverse:
        ll_a = reverse_ll(ll_a)
        ll_b = reverse_ll(ll_b)
    node_1 = ll_a.head
    node_2 = ll_b.head
    carry_over = 0
    while node_1 is not None or node_2 is not None:
        if node_1 is None:
            node_1_value = 0
        else:
            node_1_value = node_1.value
        if node_2 is None:
            node_2_value = 0
        else:
            node_2_value = node_2.value
        val_sum = node_1_value + node_2_value + carry_over
        if val_sum < 10:
            ll_sum.add(val_sum)
            carry_over = 0
        else:
            ll_sum.add(val_sum % 10)
            carry_over = 1
        if node_1 is not None:
            node_1 = node_1.next
        if node_2 is not None:
            node_2 = node_2.next
    if reverse:
        ll_sum = reverse_ll(ll_sum)
    return ll_sum
        
def reverse_ll(ll):
    values = ll.values()[::-1]
    ll_rev = LinkedList(values)
    return ll_rev


def main():
    test_cases = (
    # all values can either be list of integer or integers
    # a, b, expected_sum
    ([7, 1, 6], [5, 9, 2], [2, 1, 9]),
    ([0], [0], [0]),
    ([3, 2, 1], [3, 2, 1], [6, 4, 2])
)   
    for case in test_cases:
        ll_a = LinkedList(values=case[0][::-1])
        ll_b = LinkedList(values=case[1][::-1])
        ll_c = LinkedList(values=case[2][::-1])
        assert(print(sum_lists(ll_a, ll_b, reverse=True)) == print(ll_c))
    # ll_a = LinkedList.generate(4, 1, 9)
    # ll_b = LinkedList.generate(3, 1, 9)
    # print(ll_a)
    # print(ll_b)
    # print(sum_lists(ll_a, ll_b))

if __name__ == "__main__":
    main()
