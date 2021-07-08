"""
Write a program to sort a stack such that the smallest items are on top. You can use an additional temporary stack, but you
may not copy items into any other data structure such as an array. The stack supports the following operations: push, pop,
peek, and isEmpty.

4, 2, 5, 1, 3 --> 1, 2, 3, 4, 5
"""
from stack import Stack

def sort_stack(stack):
    
    temp_stack = Stack()
    offset = 0
    # loop through all values as min in stack
    while offset != len(stack):
        min = stack.stack[len(stack) - offset - 1]
        for i in range(len(stack)):
            if i >= offset:
                curr = stack.peek()
                if curr < min:
                    min = curr
            temp_stack.push(stack.pop())
        # Add everything back to stack and then push on the min value at the top. Make sure to account for duplicates.
        min_ct = 0
        while not temp_stack.isEmpty():
            # Skip item if it's equal to min since we'll push them onto the top at the end
            if temp_stack.peek() == min:
                min_ct += 1
                temp_stack.pop()
            else:
                stack.push(temp_stack.pop())
        # Push on the min values onto the top
        for i in range(min_ct):
            stack.push(min)
        # add to offset
        offset += min_ct

if __name__ == "__main__":
    stack = Stack()
    stack.push(4)
    stack.push(2)
    stack.push(5)
    stack.push(1)
    stack.push(3)
    stack.push(3)
    stack.push(1)
    stack.push(1)
    sort_stack(stack)
    print(stack.stack)

