class Node():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def disp(self, nesting=0):
        indent = " " * nesting * 2
        output = f"{self.value}\n"
        if self.left is not None:
            output += f"{indent}L:"
            output += self.left.disp(nesting + 1)
        if self.right is not None:
            output += f"{indent}R:"
            output += self.right.disp(nesting + 1)
        return output

    def __str__(self):
        return self.disp()
class Tree():
    def __init__(self, root=None):
        self.root = root