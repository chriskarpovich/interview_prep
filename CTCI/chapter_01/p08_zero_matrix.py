# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to zero
from copy import deepcopy

def zero_matrix(mat):
    rows = len(mat)
    cols = len(mat[0])

    rows_to_zero, cols_to_zero = [], []
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                rows_to_zero.append(i)
                cols_to_zero.append(j)
    rows_to_zero = list(set(rows_to_zero))
    cols_to_zero = list(set(cols_to_zero))

    # new_mat = [[0 for _ in range(cols)]] * rows

    # for i in range(rows):
    #     for j in range(cols):
    #         if i not in rows_to_zero and j not in cols_to_zero:
    #             new_mat[i][j] = mat[i][j]

    # without making a new matrix:
    for i in range(rows):
        for j in range(cols):
            if i in rows_to_zero or j in cols_to_zero:
                mat[i][j] = 0

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
        test_matrix = deepcopy(test_matrix)
        assert zero_matrix(test_matrix) == expected

    if __name__ == "__main__":
        main()