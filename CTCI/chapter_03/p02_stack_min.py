"""
Design a stack such taht in addition to push and pop, it has a function min which returns the minimum element? Push, pop, and min
should all operate in O(1) time.
# min/max in python are O(n) so can't use them.
"""
from stack import Stack

class MinStack(Stack):
    def __init__(self):
        # create mini stack whose top is always the minimum value in the larger stack.
        # when we remove the top we always keep the next min at the top that way
        super().__init__()
        self.minvals = Stack()
    def push(self, item):
        # call super push to push to main stack
        super().push(item)
        # if less than or equal to minimum, add it to the min stack
        if not self.minvals or item <= self.minvals.peek():
            self.minvals.push(item)
    def pop(self):
        value = super().pop()
        # only remove from minvals stack if it is the top of the min stack
        if value == self.minvals.peek():
            self.minvals.pop()
        return value
    def minimum(self):
        return self.minvals.peek()


def test_min_stack():
    newstack = MinStack()
    assert newstack.minimum() is None

    newstack.push(5)
    assert newstack.minimum() == 5

    newstack.push(6)
    assert newstack.minimum() == 5

    newstack.push(3)
    assert newstack.minimum() == 3

    newstack.push(7)
    assert newstack.minimum() == 3

    newstack.push(3)
    assert newstack.minimum() == 3

    newstack.pop()
    assert newstack.minimum() == 3

    newstack.pop()
    assert newstack.minimum() == 3

    newstack.pop()
    assert newstack.minimum() == 5

    newstack.push(1)
    assert newstack.minimum() == 1


if __name__ == "__main__":
    test_min_stack()


        
