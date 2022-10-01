"""
Implement a function to check if a binary tree is a BST.
"""

from binary_tree import BinarySearchTree, BinaryTree

# def is_binary_search_tree_concise(tree):
#     node = tree.root
#     def dfs(node, minVal, maxVal):
#         if not node:
#             return True
#         # if we go left, then node.value becomes maxVal. if we go right, then node.value becomes minVal
#         return node.value > minVal and node.value < maxVal and dfs(node.left, minVal, node.value) and dfs(node.right, node.value, maxVal)
#     return dfs(node, float("-inf"), float("inf"))

def is_binary_search_tree_concise(tree):
    node = tree.root
    def dfs(node, minVal, maxVal):
        if not node:
            return True
        if (minVal and node.value <= minVal) or (maxVal and node.value >= maxVal):
            return False
        # if we go left, then node.value becomes maxVal. if we go right, then node.value becomes minVal
        return dfs(node.left, minVal, node.value) and dfs(node.right, node.value, maxVal)
    return dfs(node, None, None)


def test_is_binary_search_tree():
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)

    t = BinaryTree()
    n1 = t.insert(5, None)
    n2 = t.insert(4, n1)
    n3 = t.insert(6, n1)
    n4 = t.insert(3, n2)
    t.insert(6, n2)
    t.insert(5, n3)
    t.insert(2, n4)

    print(1)
    t.printTree(t.root)
    assert not is_binary_search_tree_concise(t)
    print(2)
    bst.printTree(bst.root)
    assert is_binary_search_tree_concise(bst)
    
if __name__ == "__main__":
    test_is_binary_search_tree()


