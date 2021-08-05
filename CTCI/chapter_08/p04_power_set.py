"""
Write a method to return all subsets of a set.
"""
from copy import deepcopy

def get_subsets_iterative(input_set):
    subsets = []
    subsets.append(set())
    for i in input_set:
        curr_sets = []
        for j in subsets:
            new_set = deepcopy(j)
            new_set.add(i)
            curr_sets.append(new_set)
        subsets.extend(curr_sets)
    return subsets
            

def get_subsets(input_set):
    # add each number to previous set and then append it recursively
    # base case, check if set is empty
    if not input_set:
        return [[]]
    prev_subsets = get_subsets(input_set[:-1])
    new_subsets = []
    for prev in prev_subsets:
        new_set = deepcopy(prev)
        new_set.append(input_set[-1])
        new_subsets.append(new_set)
    prev_subsets.extend(new_subsets)
    return prev_subsets
        





# testable_functions = [get_subsets_a, get_subsets_b, get_subsets_c]
testable_functions = [get_subsets_iterative, get_subsets]

test_cases = [({1, 2, 3}, {(), (1,), (1, 2), (1, 2, 3), (1, 3), (2,), (2, 3), (3,)})]


def test_get_subsets():
    for input_set, expected in test_cases:
        for get_subsets in testable_functions:
            results = get_subsets(list(input_set))
            results = {tuple(s) for s in results}
            print(results)
            assert results == expected


if __name__ == "__main__":
    # print(get_subsets_a([1, 2, 3]))
    # print("")
    # print(get_subsets_b([1, 2, 3]))
    # print("")
    # print(get_subsets_c([1, 2, 3]))
    #print(get_subsets_iterative([1, 2, 3]))
    test_get_subsets()
