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

def find_bst_sequences(bst):
    root = bst.root
    nodes_depths_l = {}
    nodes_depths_r = {}
    def get_nodes_at_depth(node, node_dict, depth=1):
        if node == None:
            return
        if depth not in node_dict:
            node_dict[depth] = []
        node_dict[depth].append(node.value)          
        get_nodes_at_depth(node.left, node_dict, depth+1)
        get_nodes_at_depth(node.right, node_dict, depth+1)
    get_nodes_at_depth(root.left, nodes_depths_l)
    get_nodes_at_depth(root.right, nodes_depths_r)

    print(nodes_depths_l)
    print(nodes_depths_r)

    all_left_perms, all_right_perms = [], []
    for dictionary in nodes_depths_l, nodes_depths_r:
        prev = []
        for key in dictionary:
            perm = permutations(dictionary[key])
            curr_lists = []
            for i in list(perm):
                for j in prev:
                    new_list = []
                    new_list.extend(prev)
                    new_list.extend(list(i))
                    curr_lists.append(new_list)
                if not prev:
                    new_list = []
                    curr_lists.extend(list(i))
            prev = curr_lists
        if dictionary == nodes_depths_l:
            all_left_perms.extend(curr_lists)
        elif dictionary == nodes_depths_r:
            all_right_perms.extend(curr_lists)
    if len(all_right_perms) == 1:
        all_right_perms = [all_right_perms]
    if len(all_left_perms) == 1:
        all_left_perms = [all_left_perms]
    print(all_left_perms)
    print(all_right_perms)



    def weave(first, second, prefix, results):
        if len(first) == 0 or len(second) == 0:
            result = prefix.copy()
            result.extend(first)
            result.extend(second)
            results.append(result)
            return results

        head = first[0]
        prefix.append(head)
        results = weave(first[1:], second, prefix, results)
        prefix.pop()
        head = second[0]
        prefix.append(head)
        results = weave(first, second[1:], prefix, results)
        prefix.pop()
        return results

    sequences = []
    for right in all_right_perms:
        for left in all_left_perms:
            weave(right, left, [root.value], sequences)
    return sequences

def find_bst_sequences_concise(bst):
    if not bst.root:
        return []
    return helper(bst.root)


def helper(node):
    if not node:
        return [[]]
    # left and right sequences of children nodes on left and right
    right_sequences = helper(node.right)
    left_sequences = helper(node.left)
    sequences = []

    for right in right_sequences:
        for left in left_sequences:
            # weave in left and right subsequences with first value being the parent node
            sequences = weave(left, right, [node.value], sequences)
            print(sequences)
    return sequences


def weave(first, second, prefix, results):
    if len(first) == 0 or len(second) == 0:
        result = prefix.copy()
        result.extend(first)
        result.extend(second)
        results.append(result)
        return results

    head = first[0]
    prefix.append(head)
    results = weave(first[1:], second, prefix, results)
    prefix.pop()
    head = second[0]
    prefix.append(head)
    results = weave(first, second[1:], prefix, results)
    prefix.pop()
    return results


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
