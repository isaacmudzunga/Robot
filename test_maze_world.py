# import unittest
# from io import StringIO
# from unittest.mock import patch
# from maze import maze_world as obstacles

# class MyTest(unittest.TestCase):

#     def test_get_obstacles(self):
#         result = obstacles.get_obstacles()
#         self.assertEqual(len(result) > 0, True)

#     def test_populate_pixels_obstacles(self):
#         result = obstacles.populate_pixels_obstacles(0,0)
#         self.assertEqual(len(result) > 0, True)

#     def test_is_position_blocked(self):
#         obstacles.random.randint = lambda a,b : 1
#         obstacles.get_obstacles()
#         result = obstacles.is_position_blocked(1,1)
#         self.assertEqual(result, False)
#         result = obstacles.is_position_blocked(1,10)
#         self.assertEqual(result, False)

#     def test_is_path_blocked(self):
#         obstacles.random.randint = lambda a,b : 1
#         obstacles.get_obstacles()
#         result = obstacles.is_path_blocked(1, 0, 1, 5)
#         self.assertEqual(result, False)
#         result = obstacles.is_path_blocked(10,10, 10, 20)
#         self.assertEqual(result, False)

#     def test_compare_values(self):
#         value_1 = 1
#         value_2 = 5
#         result = obstacles.compare_values(value_1, value_2)
#         self.assertEqual(result, (value_1, value_2))
#         result = obstacles.compare_values(value_2, value_1)
#         self.assertEqual(result, (value_1, value_2))
    
# if __name__ == '__main__':
#     unittest.main(buffer=1)