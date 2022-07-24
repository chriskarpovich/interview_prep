# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.
# Can you do this in place?
from copy import deepcopy

def print_matrix(mat):
    for x in mat:
        print(x)
    print('---')

def rotate_matrix_transpose(mat):
    rows = len(mat)
    cols = len(mat[0])

    # transpose matrix
    for i in range(rows):
        for j in range(i, cols):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    # reverse rows
    for i in range(rows):
        mat[i].reverse()
    return mat

def rotate_matrix_swap(mat):
    rows = len(mat)
    cols = len(mat[0])

    # transpose matrix
    for i in range(rows):
        for j in range(i, cols):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    # swap cols
    for i in range(rows):
        for j in range(cols // 2):
            mat[i][j], mat[i][cols-j-1] = mat[i][cols-j-1], mat[i][j]
    return mat

def rotate_matrix_iter(mat):
    rows = len(mat)
    cols = len(mat[0])

    l, r = 0, cols-1
    top, bottom = 0, rows-1

    while l < r:
        for i in range(r-l):
            top, bottom = l, r
            top_left = mat[top][l + i]
            mat[top][l + i] = mat[bottom - i][l]
            mat[bottom - i][l] = mat[bottom][r - i]
            mat[bottom][r - i] = mat[top + i][r]
            mat[top + i][r] = top_left
        # top += 1
        # bottom -= 1
        l += 1
        r -= 1
    return mat
    




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
        test_1 = deepcopy(test_matrix)
        assert rotate_matrix_transpose(test_1) == expected
        test_2 = deepcopy(test_matrix)
        assert rotate_matrix_swap(test_2) == expected
        test_3 = deepcopy(test_matrix)
        assert rotate_matrix_iter(test_3) == expected

if __name__ == "__main__":
    main()