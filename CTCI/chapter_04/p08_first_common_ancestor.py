"""
Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes
in a data structure. NOTE: This is not necessarily a binary search tree. 
"""

from binary_tree import BinaryTree

def first_common_ancestor(node1, node2):
    if not node1 or not node2:
        return None
    # first make sure we start on the same depth
    depth_1 = get_depth(node1)
    depth_2 = get_depth(node2)
    #print(depth_1, depth_2)
    if depth_1 > depth_2:
        # move node_1 up in the tree to node_2
        while depth_1 > depth_2:
            node1 = node1.parent
            depth_1 -= 1
    elif depth_2 > depth_1:
        # move node_2 up in the tree to node_1
        while depth_2 > depth_1:
            node2 = node2.parent
            depth_2 -= 1
    # starting at same depth, check each iter if nodes are same. if not, move them up one parent
    while node1 and node2 and node1 != node2:
        node1 = node1.parent
        node2 = node2.parent
    return node1

    
def get_depth(node):
    depth = 0
    while node.parent != None:
        node = node.parent
        depth += 1
    return depth
    


if __name__ == "__main__":
    t = BinaryTree()
    n1 = t.insert(1, None)
    n2 = t.insert(2, n1)
    n3 = t.insert(3, n1)
    n4 = t.insert(4, n2)
    n5 = t.insert(5, n2)
    n7 = t.insert(7, n3)
    n8 = t.insert(8, n4)
    t.printTree(n1)

    ancestor = first_common_ancestor(n2, n8)
    print(ancestor.value)