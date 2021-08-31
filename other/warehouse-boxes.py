import unittest
from typing import List

class Solution(object):
    def get_num_boxes(self, boxes: List[int]):
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


class TestSolution(unittest.TestCase):

    def test_1(self):
        self.assertEqual(
            Solution().get_num_boxes(
                boxes=[5, 2, 9, 7, 8, 6, 2, 4],
            ),
            5
        )

    def test_2(self):
        self.assertEqual(
            Solution().get_num_boxes(
                boxes=[2, 2, 2, 2, 2],
            ),
            5
        )

    def test_3(self):
        self.assertEqual(
            Solution().get_num_boxes(
                boxes=[25, 50, 100],
            ),
            1
        )
    
    def test_4(self):
        self.assertEqual(
            Solution().get_num_boxes(
                boxes=[1, 1, 6, 3],
            ),
            2
        )
    
if __name__ == "__main__":
    unittest.main()