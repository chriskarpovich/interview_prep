"""
Imagine a robot sitting on the upper left corner of a grid with r rows and c columns. The robot can only move in two directions, right and down, but
certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.
T   T   T
F   T   F
F   T   T

T   T   T
T  (F)  T
F   F   T

T   F   T
F   T   F
F   T   T
For each cell, we want to know if it is possible to get to the end goal. Some cells are called multiple times (e.g. we want to know if
when we reach that cell from multiple ways we can get to the goal) so we can cache it with DP.
"""

def get_path(grid):
    if not grid:
        return None
    r = len(grid)
    c = len(grid[0])
    path = []
    def helper(i, j, r, c, grid, path):
        # base case, check if we have reached bottom right corner
        if i == (r - 1) and j == (c - 1):
            path.append((i, j))
            return True
        # base case, check if exceeded limits
        if i > (r - 1) or j > (c - 1):
            return False
        # base case, check if cell is off-limits
        if not grid[i][j]:
            return False
        if helper(i+1, j, r, c, grid, path) or helper(i, j+1, r, c, grid, path):
            path.append((i, j))
            return True
        else:
            return False

    helper(0, 0, r, c, grid, path)
    return path[::-1]

def get_path_memo(grid):
    if not grid:
        return None
    r = len(grid)
    c = len(grid[0])
    path = []
    # memo = [[None] * c] * r DON'T INITIALIZE LIKE THIS, IT'S A TRAP!
    memo = [[-1] * c for i in range(r)]

    def helper(i, j, r, c, grid, path, memo):
        # base case, check if we have reached bottom right corner
        if i == (r - 1) and j == (c - 1):
            path.append((i, j))
            memo[i][j] = True
            return True
        # base case, check if exceeded limits
        if i > (r - 1) or j > (c - 1):
            return False
        # base case, check if cell is off-limits
        if not grid[i][j]:
            memo[i][j] = False
            return False
        if memo[i][j] == -1:
            memo[i][j] = helper(i+1, j, r, c, grid, path, memo) or helper(i, j+1, r, c, grid, path, memo)
        if memo[i][j]:
            path.append((i, j))
        return memo[i][j]
    helper(0, 0, r, c, grid, path, memo)
    print(memo)

    return path[::-1]

if __name__ == "__main__":
    # possible path
    print(get_path([[True, True, True], [False, True, False], [False, True, True]]))
    print(get_path_memo([[True, True, True], [False, True, False], [False, True, True]]))
    print('---')
    print(get_path([[True, True, True], [True, False, True], [False, False, True]]))
    print(get_path_memo([[True, True, True], [True, False, True], [False, False, True]]))
    print('---')
    # impossible path
    print(get_path([[True, False, True], [False, True, False], [False, True, True]]))
    print(get_path_memo([[True, False, True], [False, True, False], [False, True, True]]))