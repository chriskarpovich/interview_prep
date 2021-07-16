"""
Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.
"""
from binary_tree import Node
import math

def array_to_binary_tree(array, L, R):
    # base case
    if R < L:
        return None
    mid = math.floor((L+R)/2)

    node = Node(value=array[mid])
    node.left = array_to_binary_tree(array, L, mid-1)
    node.right = array_to_binary_tree(array, mid+1, R)

    return node


def printTree(node, level=0):
    if node != None:
        printTree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.value)
        printTree(node.left, level + 1)


if __name__ == "__main__":
    test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
    node = array_to_binary_tree(test_array, 0, len(test_array) - 1)
    #print(node)
    printTree(node)
