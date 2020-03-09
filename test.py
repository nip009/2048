import unittest
from twentyfortyeight import goDown, goUp, goLeft, goRight, sortZeroesToLeftAndMerge, sortZeroesToRightAndMerge

# Comment out line 95-102 in twentyfortyeight.py before running tests.

grid1 = [[0 for i in range(4)] for j in range(4)]
grid2 = [[0 for i in range(4)] for j in range(4)]
grid3 = [[0 for i in range(4)] for j in range(4)]


class test_framework(unittest.TestCase):
    def setUp(self):
        # Grid 1
        grid1[0] = [2, 2, 0, 0]
        grid1[1] = [4, 16, 8, 2]
        grid1[2] = [2, 64, 32, 4]
        grid1[3] = [1024, 1024, 64, 0]

        # Grid 2
        grid2[0] = [2, 2, 4, 8]
        grid2[1] = [4, 0, 4, 4]
        grid2[2] = [16, 16, 16, 16]
        grid2[3] = [32, 16, 16, 32]

        # Grid 3
        grid3[0] = [0, 4, 2, 4]
        grid3[1] = [0, 0, 8, 4]
        grid3[2] = [0, 16, 4, 0]
        grid3[3] = [512, 8, 512, 512]


class TestGoLeft(test_framework):
    def test_goLeft_grid1(self):
        """
        Test that equal numbers are added when swiping to the left.
        """
        result = goLeft(grid1)
        self.assertEqual(result, [
            [4, 0, 0, 0],
            [4, 16, 8, 2],
            [2, 64, 32, 4],
            [2048, 64, 0, 0]
        ])

    def test_goLeft_grid2(self):
        result = goLeft(grid2)
        self.assertEqual(result, [
            [4, 4, 8, 0],
            [8, 4, 0, 0],
            [32, 32, 0, 0],
            [32, 32, 32, 0]
        ])

    def test_goLeft_grid3(self):
        result = goLeft(grid3)
        self.assertEqual(result, [
            [4, 2, 4, 0],
            [8, 4, 0, 0],
            [16, 4, 0, 0],
            [512, 8, 1024, 0]
        ])


class TestGoRight(test_framework):
    def test_goRight_grid1(self):
        result = goRight(grid1)
        self.assertEqual(result, [
            [0, 0, 0, 4],
            [4, 16, 8, 2],
            [2, 64, 32, 4],
            [0, 0, 2048, 64]
        ])

    def test_goRight_grid2(self):
        result = goRight(grid2)
        self.assertEqual(result, [
            [0, 4, 4, 8],
            [0, 0, 4, 8],
            [0, 0, 32, 32],
            [0, 32, 32, 32]
        ])

    def test_goRight_grid3(self):
        result = goRight(grid3)
        self.assertEqual(result, [
            [0, 4, 2, 4],
            [0, 0, 8, 4],
            [0, 0, 16, 4],
            [0, 512, 8, 1024]
        ])


class TestGoUp(test_framework):
    def test_goUp_move_to_top(self):
        grid = [[0 for i in range(4)] for j in range(4)]
        grid[0] = [0, 0, 0, 0]
        grid[1] = [0, 0, 0, 0]
        grid[2] = [0, 0, 0, 0]
        grid[3] = [2, 4, 8, 16]
        result = goUp(grid)
        self.assertEqual(result, [
            [2, 4, 8, 16],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ])

    def test_goUp_merging_of_equal_numbers(self):
        grid = [[0 for i in range(4)] for j in range(4)]
        grid[0] = [0, 4, 0, 0]
        grid[1] = [2, 0, 0, 16]
        grid[2] = [0, 0, 8, 0]
        grid[3] = [2, 4, 8, 16]
        result = goUp(grid)
        self.assertEqual(result, [
            [4, 8, 16, 32],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ])

    def test_goUp_no_move_possible_means_nothing_changed(self):
        grid = [[0 for i in range(4)] for j in range(4)]
        grid[0] = [2, 32, 512, 8]
        grid[1] = [4, 64, 1024, 16]
        grid[2] = [8, 128, 2, 32]
        grid[3] = [16, 256, 4, 16]
        result = goUp(grid)
        self.assertEqual(result, grid)

    def test_goUp_grid1(self):
        result = goUp(grid1)
        self.assertEqual(result, [
            [2, 2, 8, 2],
            [4, 16, 32, 4],
            [2, 64, 64, 0],
            [1024, 1024, 0, 0]
        ])

    def test_goUp_grid2(self):
        result = goUp(grid2)
        self.assertEqual(result, [
            [2, 2, 8, 8],
            [4, 32, 32, 4],
            [16, 0, 0, 16],
            [32, 0, 0, 32]
        ])

    def test_goUp_grid3(self):
        result = goUp(grid3)
        self.assertEqual(result, [
            [512, 4, 2, 8],
            [0, 16, 8, 512],
            [0, 8, 4, 0],
            [0, 0, 512, 0]
        ])


