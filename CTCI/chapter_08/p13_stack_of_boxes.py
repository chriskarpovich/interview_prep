"""
You have a stack of n boxes, with widths w_i, heights h_i, and depths d_i. The boxes cannot be rotated and can only be stacked
on top of one another if each box in the stack is strictly larger than the box above it in width, height, and depth. Implement
a method to compute the height of the tallest possible stack. The height of a stack is the sum of the heights of each box.
"""
import unittest

class Box:
    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth



def tallest_stack_iter(boxes):
    max_height = 0
    # sorts boxes in descending order by height
    boxes = sorted(boxes, key = lambda x: x.height, reverse=True)
    for i in range(len(boxes)):
        # each box gets a turn at being the starting box
        prev_box = boxes[i]
        total_height = boxes[i].height
        # loop through all other boxes smaller in height and make sure they fit. if not, then skip it
        for box in boxes[i+1:]:
            if box.width < prev_box.width and box.depth < prev_box.depth:
                total_height += box.height
                prev_box = box
        max_height = max(max_height, total_height)
    return max_height

def tallest_stack(boxes):
    def helper(boxes, i, prev_i, memo, total_height):
        # base case, no more boxes
        if i == len(boxes):
            return total_height

        # check if box at i is less in width and depth than the previous box
        # check if cached the total height this box can support (including itself)
        if boxes[i].width < boxes[prev_i].width and boxes[i].depth < boxes[prev_i].depth:
            if memo[i] == -1:
                # store the total height the current box can support plus itself as memo
                memo[i] = helper(boxes, i+1, i, memo, total_height + boxes[i].height) - total_height
            return total_height + memo[i]
        else:
            return helper(boxes, i+1, prev_i, memo, total_height)

    memo = [-1 for _ in range(len(boxes))]
    # traverse boxes in descending order
    boxes = sorted(boxes, key = lambda x: x.height, reverse=True)
    max_height = 0
    for i in range(len(boxes)):
        max_height = max(max_height, helper(boxes, i+1, i, memo, total_height=boxes[i].height))
    return max_height


class TestSuite(unittest.TestCase):
    def test_null(self):
        assert tallest_stack([]) == 0


    def test_single_box(self):
        assert tallest_stack([Box(3, 2, 1)]) == 3


    def test_two_conflicting_boxes(self):
        assert tallest_stack([Box(3, 2, 1), Box(5, 4, 1)]) == 5


    def test_two_stackable_boxes(self):
        assert tallest_stack([Box(3, 2, 1), Box(6, 5, 4)]) == 9

    def test_three(self):
        boxes = [Box(1, 7, 4), Box(2, 6, 9), Box(4, 9, 6), Box(10, 12, 8), Box(6, 2, 5), 
        Box(3, 8, 5), Box(5, 7, 7), Box(2, 10, 16), Box(12, 15, 9)]
        print(tallest_stack(boxes))
        assert tallest_stack(boxes) == 28


if __name__ == "__main__":
    unittest.main()