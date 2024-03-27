# import unittest
# from io import StringIO
# from unittest.mock import patch
# import sys
# import maze_engine
# from maze import maze_world as obs
# import robot

# class MyTests(unittest.TestCase):

#     @patch("sys.stdin", StringIO('HAL\nmazerun\noff\n'))
#     def test_edge_finder(self):
#         sys.stdout = StringIO()
#         obs.random.randint = lambda a, b: 1
#         robot.robot_start()

#         output = sys.stdout.getvalue()
#         self.assertTrue(output.find('starting maze run..') > -1)
#         self.assertTrue(output.find('I am at the top edge') > -1)

#     def test_convert_instructions(self):
#         instruct = ["L","L","R","L", "D", "D", "R"]
#         result = maze_engine.convert_instructions(instruct, [])
#         self.assertEqual(result,[('L', 10), ('R', 5), ('L', 5), ('D', 10)])

#     def test_convert_coordinates(self):
#         result = maze_engine.convert_coordinates(10, 3, "U", "D")
#         self.assertEqual(result,"D")
#         result = maze_engine.convert_coordinates(0, 3, "R", "L")
#         self.assertEqual(result,"R")

#     def test_instruct_(self):
#         wayout = [(0,0),(0,5),(5,0)]
#         result = maze_engine.instruct_(wayout, [])
#         self.assertEqual(result, [('U', 5), ('R', 5)])

#     def test_back_path(self):
#         solution = {(0,10): (0,10), (0,5): (0,10), (0,0): (0,5)}
#         result = maze_engine.back_path(solution, 0, 10, 0, 0)
#         self.assertEqual(result, [('U', 10)])

#     @patch("sys.stdin", StringIO('HAL\nmazerun\nmazerun bottom\noff\n'))
#     def test_search_route(self):
#         sys.stdout = StringIO()
#         obs.random.randint = lambda a, b: 1
#         robot.robot_start()

#         output = sys.stdout.getvalue()
#         self.assertTrue(output.find('starting maze run..') > -1)
#         self.assertTrue(output.find('I am at the top edge') > -1)
#         self.assertTrue(output.find('I am at the bottom edge') > -1)
        
# if __name__ == '__main__':
#     unittest.main(buffer=1)