class TestGoDown(test_framework):

    def test_goDown_stay_the_same(self):
        grid = [[0 for i in range(4)] for j in range(4)]
        grid[0] = [0, 0, 0, 0]
        grid[1] = [0, 0, 0, 0]
        grid[2] = [0, 0, 0, 0]
        grid[3] = [2, 4, 8, 16]
        result = goDown(grid)
        self.assertEqual(result, [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 4, 8, 16]
        ])

    def test_goDown_goes_all_the_way_down(self):
        grid = [[0 for i in range(4)] for j in range(4)]
        grid[0] = [2, 0, 0, 0]
        grid[1] = [0, 4, 8, 0]
        grid[2] = [0, 0, 0, 16]
        grid[3] = [0, 0, 0, 0]
        result = goDown(grid)
        self.assertEqual(result, [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 4, 8, 16]
        ])

    def test_goDown_no_move_possible_means_nothing_changed(self):
        grid = [[0 for i in range(4)] for j in range(4)]
        grid[0] = [2, 32, 512, 8]
        grid[1] = [4, 64, 1024, 16]
        grid[2] = [8, 128, 2, 32]
        grid[3] = [16, 256, 4, 16]
        result = goDown(grid)
        self.assertEqual(result, grid)

    def test_goDown_merge_equal(self):
        grid = [[0 for i in range(4)] for j in range(4)]
        grid[0] = [2, 0, 2, 16]
        grid[1] = [2, 4, 4, 0]
        grid[2] = [0, 4, 4, 16]
        grid[3] = [0, 0, 0, 0]
        result = goDown(grid)
        self.assertEqual(result, [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 2, 0],
            [4, 8, 8, 32]
        ])

    def test_goDown_grid1(self):
        result = goDown(grid1)
        self.assertEqual(result, [
            [2, 2, 0, 0],
            [4, 16, 8, 0],
            [2, 64, 32, 2],
            [1024, 1024, 64, 4]
        ])

    def test_goDown_grid2(self):
        result = goDown(grid2)
        self.assertEqual(result, [
            [2, 0, 0, 8],
            [4, 0, 0, 4],
            [16, 2, 8, 16],
            [32, 32, 32, 32]
        ])

    def test_goDown_grid3(self):
        result = goDown(grid3)
        self.assertEqual(result, [
            [0, 0, 2, 0],
            [0, 4, 8, 0],
            [0, 16, 4, 8],
            [512, 8, 512, 512]
        ])

    def test_goDown_sample_4(self):
        grid = [[0 for i in range(4)] for j in range(4)]
        grid[0] = [2, 0, 0, 2]
        grid[1] = [4, 16, 8, 2]
        grid[2] = [2, 64, 32, 4]
        grid[3] = [1024, 1024, 64, 0]
        result = goDown(grid)
        self.assertEqual(result, [
            [2, 0, 0, 0],
            [4, 16, 8, 0],
            [2, 64, 32, 4],
            [1024, 1024, 64, 4]
        ])


if __name__ == '__main__':
    unittest.main()
