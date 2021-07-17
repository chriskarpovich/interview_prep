class Node():
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None

    # def disp(self, nesting=0):
    #     indent = " " * nesting * 2
    #     output = f"{self.value}\n"
    #     if self.left is not None:
    #         output += f"{indent}L:"
    #         output += self.left.disp(nesting + 1)
    #     if self.right is not None:
    #         output += f"{indent}R:"
    #         output += self.right.disp(nesting + 1)
    #     return output

    def __str__(self):
        return self.value
class Tree():
    def __init__(self, root=None):
        self.root = root

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert_recursive(self, value):
        def helper(node, query):
            if query <= node.value:
                if node.left:
                    helper(node.left, query)
                else:
                    node.left = Node(value=query)
                    node.left.parent = node.left
                return
            else:
                if node.right:
                    helper(node.right, query)
                else:
                    node.right = Node(value=query)
                    node.right.parent = node.right
                return
        if not self.root:
            self.root = Node(value=value)
            return
        else:
            helper(self.root, value)
            return

    def insert(self, key):
        new = Node(value=key)
        if self.root is None:
            self.root = new
            return

        current = self.root
        while current:
            if current.value > key:
                if current.left is None:
                    current.left = new
                    new.parent = current
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new
                    new.parent = current
                    return
                current = current.right

    def get_node(self, query):
        if not self.root:
            return None
        curr = self.root
        while curr:
            if query == curr.value:
                return curr
            elif query < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return None



    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self.printTree(node.left, level + 1)

class BinaryTree:
    NodeCls = Node

    def __init__(self):
        self.root = None

    def insert(self, value, parent):
        new = self.NodeCls(value)
        if parent is None:
            if self.root is None:
                self.root = new
                return new
            raise Exception("a root already exists")

        if not parent.left:
            parent.left = new
            new.parent = parent
        elif not parent.right:
            parent.right = new
            new.parent = parent
        else:
            raise Exception("a node cannot have more than two children")
        return new
    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self.printTree(node.left, level + 1)
                

