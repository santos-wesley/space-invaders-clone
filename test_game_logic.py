import unittest
from game_logic import is_collision

class TestGameLogic(unittest.TestCase):

    def test_collision_true(self):
        """Test that is_collision returns True when objects are within the desired distance."""
        self.assertTrue(is_collision(0, 0, 2, 3, 5))  # Objects are less than 5 units apart


    def test_collision_false(self):
        """Test that is_collision returns False when objects are not within the desired distance."""
        self.assertFalse(is_collision(0, 0, 10, 10, 5))  # Objects are more than 5 units apart

    def test_collision_at_exact_distance(self):
        """Test that is_collision returns False when objects are exactly at the desired distance."""
        self.assertFalse(is_collision(0, 0, 3, 4, 4))  # Objects are exactly 5 units apart

if __name__ == '__main__':
    unittest.main()
