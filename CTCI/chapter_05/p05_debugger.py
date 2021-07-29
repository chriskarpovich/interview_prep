"""
Explain what the following code does: ((n & (n-1)) == 0)

Say n = 1001100
n - 1 is 
    1001100
-   0000001
____________
which is 1001011
101100 & 1001011 is 0001000 which is not equal to zero

The code checks if a number and one minus the number have no ones in common. Therefore it checks if n is a power of 
two or n is zero. If n is a power of 2 it will not have any common ones with one minus it.
"""