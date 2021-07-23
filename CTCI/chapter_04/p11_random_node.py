"""
You are implementing a binary tree class from scratch which, in addition, to insert(), find(), and delete(), has a method getRandomNode(),
which returns a random node from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm for getRandomNode(),
and explain how you would implement the rest of the methods.
"""

"""
3 cases for deletion.
1) Node to be deleted is the leaf: Simply remove from the tree. 
2) Node to be deleted has only one child: Copy the child to the node and delete the child 
3) Node to be deleted has two children: Find inorder successor of the node. Copy contents of the inorder successor 
to the node and delete the inorder successor. Note that inorder predecessor can also be used. 
In this particular case, inorder successor can be obtained by finding the minimum value in the right child of the node.
"""
import random 
from collections import defaultdict

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None
        self.size = 1
    @property
    def left_size(self):
        if self.left:
            return self.left.size
        return 0
    @property
    def right_size(self):
        if self.right: 
            return self.right.size
        return 0

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value=value)
        if not self.root:
            self.root = node
            return
        n = self.root
        while n != None:
            # increment the current (some parent) node's size by one since we are adding a child below it
            n.size += 1
            if value <= n.value:
                if n.left == None:
                    # insert the node as the left child
                    n.left = node
                    node.parent = n
                    return
                n = n.left
            else:
                if n.right == None:
                    # insert the node as the right child
                    n.right = node
                    node.parent = n
                    return
                n = n.right

    def find(self, value):
        if not self.root:
            return None
        curr = self.root
        while curr:
            if curr.value == value:
                return curr
            elif value <= curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return None

    # find minimum node in tree given node
    def min_val_node_iter(self, prev, node):
        prev = prev
        while node.left:
            prev = node
            node = node.left
        if prev.left == node:
            prev.left = None
        elif prev.right == node:
            prev.right = None
        return node

    # returns deleted value (not necessary)
    def delete_iter(self, value):
        if not self.root:
            return None
        curr = self.root
        prev = None
        while curr:
            if value < curr.value:
                prev = curr
                curr = curr.left
            elif value > curr.value:
                prev = curr
                curr = curr.right
            else:
                # found the value in the tree, now need to delete it
                if not curr.left and not curr.right:
                    # leaf node, remove. check to make sure it's not the root
                    if prev and prev.left == curr:
                        prev.left = None
                    elif prev and prev.right == curr:
                        prev.right = None
                    else:
                        # only node in tree, set root to None and return curr
                        self.root = None
                    return curr
                # if one child, copy child to node and remove child
                elif curr.left and not curr.right:
                    curr.value = curr.left.value
                    temp = curr.left
                    curr.left = None
                    return temp
                elif curr.right and not curr.left:
                    curr.value = curr.right.value
                    temp = curr.right
                    curr.right = None
                    return temp
                # both children. find successor (leftmost value in right subtree) and copy to curr node and delete successor node
                else:
                    successor = self.min_val_node_iter(curr, curr.right)
                    curr.value = successor.value
                    return successor
        return None

    def delete(self, value):
        if not self.root:
            return None
        # check if value exists in tree before deleting, if it doesn't then don't call delete
        if not self.find(value):
            return None
        return self.delete_helper(self.root, value)
        
    
    def min_val_node(self, node):
        while node.left:
            node = node.left
        return node
    
    # recursive solution to delete
    def delete_helper(self, node, value):
        # base case
        if not node:
            return None
        if value < node.value:
            node.left = self.delete_helper(node.left, value)
        elif value > node.value:
            node.right = self.delete_helper(node.right, value)
        else:
            # found the node, now need to delete it
            # if node has one or less children, either delete the leaf directly or copy the child to the node and delete the child
            if node.left == None:
                temp = node.right
                node = None
                return temp
            elif node.right == None:
                temp = node.left
                node = None
                return temp
            else:
                # if node has two children, find leftmost node in right subtree (successor) and copy to node. delete the successor node
                min_node = self.min_val_node(node.right)
                # copy the min node value to the node we are deleting
                node.value = min_node.value
                # delete the min node from the tree
                node.right = self.delete_helper(node.right, node.value)
        # decrement size of current node
        node.size -= 1
        return node

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self.printTree(node.left, level + 1)

    def get_random_node(self):
        node = self.root
        while node:
            # with prob 1/N = 1/(1+l+r), choose curr node
            # with prob l/(1+l+r), go down left
            # with prob r/(1+l+r), go down right
            choices = ["self", "left", "right"]
            choice_weights = [1, node.left_size, node.right_size]
            decision = random.choices(choices, weights=choice_weights, k=1)[0]

            if decision == "self":
                return node
            elif decision == "left":
                node = node.left
            elif decision == "right":
                node = node.right
        return node
        



    

def example():
    # bst = BinarySearchTree()
    # bst.insert(20)
    # bst.insert(9)
    # bst.insert(25)
    # bst.insert(5)
    # bst.insert(12)
    # bst.insert(11)
    # bst.insert(14)
    # bst.printTree(bst.root)
    # print(bst.delete(9).value)
    # print('-----')
    # bst.printTree(bst.root)
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)
    print(bst.root.size)
    bst.delete(12)
    print(bst.root.size)

    chosen_counts = defaultdict(int)
    for _ in range(6000):
        node = bst.get_random_node()
        chosen_counts[node.value] += 1
    print(chosen_counts.keys())
    print(chosen_counts.values())

if __name__ == "__main__":
    example()