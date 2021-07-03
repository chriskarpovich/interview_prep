"""
1. Describe how you would use a single array to implement three stacks.
Allocate a fixed amount of memory for each stack on the array. Array is length n.
Stack 1: [0, n/3). Stack 2: [n/3, 2n/3). Stack 3: [2n/3, n)
"""
import pytest

class MultiStack:
    def __init__(self, stack_size, number_of_stacks):
        self.stack_size = stack_size
        self.number_of_stacks = number_of_stacks
        self.stack = [0] * (stack_size * number_of_stacks)
        # Top of stack is end of each array. Starts at 0, n/num_stacks, 2n/num_stacks, ... (num_stacks - 1)/num_stacks.
        # Stack top points to nearest empty slot 
        self.sizes = [0] * self.number_of_stacks

    # remove top item from stack and return it
    def pop(self, stack_no):
        if not self.check_valid_stack_no(stack_no):
            raise StackDoesNotExistError(f"Pop failed. Stack #{stack_no} does not exist.")
        if self.is_empty(stack_no):
            raise StackEmptyError(f"Pop failed. Stack #{stack_no} is empty.")
        top_ind_filled = self.get_top_ind(stack_no)
        top_item = self.stack[top_ind_filled]
        # decrement stack size after removing
        self.sizes[stack_no] -= 1
        return top_item

    # Add item to top of the stack
    def push(self, item, stack_no):
        if not self.check_valid_stack_no(stack_no):
            raise StackDoesNotExistError(f"Push failed. Stack #{stack_no} does not exist.")
        elif self.is_full(stack_no):
            raise StackFullError(f"Push failed. Stack #{stack_no} is full.")
        # increment size of stack first to add to empty slot
        self.sizes[stack_no] += 1
        top_ind = self.get_top_ind(stack_no)
        self.stack[top_ind] = item
        

    # Return the top of the stack but don't remove it
    def peek(self, stack_no):
        if not self.check_valid_stack_no(stack_no):
            raise StackDoesNotExistError(f"Peek failed. Stack #{stack_no} does not exist.")
        elif self.is_empty(stack_no):
            raise StackEmptyError(f"Peek failed. Stack #{stack_no} is empty.")
        top_ind_filled = self.get_top_ind(stack_no)
        return self.stack[top_ind_filled]

    def is_empty(self, stack_no):
        if self.sizes[stack_no] == 0:
            return True
        else:
            return False
    def is_full(self, stack_no):
        # empty slot is at limit of stack size
        if self.sizes[stack_no] == self.stack_size:
            return True
        else:
            return False
    def get_top_ind(self, stack_no):
        # Stack top points to nearest filled slot
        return (self.stack_size * stack_no) + (self.sizes[stack_no] - 1)
    def check_valid_stack_no(self, stack_no):
        if stack_no < self.number_of_stacks:
            return True
        else:
            return False

class MultiStackError(Exception):
    """multistack operation error"""


class StackFullError(MultiStackError):
    """the stack is full"""


class StackEmptyError(MultiStackError):
    """the stack is empty"""


class StackDoesNotExistError(ValueError):
    """stack does not exist"""

        

def test_multistack():
    num_stacks = 3
    stack_size = 6
    s = MultiStack(stack_size=stack_size, number_of_stacks=num_stacks)

    for stack_no in range(num_stacks):
        assert s.is_empty(stack_no)
        assert not s.is_full(stack_no)
        with pytest.raises(StackEmptyError):
            s.pop(stack_no)

        for i in range(stack_size - 1):
            s.push(i, stack_no=stack_no)
            assert s.peek(stack_no) == i
            assert not s.is_empty(stack_no)
            assert not s.is_full(stack_no)

        s.push(999, stack_no=stack_no)
        with pytest.raises(StackFullError):
            s.push(777, stack_no=stack_no)

        assert not s.is_empty(stack_no)
        assert s.is_full(stack_no)

        assert s.peek(stack_no) == 999
        assert s.pop(stack_no) == 999
        assert not s.is_empty(stack_no)
        assert not s.is_full(stack_no)

        for i in range(stack_size - 2, 0, -1):
            assert s.peek(stack_no) == i
            assert s.pop(stack_no) == i
            assert not s.is_empty(stack_no)
            assert not s.is_full(stack_no)

        assert s.peek(stack_no) == 0
        assert s.pop(stack_no) == 0
        assert s.is_empty(stack_no)
        assert not s.is_full(stack_no)

        with pytest.raises(StackEmptyError):
            s.peek(stack_no)
        with pytest.raises(StackEmptyError):
            s.pop(stack_no)


def test_stack_does_not_exist():
    s = MultiStack(stack_size=3, number_of_stacks=1)
    with pytest.raises(StackDoesNotExistError):
        s.push(1, 1)


if __name__ == "__main__":
    # newstack = MultiStack(stack_size=2, number_of_stacks=2)
    # print(newstack.is_empty(1))
    # newstack.push(3, 1)
    # print(newstack.peek(1))
    # print(newstack.is_empty(1))
    # newstack.push(2, 1)
    # print(newstack.peek(1))
    # print(newstack.pop(1))
    # print(newstack.peek(1))
    # newstack.push(3, 1)

    test_multistack()