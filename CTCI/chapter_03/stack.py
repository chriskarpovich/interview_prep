"""
Stack class
"""

class Stack:
    def __init__(self):
        self.stack = []
    # remove the top of the stack and return it
    def pop(self):
        return self.stack.pop()
    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)
    # return the top of the stack but don't remove it
    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None
    def __len__(self):
        return len(self.stack)
    def __bool__(self):
        # lets us use the stack as a conditional
        return bool(self.stack)
    def isEmpty(self):
        if self.stack:
            return False
        else:
            return True

