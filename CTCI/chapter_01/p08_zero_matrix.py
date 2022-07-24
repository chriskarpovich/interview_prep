# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to zero
from copy import deepcopy
from re import L

from p07_rotate_matrix import print_matrix

def zero_matrix_bad(mat):
    # O(M+N) space solution
    rows = len(mat)
    cols = len(mat[0])
    r = [0 for _ in range(rows)]
    c = [0 for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                r[i] = 1
                c[j] = 1
    for i in range(rows):
        for j in range(cols):
            if r[i] == 1 or c[j] == 1:
                mat[i][j] = 0
    return mat


def zero_matrix_opt(mat):
    # O(1) space, two-pass solution
    # store states in first element of row/col and check those to see if they should be zeroed
    # need to keep track if first row and/or first col need to be zeroed out as well, because
    # putting a zero in the first row/col will make it look like that row/col needs to be zeroed
    # but it may not need to be.
    rows = len(mat)
    cols = len(mat[0])
    firstRow = False
    firstCol = False

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                if i == 0:
                    firstRow = True
                if j == 0:
                    firstCol = True
                mat[0][j] = 0
                mat[i][0] = 0
    for i in range(1, rows):
        for j in range(1, cols):
            # don't iterate through first row or col
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0
    if firstRow:
        for j in range(cols):
            mat[0][j] = 0
    if firstCol:
        for i in range(rows):
            mat[i][0] = 0

    return mat
    


def main():
    test_cases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]

    for [test_matrix, expected] in test_cases:
        test_1 = deepcopy(test_matrix)
        assert zero_matrix_bad(test_1) == expected
        test_2 = deepcopy(test_matrix)
        assert zero_matrix_opt(test_2) == expected

if __name__ == "__main__":
    main()