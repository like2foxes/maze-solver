import unittest
from src.core.cell import Cell

class Tests(unittest.TestCase):
    def setUp(self):
        self.top_left = Cell(0,0)
        self.bottom_left = Cell(1,0)
        self.top_right = Cell(0,1)
        self.bottom_right = Cell(1,1)

    def test_is_above(self):
        self.assertTrue(self.top_left.is_above(self.bottom_left))
        self.assertFalse(self.bottom_right.is_above(self.top_right))

    def test_is_below(self):
        self.assertTrue(self.bottom_right.is_below(self.top_right))
        self.assertFalse(self.top_left.is_below(self.bottom_left))

    def test_is_right_of(self):
        self.assertTrue(self.top_right.is_right_of(self.top_left))
        self.assertFalse(self.top_left.is_right_of(self.top_right))

    def test_is_left_of(self):
        self.assertTrue(self.top_left.is_left_of(self.top_right))
        self.assertFalse(self.top_right.is_left_of(self.top_left))

    def test_is_path_clear_to(self):
        not_clear_above = self.bottom_left.has_open_path_to(self.top_left)
        not_clear_below = self.top_left.has_open_path_to(self.bottom_left)
        not_clear_to_right = self.top_left.has_open_path_to(self.top_right)
        not_clear_to_left = self.top_right.has_open_path_to(self.top_left)

        self.bottom_left.break_connecting_wall_to(self.top_left)
        self.top_left.break_connecting_wall_to(self.bottom_left)
        self.top_left.break_connecting_wall_to(self.top_right)
        self.top_right.break_connecting_wall_to(self.top_left)

        clear_above = self.bottom_left.has_open_path_to(self.top_left)
        clear_below = self.top_left.has_open_path_to(self.bottom_left)
        clear_to_right = self.top_left.has_open_path_to(self.top_right)
        clear_to_left = self.top_right.has_open_path_to(self.top_left)

        self.assertFalse(not_clear_above)
        self.assertFalse(not_clear_below)
        self.assertFalse(not_clear_to_right)
        self.assertFalse(not_clear_to_left)

        self.assertTrue(clear_above)
        self.assertTrue(clear_below)
        self.assertTrue(clear_to_right)
        self.assertTrue(clear_to_left)
