"""
Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined such that the
heights of the two subtrees of any node never differ by more than one.
"""

class BinaryNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

def check_balanced(node):
    def dfs(node):
        if not node:
            return 0, True
        left, left_balanced = dfs(node.left)
        right, right_balanced = dfs(node.right)
        balanced = True
        if not left_balanced or not right_balanced or abs(left - right) > 1:
            balanced = False
        return max(left, right) + 1, balanced
    _, balanced = dfs(node)
    return balanced

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
testable_functions = [check_balanced]


def test_is_balanced():
    for tree_gen, expected in test_cases:
        for is_balanced in testable_functions:
            error_msg = f"{is_balanced.__name__} failed on {tree_gen.__name__}"
            res = is_balanced(tree_gen())
            print(expected, res)
            assert res == expected, error_msg


if __name__ == "__main__":
    test_is_balanced()