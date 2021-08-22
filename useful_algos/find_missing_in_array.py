arr = [3, 4, 0, 2]

def bin_search(arr, L, R):
    # find first number where arr[i] != i
    while L <= R:
        mid = (L + R) // 2
        if arr[mid] == mid:
            # sorted up to this point correctly, go right
            L = mid + 1
        else:
            # go left
            R = mid - 1
    # whenever we go right, we update the left index
    # the left index will point to the slot where
    # arr[i] != i
    return L
        
arr.sort()
print(bin_search(arr, 0, len(arr) - 1))