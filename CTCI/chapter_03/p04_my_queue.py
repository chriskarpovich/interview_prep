"""
Implement a MyQueue class which implements a queue using two stacks.
Queue: FIFO
Stack: LIFO
"""
import unittest
from stack import Stack

class MyQueue:
    def __init__(self):
        self.old_stack = Stack()
        self.new_stack = Stack()
    # add item to bottom of the queue
    def add(self, item):
        return self.new_stack.push(item)
    # remove an item from the top of the queue and return it
    def remove(self):
        # check if stack is empty
        if self.isEmpty():
            return None
        # shift stacks
        self.shift_stacks()
        # return top item of stack
        return self.old_stack.pop()

    # return the top of the queue but don't remove it
    def peek(self):
        if self.isEmpty():
            return None
        self.shift_stacks()
        return self.old_stack.peek()
    
    # return True iff the queue is empty
    def isEmpty(self):
        if len(self) == 0:
            return True
        else:
            return False
    def __len__(self):
        return len(self.old_stack) + len(self.new_stack)

    def shift_stacks(self):  
        # only shift when old_stack is empty to avoid mixing up the order from things put on new_stack 
        if self.old_stack.isEmpty():     
            while not self.new_stack.isEmpty():
                self.old_stack.push(self.new_stack.pop())
    


class Tests(unittest.TestCase):
    test_cases = [([1, 2, 3]), ([-1, 0, 1]), (["a", "b", "c", "d", "e", "f"])]

    def test_size(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for index, val in enumerate(sequence, start=1):
                q.add(val)
                assert len(q) == index
            for index, val in enumerate(sequence, start=1):
                q.remove()
                assert len(q) == len(sequence) - index

    def test_add(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
            assert q.peek() == sequence[0]
            assert len(q) == len(sequence)

    def test_shift_stacks(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
            assert len(q.old_stack) == 0
            assert len(q.new_stack) == len(sequence)
            assert q.new_stack.peek() == sequence[-1]
            q.shift_stacks()
            assert len(q.old_stack) == len(sequence)
            assert len(q.new_stack) == 0
            assert q.old_stack.peek() == sequence[0]

    def test_peek(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
                assert q.peek() == sequence[0]
            q.remove()
            assert q.peek() == sequence[1]

    def test_remove(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
            for i in range(len(sequence)):  # noqa
                assert q.remove() == sequence[i]

    def test_peek_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        assert q.peek() == 4

    def test_add_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        assert q.peek() == 4
        q.add(101)
        assert q.peek() != 101

    def test_remove_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        assert len(q) == 2
        assert q.remove() == 4
        assert q.remove() == 6
        assert len(q) == 0
        assert not q.remove()
if __name__ == "__main__":
    unittest.main()



