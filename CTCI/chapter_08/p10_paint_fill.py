"""
Implement the "paint fill" function that one might see on many image editing programs. That is, given a screen (represented
by a two-dimensional array of colors), a point, and a new color, fill in the surrounding area until the color changes from the
original color.
"""
import unittest

# visited is not necessary here because we aren't looking through a maze. if a color is not the correct one we will know
# just from checking screen
def paint_fill(screen, r, c, new_color):
    rows = len(screen)
    cols = len(screen[0])
    visited = [[0 for i in range(rows)] for j in range(cols)]
    orig_color = screen[r][c]
    def helper(screen, r, c, rows, cols, orig_color, new_color, visited):
        # base case, if out of bounds of screen, return
        if r >= rows or c >= cols or r < 0 or c < 0:
            return
        # base case, if visited return
        if visited[r][c] == 1:
            return
        # base case, check color of cell and if not correct color return
        if screen[r][c] != orig_color:
            return
        # change to visited
        # change color if orig color and then recurse to R, L, U, D
        visited[r][c] = 1
        screen[r][c] = new_color
        helper(screen, r+1, c, rows, cols, orig_color, new_color, visited)
        helper(screen, r-1, c, rows, cols, orig_color, new_color, visited)
        helper(screen, r, c+1, rows, cols, orig_color, new_color, visited)
        helper(screen, r, c-1, rows, cols, orig_color, new_color, visited)
    helper(screen, r, c, rows, cols, orig_color, new_color, visited)
    return screen



class Test(unittest.TestCase):
    test_cases = [
        (
            [[1, 2, 5], [2, 2, 4], [2, 8, 6]],
            1,
            1,
            3,
            [[1, 3, 5], [3, 3, 4], [3, 8, 6]],
        )
    ]
    testable_functions = [paint_fill]

    def test_paint_fill(self):
        for f in self.testable_functions:
            for [screen, r, c, new_color, expected] in self.test_cases:
                result = f(screen, r, c, new_color)
                print(result)
                assert result == expected


if __name__ == "__main__":
    unittest.main()