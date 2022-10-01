"""
T1 and T2 are two very large binary trees, with T1 much larger than T2. Create an algorithm to determine if T2 is a subtree of T1.
A tree T2 is a subtree of tree T1 if there exists a node n in T1 such that the subtree of n is identical to T2. That is,
if you cut off the tree at node n, the two trees would be identical.
"""
from binary_tree import Node, BinaryTree

class ComparableTreeNode(Node):
    def __eq__(self, other):
        if not isinstance(other, ComparableTreeNode):
            return False
        return (self.value == other.value and self.left == other.left and self.right == other.right)



class BinaryTreeAlternative(BinaryTree):
    NodeCls = ComparableTreeNode

if __name__ == "__main__":
    t1 = BinaryTreeAlternative()
    n1 = t1.insert(1, None)
    n2 = t1.insert(2, n1)
    n3 = t1.insert(3, n1)
    n4 = t1.insert(4, n2)
    n5 = t1.insert(5, n2)
    n7 = t1.insert(7, n3)
    n8 = t1.insert(8, n4)
    t1.printTree(t1.root)

    t2 = BinaryTreeAlternative()
    n40 = t2.insert(4, None)
    n80 = t2.insert(8, n40)
    #n90 = t2.insert(9, n40)
    t2.printTree(t2.root)

    print(is_subtree_alternate(t1, t2))