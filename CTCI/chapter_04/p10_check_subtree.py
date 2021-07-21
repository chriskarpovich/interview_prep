"""
T1 and T2 are two very large binary trees, with T1 much larger than T2. Create an algorithm to determine if T2 is a subtree of T1.
A tree T2 is a subtree of tree T1 if there exists a node n in T1 such that the subtree of n is identical to T2. That is,
if you cut off the tree at node n, the two trees would be identical.
"""
from binary_tree import Node, BinaryTree


def is_subtree(t1, t2):
    def helper(node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        # check if nodes are equal and their left and right subchildren are equal
        good = False
        if node1.value == node2.value:
            good = True
        return good and helper(node1.left, node2.left) and helper(node1.right, node2.right)
    # search every node in larger tree as starting point?
    def traverse(node):
        if node == None:
            return False
        # visit node
        if helper(node, t2.root):
            return True
        return traverse(node.left) or traverse(node.right)
    return traverse(t1.root)


if __name__ == "__main__":
    t1 = BinaryTree()
    n1 = t1.insert(1, None)
    n2 = t1.insert(2, n1)
    n3 = t1.insert(3, n1)
    n4 = t1.insert(4, n2)
    n5 = t1.insert(5, n2)
    n7 = t1.insert(7, n3)
    n8 = t1.insert(8, n4)
    t1.printTree(t1.root)

    t2 = BinaryTree()
    n40 = t2.insert(4, None)
    n80 = t2.insert(8, n40)
    n90 = t2.insert(9, n40)
    t2.printTree(t2.root)

    print(is_subtree(t1, t2))