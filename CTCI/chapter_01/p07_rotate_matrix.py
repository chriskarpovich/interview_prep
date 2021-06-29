# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.
# Can you do this in place?

def rotate_matrix(mat):
    # rotate like a ring
    top = 0
    bottom = len(mat) - 1
    left = 0
    right = len(mat[0]) - 1

    new_mat = [0 * len(mat[0])] * len(mat)
    for i in range(bottom)

def main():
    matrix =[
            [1,  2,  3,  4 ],
            [5,  6,  7,  8 ],
            [9,  10, 11, 12 ],
            [13, 14, 15, 16 ] 
        ]

if __name__ == "__main__":
    main()