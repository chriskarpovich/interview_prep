"""
Given a binary tree, design an algorithm which creates a linked list of all of the nodes at each depth (e.g. for a binary tree of depth D, you'll
have D linked lists).
"""
import sys
sys.path.append('..')
from chapter_02.linked_list import LinkedList, LinkedListNode
from binary_tree import Node
from collections import deque

def list_of_depths(node, desired_depth, depth, ll):
    if node is None:
        return
    if desired_depth == depth:
        # return nodes at this level
        ll.add(node)
    else:
        list_of_depths(node.left, desired_depth, depth+1, ll)
        list_of_depths(node.right, desired_depth, depth+1, ll)

def maxDepth(node):
    if node is None:
        return -1
    else:
        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
 
        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1

def get_linked_list(node):
    tree_depth = maxDepth(node)
    lists = []
    for i in range(0, tree_depth+1):
        ll = LinkedList()
        list_of_depths(node=node, desired_depth=i, depth=0, ll=ll)
        lists.append(ll)
    return lists

def create_node_list_by_depth(root):
    if root == None:
        return []
    # Using BFS
    queue = deque()
    # append root node and level
    queue.append((root, 0))
    depth_list = {}
    while(len(queue) > 0):
        # dequeue and visit node
        node, level = queue.popleft()
        if level not in depth_list:
            depth_list[level] = LinkedList()
        depth_list[level].add(node)
        # add left and right nodes and levels to queue if not None
        if node.left is not None:
            queue.append((node.left, level+1))
        if node.right is not None:
            queue.append((node.right, level+1))
    return [depth_list[key] for key in depth_list]

def create_node_list_by_depth_b(root):
    # iterative solution
    curr = root
    if curr is None:
        return []
    level = 0
    result = [LinkedList()]
    result[level].add(curr)

    while len(result[level]) > 0:
        result.append(LinkedList())
        for linked_list_node in result[level]:
            if linked_list_node.value.left:
                result[level+1].add(linked_list_node.value.left)
            if linked_list_node.value.right:
                result[level+1].add(linked_list_node.value.right)
        level += 1
    return result[:-1]



    

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