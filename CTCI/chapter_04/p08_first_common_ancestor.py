"""
Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes
in a data structure. NOTE: This is not necessarily a binary search tree. 
"""

from binary_tree import BinaryTree
    


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