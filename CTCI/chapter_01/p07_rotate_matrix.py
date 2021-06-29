# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.
# Can you do this in place?
import math
from copy import deepcopy

def print_matrix(mat):
    for x in mat:
        print(x)
    print('---')

def rotate_matrix(mat):
    # rotate like a ring
    # top = 0
    # bottom = len(mat) - 1
    # left = 0
    # right = len(mat[0]) - 1

    new_mat = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
    # iterate through top, bottom, left, right
    for top, bottom, left, right in zip(range(math.ceil(len(mat) / 2)), reversed(range(math.floor(len(mat) / 2), len(mat))), range(math.ceil(len(mat[0]) / 2)), reversed(range(math.floor(len(mat[0]) / 2), len(mat[0])))):
        # rows
        print(top, bottom, left, right)
        for i, j in zip(range(top, bottom + 1), reversed(range(left, right + 1))):
            # set top row of new matrix to be left column of old matrix
            new_mat[top][j] = mat[i][left]
        for i, j in zip(range(top, bottom + 1), range(left, right + 1)):
            # set right column of new matrix to be top row of old matrix
            new_mat[i][right] = mat[top][j]
        for i, j in zip(reversed(range(top, bottom + 1)), range(left, right + 1)):
            # set bottom row of new matrix to be right column of old matrix
            new_mat[bottom][j] = mat[i][right]
        for i, j in zip(reversed(range(top, bottom + 1)), reversed(range(left, right + 1))):
            # set left column of new matrix to be bottom row of old matrix
            new_mat[i][left] = mat[bottom][j]
        print_matrix(new_mat)
    return(new_mat)

def rotate_matrix_pythonic(matrix):
    """rotates a matrix 90 degrees clockwise"""
    n = len(matrix)
    result = [[0] * n for i in range(n)]  # empty list of 0s
    for i, j in zip(range(n), range(n - 1, -1, -1)):  # i counts up, j counts down
        for k in range(n):
            result[k][i] = matrix[j][k]
        print(i, j)
        print_matrix(result)
    return result


def main():
    test_cases = [
        ([[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]], 

        [[7, 4, 1], 
        [8, 5, 2], 
        [9, 6, 3]]),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]
    for [test_matrix, expected] in test_cases:
        test_matrix = deepcopy(test_matrix)
        assert rotate_matrix_pythonic(test_matrix) == expected

if __name__ == "__main__":
    main()