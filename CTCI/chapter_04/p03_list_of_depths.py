"""
Given a binary tree, design an algorithm which creates a linked list of all of the nodes at each depth (e.g. for a binary tree of depth D, you'll
have D linked lists).
"""
import sys
sys.path.append('..')
from chapter_02.linked_list import LinkedList, LinkedListNode
from binary_tree import Node
from collections import deque
    

testable_functions = [get_linked_list, create_node_list_by_depth, create_node_list_by_depth_b]

def test_create_node_list_by_depth():
    for f in testable_functions:
        node_h = Node("H")
        node_g = Node("G")
        node_f = Node("F")
        node_e = Node("E", node_g)
        node_d = Node("D", node_h)
        node_c = Node("C", None, node_f)
        node_b = Node("B", node_d, node_e)
        node_a = Node("A", node_b, node_c)
        lists = f(node_a)
        assert lists[0].values() == LinkedList([node_a]).values()
        assert lists[1].values() == LinkedList([node_b, node_c]).values()
        assert lists[2].values() == LinkedList([node_d, node_e, node_f]).values()
        assert lists[3].values() == LinkedList([node_h, node_g]).values()
if __name__ == "__main__":
    test_create_node_list_by_depth()