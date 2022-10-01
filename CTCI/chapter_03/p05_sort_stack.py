"""
Write a program to sort a stack such that the smallest items are on top. You can use an additional temporary stack, but you
may not copy items into any other data structure such as an array. The stack supports the following operations: push, pop,
peek, and isEmpty.

4, 2, 5, 1, 3 --> 1, 2, 3, 4, 5
"""
def sort_stack(stack):
    temp = []
    while stack:
        val = stack.pop()
        while temp and val < temp[-1]:
            stack.append(temp.pop())
        temp.append(val)

    return temp
    


if __name__ == "__main__":
    stack = []
    stack.append(4)
    stack.append(2)
    stack.append(5)
    stack.append(1)
    stack.append(3)
    stack.append(3)
    stack.append(1)
    stack.append(1)
    stack = sort_stack(stack)
    print(stack)

