"""
A BST was created by traversing through an array from left to right and inserting each element. Given a BST with distinct elements,
print all possible arrays that could have led to this tree.
Ex: 
    2
1       3
Output: {2, 1, 3}, {2, 3, 1}
"""
from binary_tree import BinarySearchTree
from itertools import permutations

testable_functions = [find_bst_sequences_concise]

def test_find_bst_sequences():
    for find_bst in testable_functions:
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        sequences = find_bst(bst)
        assert [2, 1, 3] in sequences
        assert [2, 3, 1] in sequences
        assert len(sequences) == 2


def example():
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    # bst.insert(11);
    # bst.insert(14);
    bst.printTree(bst.root)
    sequences = find_bst_sequences_concise(bst)
    #print(sequences)


if __name__ == "__main__":
    example()
