"""
You are given a binary tree in which each node contains an integer value (which might be positive or negative). Design an algorithm to count
the number of paths that sum to a given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).
"""
from binary_tree import BinaryTree
from collections import defaultdict

def count_sum_paths(t1, desired_sum):
    root = t1.root
    if not root:
        return None
    # brute force loop through every node in tree as starting point
    # O(NlogN) b/c N nodes in tree, each worst case O(logN) depth. nested for loop to find each node, and each node is
    # touched once for each node above it (must search to bottom of tree).
    def helper(node, desired_sum, sum=0):
        # check if node, base case
        if not node:
            return 0
        # visit node
        sum += node.value
        # check if sum is what we want and increment
        num_paths_found = 0
        if sum == desired_sum:
            num_paths_found += 1
        # recursively go to left and right
        return helper(node.left, desired_sum, sum) + helper(node.right, desired_sum, sum) + num_paths_found

    total_paths_found = 0
    def traverse_each_node(node):
        if not node:
            return 0
        # visit node by traversing whole tree
        # recursively go to left and right child
        # sum all total paths found
        return helper(node, desired_sum) + traverse_each_node(node.left) + traverse_each_node(node.right)
    
    return traverse_each_node(root)

# starting at root node, there are N unique paths in the tree
# O(N) time complexity to traverse a binary tree
# running_sum(i-1) + target_sum = running_sum(j)
def count_sum_paths_optimized(t1, target_sum):
    root = t1.root
    if not root:
        return None
    def helper(node, target_sum, running_sum=0, hashtable=None):
        if not node:
            return 0
        # visit node
        running_sum += node.value
        # add our running_sum to the hashtable count
        hashtable[running_sum] += 1
        # check if our running_sum is equal to target_sum and increment if it does
        total_sum = 0
        if running_sum == target_sum:
            total_sum += 1
        # see of we have seen running_sum(i-1) before and return number, if the key doesn't exist we return zero by default
        total_sum += hashtable.get(running_sum - target_sum, 0)
        # recursively go down left and right paths
        total_sum += (helper(node.left, target_sum, running_sum, hashtable) + helper(node.right, target_sum, running_sum, hashtable))
        # decrement our running sum count before we return
        hashtable[running_sum] -= 1
        return total_sum

    hashtable = defaultdict(int)
    return helper(root, target_sum, running_sum=0, hashtable=hashtable)

def return_all_paths(t1, desired_sum):
    root = t1.root
    if not root:
        return None
    # first get all unique paths from root (arrays) down to leaf nodes.
    def helper(node):
        # visit node
        if node.left and node.right:
            left_arrays = helper(node.left)
            left_arrays = [x + [node.value] for x in left_arrays]
            right_arrays = helper(node.right)
            right_arrays = [x + [node.value] for x in right_arrays]
            return right_arrays + left_arrays
        elif node.left:
            left_arrays = helper(node.left)
            left_arrays = [x + [node.value] for x in left_arrays]
            return left_arrays
        elif node.right:
            right_arrays = helper(node.right)
            right_arrays = [x + [node.value] for x in right_arrays]
            return right_arrays
        else:
            # leaf node, return own value
            return [[node.value]]
    return helper(root)
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