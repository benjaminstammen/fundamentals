import unittest
from typing import List

class Solution(object):
    def get_num_boxes_n_squared(self, boxes: List[int]):
        empty_boxes = []
        # sort using largest first so that
        # we're not putting a tiny box into a
        # giant box.
        sorted_boxes = reversed(sorted(boxes))
        for box in sorted_boxes:
            for index, empty_box in enumerate(empty_boxes):
                if box <= (empty_box / 2):
                    # The math on this is funky, but the number of empty
                    # boxes at the end is equal to the number of boxes in
                    # total.
                    #
                    # For instance, a '10' box with a '5' box inside it is
                    # represented by the empty '5' box.
                    print(f'{box} fits in {empty_box}...')
                    empty_boxes.pop(index)
                    break
            empty_boxes.append(box)
        return len(empty_boxes)

    def get_num_boxes_n_log_n(self, boxes: List[int]):
        boxes.sort() # sorting takes n * log(n), remainder takes n
        num_boxes = len(boxes)
        l, r = 0, 1
        while r < len(boxes):
            if boxes[l] <= boxes[r] / 2:
                num_boxes -= 1
                l += 1
                r += 1
            else:
                r += 1
        return num_boxes
        



class TestSolution(unittest.TestCase):

    def test_1(self):
        boxes = [5, 2, 9, 7, 8, 6, 2, 4]
        self.assertEqual(
            Solution().get_num_boxes_n_squared(boxes),
            Solution().get_num_boxes_n_log_n(boxes),
            5
        )

    def test_2(self):
        boxes = [2, 2, 2, 2, 2]
        self.assertEqual(
            Solution().get_num_boxes_n_squared(boxes),
            Solution().get_num_boxes_n_log_n(boxes),
            5
        )

    def test_3(self):
        boxes = [25, 50, 100]
        self.assertEqual(
            Solution().get_num_boxes_n_squared(boxes),
            Solution().get_num_boxes_n_log_n(boxes),
            1
        )
    
    def test_4(self):
        boxes = [1, 1, 6, 3]
        self.assertEqual(
            Solution().get_num_boxes_n_squared(boxes),
            Solution().get_num_boxes_n_log_n(boxes),
            2
        )
    
if __name__ == "__main__":
    unittest.main()