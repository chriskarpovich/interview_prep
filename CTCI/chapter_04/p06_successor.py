"""
Write an algorithm to find the "next" node (i.e. in-order successor) of a given node in a BST. You may assume each node has a link to
its parent.
"""
from binary_tree import BinarySearchTree

def in_order_successor(query):
    # in-order traversal of a tree
    # find root
    root = query
    while root.parent != None:
        root = root.parent
    def helper(node):
        if not node:
            return
        left = helper(node.left)
        if left:
            return left
        # visit node
        if node.value > query.value:
            return node
        right = helper(node.right)
        if right:
            return right
    return helper(root)

def in_order_successor_iter(query):
    # return leftmost node on the right branch
    if query.right:
        node = query.right
        while node.left:
            node = node.left
        return node
    # if no right node, then go up from parent until you hit a left
    else:
        ancestor = query.parent
        child = query
        while ancestor and not ancestor.left == child:
            child = ancestor
            ancestor = ancestor.parent
        return ancestor
    



def test_in_order_successor():
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)

    # Test all nodes
    inputs = [5, 9, 11, 12, 14, 20, 25]
    outputs = inputs[1:]
    outputs.append(None)

    for x, y in zip(inputs, outputs):
        test = bst.get_node(x)
        succ = in_order_successor_iter(test)
        if succ is not None:
            assert succ.value == y
        else:
            assert succ == y


if __name__ == "__main__":
    test_in_order_successor()