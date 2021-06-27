import math
test_list = [1, 5, 8, 9, 11, 13, 15, 21]

# O(logN) runtime
def binary_search(sorted_list, T):
    R = len(sorted_list) - 1
    L = 0
    while L <= R:
        m = math.floor((L+R)/2)
        if T < test_list[m]:
            R = m-1
        elif T > test_list[m]:
            L = m+1
        else:
            return m
    return -1
        
print(binary_search(test_list, 1))

def binary_search_recursive(sorted_list, L, R, T):
    m = math.floor((L + R)/2)
    # base case
    if R < L:
        return -1
    if T < sorted_list[m]:
        # found in left side
        return binary_search_recursive(sorted_list, L, R-1, T)
    elif T > sorted_list[m]:
        # found in right side
        return binary_search_recursive(sorted_list, L+1, R, T)
    else:
        # found element, return index
        return m

print(binary_search_recursive(test_list, 0, len(test_list)-1, 21))

