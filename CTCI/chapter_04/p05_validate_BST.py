"""
Implement a function to check if a binary tree is a BST.
"""

from binary_tree import BinarySearchTree, BinaryTree

def is_binary_search_tree(tree):
    root = tree.root
    if not root:
        return False

    def helper(node):
        if not node:
            return (True, [])

        cond_left, all_left = helper(node.left)
        cond_right, all_right = helper(node.right)
        
        if (cond_left and cond_right):
            if all_left and all_right:
                if all(x <= node.value for x in all_left) and all(x > node.value for x in all_right):
                    return (True, all_left+all_right+[node.value])
                else:
                    return (False, all_left+all_right+[node.value])
            elif all_left:
                if all(x <= node.value for x in all_left):
                    return (True, all_left+[node.value])
                else:
                    (False, all_left+[node.value])
            elif all_right:
                if all(x > node.value for x in all_right):
                    return (True, all_right+[node.value])
                else:
                    return (False, all_right+[node.value])
            else:
                return (True, [node.value])
        else:
            return (False, all_left+all_right+[node.value])
    cond, values = helper(root)
    return cond

def is_binary_search_tree_concise(tree):
    return _is_bst(tree.root)


def _is_bst(node, min_val=None, max_val=None):
    if not node:
        return True
    if (min_val and node.value < min_val) or (max_val and node.value >= max_val):
        return False
    return _is_bst(node.left, min_val, node.value) and _is_bst(node.right, node.value, max_val)
        



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


