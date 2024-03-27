import unittest
from io import StringIO
from unittest.mock import patch
from maze import obstacles as obs

class MyTest(unittest.TestCase):

    def test_get_obstacles(self):
        result = obs.get_obstacles()
        self.assertEqual(10 >= len(result) >= 0, True)

    def test_random_obstacles(self):
        result = obs.get_obstacles()
        self.assertEqual(10 >= len(result) >= 0, True)

    def test_is_position_blocked(self):
        obs.random.randint = lambda a,b : 1
        obs.get_obstacles()
        result = obs.is_position_blocked(1,1)
        self.assertEqual(result, True)
        result = obs.is_position_blocked(1,10)
        self.assertEqual(result, False)

    def test_is_path_blocked(self):
        obs.random.randint = lambda a,b : 1
        obs.get_obstacles()
        result = obs.is_path_blocked(1, 0, 1, 5)
        self.assertEqual(result, True)
        result = obs.is_path_blocked(10,10, 10, 20)
        self.assertEqual(result, False)

    def test_check_value(self):
        value_1 = 1
        value_2 = 5
        result = obs.check_value(value_1, value_2)
        self.assertEqual(result, (value_1, value_2))
        result = obs.check_value(value_2, value_1)
        self.assertEqual(result, (value_1, value_2))
    
if __name__ == '__main__':
    unittest.main(buffer=1)