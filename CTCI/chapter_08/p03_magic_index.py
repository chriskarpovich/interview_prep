"""
A magic index in an array A[0, ... n-1] is defined to be an index such that A[i] = i. Given a sorted array of distinct integers, write a method to
find a magic index, if one exists, in array A.
Ex: [-2, 0, "2", "3",]
FOLLOW UP: What if the values are not distinct?
"""
NOT_FOUND = -1

def magic_index_unoptimized(array):
    for i in range(len(array)):
        if array[i] == i:
            return i
    return -1

def magic_index(array):
    # if A[i] > i we know for i and any j>i that it's impossible to have a magic index there (for distinct values).
    # if A[i] < i we know for i and any j<i that it's impossible to have a magic index there (for distinct values)
    # binary search the sorted array to determine which half may have a magic index
    L = 0
    R = len(array) - 1
    def helper(L, R, arr):
        # base case
        if R < L:
            return -1
        mid = (L + R) // 2
        # check if magic value
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            # discard left half and search right half of array
            L = mid + 1
            return helper(L, R, arr)
        elif arr[mid] > mid:
            # discard right half and search left half of array
            R = mid - 1
            return helper(L, R, arr)
    return helper(L, R, array)

def magic_index_non_distinct(array):
    L = 0
    R = len(array) - 1
    def helper(L, R, arr):
        # base case
        if R < L:
            return -1
        mid = (L + R) // 2
        # check if magic value
        if arr[mid] == mid:
            return mid
        # recursively search left half of array. only have to search between indices start and min(mid-1, arr[mid]) since if arr[mid] < mid-1
        # we know anything between indices arr[mid] and mid-1 cannot be the magic number
        right_ind = min(mid-1, arr[mid])
        found_ind = helper(L, right_ind, arr)
        if found_ind >= 0:
            return found_ind
        # recursively search right half of array. only have to search through max(mid+1, arr[mid]) for same reason as above
        left_ind = max(mid+1, arr[mid])
        return helper(left_ind, R, arr)
    return helper(L, R, array)


test_cases = [
    ([-14, -12, 0, 1, 2, 5, 9, 10, 23, 25], 5),
    ([-14, -12, 0, 1, 2, 7, 9, 10, 23, 25], NOT_FOUND),
    ([0, 1, 2, 3, 4], 2),
    ([], NOT_FOUND),
]

followup_test_cases = test_cases + [
    ([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13], 2),
]


def test_magic_index():
    for array, expected in test_cases:
        result = magic_index(array)
        assert result == expected


def test_magic_index_non_distinct():
    for array, expected in followup_test_cases:
        assert magic_index_non_distinct(array) == expected


if __name__ == "__main__":
    test_magic_index()
    test_magic_index_non_distinct()
