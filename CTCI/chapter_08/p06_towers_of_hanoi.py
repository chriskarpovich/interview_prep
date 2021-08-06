"""
In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide onto any tower. The puzzle starts with
disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following constraints:
1. Only one disk can be moved at a time
2. A disk is slid off the top of one tower onto another tower.
3. A disk cannot be placed on top of a smaller disk.

Write a program to move the disks from the first tower to the last using stacks.
"""
"""
Iterative solution:
For an even number of disks:

make the legal move between pegs A and B (in either direction),
make the legal move between pegs A and C (in either direction),
make the legal move between pegs B and C (in either direction),
repeat until complete.

For an odd number of disks:

make the legal move between pegs A and C (in either direction),
make the legal move between pegs A and B (in either direction),
make the legal move between pegs B and C (in either direction),
repeat until complete.
"""
def towers(n):
    A, B, C = [], [], []
    for i in range(n)[::-1]:
        A.append(i)
    while(len(C) != n):
        if n % 2 == 0:
            if not B or (A and B and A[-1] < B[-1]):
                B.append(A.pop())
            elif not A or (A and B and A[-1] > B[-1]):
                A.append(B.pop())
            
            if len(C) == n:
                break

                
            if not C or (A and C and A[-1] < C[-1]):
                C.append(A.pop())
            elif not A or (A and C and A[-1] > C[-1]):
                A.append(C.pop())

            if len(C) == n:
                break

        else:
            if not C or (A and C and A[-1] < C[-1]):
                C.append(A.pop())
            elif not A or (A and C and A[-1] > C[-1]):
                A.append(C.pop())

            if len(C) == n:
                break


            if not B or (A and B and A[-1] < B[-1]):
                B.append(A.pop())
            elif not A or (A and B and A[-1] > B[-1]):
                A.append(B.pop())

            if len(C) == n:
                break

        
        if not B or (B and C and C[-1] < B[-1]):
            B.append(C.pop())
        elif not C or (B and C and C[-1] > B[-1]):
            C.append(B.pop())

    return (A, B, C)

"""
1. Move m − 1 disks from the source to the spare peg, by the same general solving procedure. Rules are not violated, by assumption. 
This leaves the disk m as a top disk on the source peg.
2. Move the disk m from the source to the target peg, which is guaranteed to be a valid move, by the assumptions — a simple step.
3. Move the m − 1 disks that we have just placed on the spare, from the spare to the target peg by the same general solving procedure, so 
they are placed on top of the disk m without violating the rules.
The base case is to move 0 disks (in steps 1 and 3), that is, do nothing – which obviously doesn't violate the rules.
"""

def towers_recursive(n):
    A, B, C = [], [], []
    for i in range(n)[::-1]:
        A.append(i)
    def helper(m, n, A, B, C):
        if m == 0:
            return
        helper(m-1, n+1, A, B, C)
        ind = n - m
        if n % 2 == 0:
            if not B or (A and B and A[ind] < B[ind]):
                B.append(A.pop())
            elif not A or (A and B and A[ind] > B[ind]):
                A.append(B.pop())
            
            if len(C) == n:
                return

                
            if not C or (A and C and A[ind] < C[ind]):
                C.append(A.pop())
            elif not A or (A and C and A[ind] > C[ind]):
                A.append(C.pop())

            if len(C) == n:
                return

        else:
            if not C or (A and C and A[ind] < C[ind]):
                C.append(A.pop())
            elif not A or (A and C and A[ind] > C[ind]):
                A.append(C.pop())

            if len(C) == n:
                return


            if not B or (A and B and A[-1] < B[-1]):
                B.append(A.pop())
            elif not A or (A and B and A[-1] > B[-1]):
                A.append(B.pop())

            if len(C) == n:
                return

        
        if not B or (B and C and C[-1] < B[-1]):
            B.append(C.pop())
        elif not C or (B and C and C[-1] > B[-1]):
            C.append(B.pop())


        

def example():
    n = 5
    A, B, C = towers_recursive(n)
    print(A)
    print(B)
    print(C)


if __name__ == "__main__":
    example()