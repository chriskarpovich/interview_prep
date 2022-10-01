"""
You are given a binary tree in which each node contains an integer value (which might be positive or negative). Design an algorithm to count
the number of paths that sum to a given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).
"""
from binary_tree import BinaryTree
from collections import defaultdict



if __name__ == "__main__":
    t1 = BinaryTree()
    n1 = t1.insert(10, None)
    n2 = t1.insert(5, n1)
    n3 = t1.insert(-3, n1)
    n4 = t1.insert(3, n2)
    n5 = t1.insert(2, n2)
    n6 = t1.insert(3, n4)
    n7 = t1.insert(-2, n4)
    n8 = t1.insert(1, n5)
    n9 = t1.insert(11, n3)
    n10 = t1.insert(8, n9)
    n11 = t1.insert(-8, n10)
    # t1.printTree(t1.root)
    print(count_sum_paths(t1, 8))
    print(count_sum_paths(t1, 6))
    print(count_sum_paths_optimized(t1, 8))
    print(count_sum_paths_optimized(t1, 6))