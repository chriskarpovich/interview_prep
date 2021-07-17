"""
Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined such that the
heights of the two subtrees of any node never differ by more than one.
"""

class BinaryNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

def check_balanced_parent(root):
    difference_list = []
    def check_balanced(root, difference_list):
        # try DFS for each node in tree
        if root == None:
            return 0
        left_depth = check_balanced(root.left, difference_list)
        right_depth = check_balanced(root.right, difference_list)
        difference_list.append(abs(left_depth-right_depth))
        return max(left_depth, right_depth)+1
    check_balanced(root, difference_list)
    if any(x > 1 for x in difference_list):
        return False
    else:
        return True
def check_balanced_parent_2(root):
    def check_balanced_2(root):
        # try DFS for each node in tree
        if root == None:
            return (True, 0)
        is_balanced_left, left_depth = check_balanced_2(root.left)
        is_balanced_right, right_depth = check_balanced_2(root.right)
        height = max(left_depth, right_depth)+1
        diff = abs(left_depth - right_depth)

        if not(is_balanced_left and is_balanced_right) or diff > 1:
            return (False, height)
        else:
            return (True, height)
    cond, height = check_balanced_2(root)
    return cond





def _gen_balanced_1():
    root = BinaryNode(1)
    root.left = BinaryNode(2)
    return root


def _gen_balanced_2():
    root = BinaryNode(7)
    root.left = BinaryNode(2)
    root.left.left = BinaryNode(4)
    root.right = BinaryNode(3)
    root.right.left = BinaryNode(8)
    root.right.right = BinaryNode(9)
    root.right.right.right = BinaryNode(10)
    return root


def _gen_unbalanced_1():
    root = BinaryNode(1)
    root.left = BinaryNode(2)
    root.left.left = BinaryNode(4)
    root.left.right = BinaryNode(5)
    root.left.right.right = BinaryNode(6)
    root.left.right.right.right = BinaryNode(7)
    root.right = BinaryNode(3)
    root.right.left = BinaryNode(8)
    root.right.right = BinaryNode(9)
    root.right.right.right = BinaryNode(10)
    root.right.right.right.right = BinaryNode(11)
    return root


def _gen_unbalanced_2():
    tree = BinaryNode(1)
    tree.left = BinaryNode(2)
    tree.right = BinaryNode(9)
    tree.right.left = BinaryNode(10)
    tree.left.left = BinaryNode(3)
    tree.left.right = BinaryNode(7)
    tree.left.right.right = BinaryNode(5)
    tree.left.left.left = BinaryNode(6)
    tree.left.right.left = BinaryNode(12)
    tree.left.right.left.left = BinaryNode(16)
    tree.left.right.left.right = BinaryNode(0)
    return tree


test_cases = [
    (_gen_balanced_1, True),
    (_gen_balanced_2, True),
    (_gen_unbalanced_1, False),
    (_gen_unbalanced_2, False),
]

#testable_functions = [is_balanced_v1, is_balanced_v2]
testable_functions = [check_balanced_parent, check_balanced_parent_2]


def test_is_balanced():
    for tree_gen, expected in test_cases:
        for is_balanced in testable_functions:
            error_msg = f"{is_balanced.__name__} failed on {tree_gen.__name__}"
            assert is_balanced(tree_gen()) == expected, error_msg


if __name__ == "__main__":
    test_is_balanced()