import unittest

import BisectionAlgorithm as ba
import NewtonRepson as nr
import SecantAlgorithm as sc

class Test(unittest.TestCase):
	def test_bisection(self):
		self.assertEqual(ba.findRoots(lambda x : x**2, -10, 10), 0)
		self.assertEqual(ba.findRoots(lambda x : x**2 - 1, 0, 4), 1)
		self.assertEqual(ba.findRoots(lambda x : x + 8, -10, 10), -8)
		self.assertEqual(ba.findRoots(lambda x : 2*x + 8, -10, 10), -4)
		self.assertEqual(ba.findRoots(lambda x : x**4 + 11*x**3 -7*x**2 -155*x + 150, -7, -4), -5)
		self.assertEqual(ba.findRoots(lambda x : x**4 + 11*x**3 -7*x**2 -155*x + 150, -12, -4), -10)
		self.assertEqual(ba.findRoots(lambda x : x**4 + 11*x**3 -7*x**2 -155*x + 150, 0, 2), 1)
		self.assertEqual(ba.findRoots(lambda x : x**4 + 11*x**3 -7*x**2 -155*x + 150, 0, 10), 3)
		self.assertEqual(ba.findRoots(lambda x : x**2 - 25, -10, 0), -5)
		self.assertEqual(ba.findRoots(lambda x : x**2 - 25, 0, 10), 5)
		self.assertEqual(ba.findRoots(lambda x : x**2 - 25, -10, 3), -5)
		self.assertEqual(ba.findRoots(lambda x : x**2 - 25, 3, 10), 5)
		
	def test_newtonrepson(self):
		self.assertEqual(nr.findRoots(lambda x : x**2, lambda x : 2*x), 0)
		self.assertEqual(nr.findRoots(lambda x : x**2 - 1, lambda x : 2*x), 1)
		self.assertEqual(nr.findRoots(lambda x : x + 8, lambda x : 1), -8)
		self.assertEqual(nr.findRoots(lambda x : 2*x + 8, lambda x : 2), -4)
		self.assertEqual(nr.findRoots(lambda x : x**4 + 11*x**3 -7*x**2 -155*x + 150, lambda x : 4*x**3 + 3*11*x**2 -7*2*x -155), -5)
		self.assertEqual(nr.findRoots(lambda x : x**4 + 11*x**3 -7*x**2 -155*x + 150, lambda x : 4*x**3 + 3*11*x**2 -7*2*x -155), -10)
		self.assertEqual(nr.findRoots(lambda x : x**4 + 11*x**3 -7*x**2 -155*x + 150, lambda x : 4*x**3 + 3*11*x**2 -7*2*x -155), 1)
		self.assertEqual(nr.findRoots(lambda x : x**4 + 11*x**3 -7*x**2 -155*x + 150, lambda x : 4*x**3 + 3*11*x**2 -7*2*x -155), 3)
		self.assertEqual(nr.findRoots(lambda x : x**2 - 25, -10, lambda x : 2*x), 5)
	
	def test_secant(self):
		self.assertEqual(sc.findRoots(lambda x : x**2, -10, 10), 0)
		self.assertEqual(sc.findRoots(lambda x : x**2 - 1, 0, 4), 1)
		self.assertEqual(sc.findRoots(lambda x : x + 8, -10, 10), -8)
		self.assertEqual(sc.findRoots(lambda x : 2*x + 8, -10, 10), -4)
		self.assertEqual(sc.findRoots(lambda x : x**4 + 11*x**3 -7*x**2 -155*x + 150, -7, -4), -5)
		self.assertEqual(sc.findRoots(lambda x : x**4 + 11*x**3 -7*x**2 -155*x + 150, -12, -4), -10)
		self.assertEqual(sc.findRoots(lambda x : x**4 + 11*x**3 -7*x**2 -155*x + 150, 0, 2), 1)
		self.assertEqual(sc.findRoots(lambda x : x**4 + 11*x**3 -7*x**2 -155*x + 150, 0, 10), 3)
		self.assertEqual(sc.findRoots(lambda x : x**2 - 25, -10, 0), -5)
		self.assertEqual(sc.findRoots(lambda x : x**2 - 25, 0, 10), 5)
		self.assertEqual(sc.findRoots(lambda x : x**2 - 25, -10, 3), -5)
		self.assertEqual(sc.findRoots(lambda x : x**2 - 25, 3, 10), 5)
	
if __name__ == '__main__':
    unittest.main()
