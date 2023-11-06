import unittest
from src.core.maze import Maze

class Tests(unittest.TestCase):
    def setUp(self):
        self.num_rows = 10
        self.num_cols = 5
        self.maze = Maze(self.num_rows, self.num_cols)

    def test_maze_create_grid(self):
        self.assertEqual(len(self.maze.grid), self.num_rows)
        self.assertEqual(len(self.maze.grid[0]), self.num_cols)

    def test_first_cell_open_top(self):
        expected = False
        actual = self.maze.first.walls["top"].exists
        self.assertEqual(expected, actual)

    def test_last_cell_open_bottom(self):
        expected = False
        actual = self.maze.last.walls["bottom"].exists
        self.assertEqual(expected, actual)

    def test_get_cell_above_exists(self):
        cell = self.maze.get_cell_above(self.maze.grid[1][0])
        if cell is None:
            raise Exception("no cell found")
        self.assertEqual(cell.row, 0)

    def test_get_cell_above_not_exists(self):
        cell = self.maze.get_cell_above(self.maze.first)
        if cell is None:
            self.assertTrue(True)
        else:
            raise Exception("cell shouldn't be found")

    def test_get_cell_below_exists(self):
        cell = self.maze.get_cell_below(self.maze.first)
        if cell is None:
            raise Exception("no cell found")
        self.assertEqual(cell.row, 1)

    def test_get_cell_below_not_exists(self):
        cell = self.maze.get_cell_below(self.maze.grid[self.num_rows - 1][0])
        if cell is None:
            self.assertTrue(True)
        else:
            raise Exception("cell shouldn't be found")

    def test_get_cell_left_of_exists(self):
        cell = self.maze.get_cell_left_of(self.maze.grid[0][1])
        if cell is None:
            raise Exception("no cell found")
        self.assertEqual(cell.col, 0)

    def test_get_cell_left_of_not_exists(self):
        cell = self.maze.get_cell_left_of(self.maze.first)
        if cell is None:
            self.assertTrue(True)
        else:
            raise Exception("cell shouldn't be found")

    def test_get_cell_right_of_exists(self):
        cell = self.maze.get_cell_right_of(self.maze.first)
        if cell is None:
            raise Exception("no cell found")
        self.assertEqual(cell.col, 1)

    def test_get_cell_right_of_not_exists(self):
        cell = self.maze.get_cell_right_of(self.maze.grid[0][self.num_cols - 1])
        if cell is None:
            self.assertTrue(True)
        else:
            raise Exception("cell shouldn't be found")

if __name__ == "__main__":
    unittest.main()
