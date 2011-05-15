import unittest
from solver import Solver

class TestSolver(unittest.TestCase):
	def setUp(self):
		self.solver = Solver()
		pass

	def test_simple_maze(self):
		maze = [[0, 0], [0, 0]]
		start = 1, 1
		self.assertEqual(self.solver.solve(maze, start)[1], 
								[(1, 1), (0, 1), (0, 0)])

	def test_3_side_maze(self):
		maze = [[0, 1, 1], [0, 1, 1], [0, 0, 0]]
		start = 2, 2
		self.assertEqual(self.solver.solve(maze, start)[1],
								[(2, 2), (2, 1), (2, 0), (1, 0), (0, 0)])

	def test_3_side_maze_again(self):
		maze = [[1, 1, 1], [0, 1, 1], [0, 0, 0]]
		start = 2, 2
		self.assertFalse(self.solver.solve(maze, start)[0])


	
suite = unittest.TestLoader().loadTestsFromTestCase(TestSolver)
unittest.TextTestRunner(verbosity = 2).run(suite)
