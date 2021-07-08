"""
For a stack of plates, if it gets too high, it might topple. In real life, we want to start a new stack when the
previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. It should be composed of
several stacks and should create a new stack once the previous once exceeds capacity. push and pop should behave identically to
a single stack.

Follow up: Implement a function popAt(int index) which performs a pop operation on a specific substack.
"""
from stack import Stack
import unittest

class SetOfStacks(Stack):
    def __init__(self, threshold):
        super().__init__()
        self.threshold = threshold
    
    def push(self, item):
        # check if stack of stacks is empty and add one if necessary
        if not self.stack:
            self.stack.append(Stack())
        # check if stack is full and create another if necessary
        if len(self.stack[-1]) == self.threshold:
            self.stack.append(Stack())
        # push item to stack
        self.stack[-1].push(item)

    def pop(self):
        # check if stack of stacks is empty and return None
        if not self.stack:
            return None
        # check if removing item from stack with 0 elements and decrement stack number
        elif len(self.stack[-1]) == 0:
            self.stack.pop()
        return self.stack[-1].pop()


class Tests(unittest.TestCase):
    def test_stacks(self):
        stacks = SetOfStacks(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(35):
            lst.append(stacks.pop())
        assert lst == list(reversed(range(35)))

    # def test_pop_at(self):
    #     stacks = SetOfStacks(5)
    #     for i in range(35):
    #         stacks.push(i)
    #     lst = []
    #     for _ in range(31):
    #         lst.append(stacks.pop_at(0))
    #     assert lst == list(range(4, 35))


if __name__ == "__main__":
    unittest.main()
