import unittest

import BisectionAlgorithm as ba
import NewtonRepson as nr
import SecantAlgorithm as sc
import Functions as fun
import Matrix as mat

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
	
	def test_fun(self):
		self.assertEqual(fun.evaluateFunction([],  0), 0)
		self.assertEqual(fun.evaluateFunction([0], 0), 0)
		self.assertEqual(fun.evaluateFunction([1], 0), 1)
		self.assertEqual(fun.evaluateFunction([1], 5), 1)
		self.assertEqual(fun.evaluateFunction([2], 5), 2)
		self.assertEqual(fun.evaluateFunction([0, 0], 5), 0)
		self.assertEqual(fun.evaluateFunction([0, 1], 5), 5)
		self.assertEqual(fun.evaluateFunction([0, 2], 5), 10)
		self.assertEqual(fun.evaluateFunction([1, 2], 5), 11)
		
		self.assertEqual(fun.findDerivativeCoefficients([]), [])
		self.assertEqual(fun.findDerivativeCoefficients([1]), [])
		self.assertEqual(fun.findDerivativeCoefficients([5]), [])
		self.assertEqual(fun.findDerivativeCoefficients([0, 1]), [1])
		self.assertEqual(fun.findDerivativeCoefficients([5, 1]), [1])
		self.assertEqual(fun.findDerivativeCoefficients([0, 3]), [3])
		self.assertEqual(fun.findDerivativeCoefficients([5, 3]), [3])
		self.assertEqual(fun.findDerivativeCoefficients([5, 3, 1]), [3, 2])
		self.assertEqual(fun.findDerivativeCoefficients([5, 3, 5]), [3, 10])
		self.assertEqual(fun.findDerivativeCoefficients([5, 3, 5, 1]), [3, 10, 3])
		
		self.assertEqual(fun.coefficientsToFunction([0])(0), 0)
		self.assertEqual(fun.coefficientsToFunction([1])(0), 1)
		self.assertEqual(fun.coefficientsToFunction([1])(5), 1)
		self.assertEqual(fun.coefficientsToFunction([2])(5), 2)
		self.assertEqual(fun.coefficientsToFunction([0, 0])(5), 0)
		self.assertEqual(fun.coefficientsToFunction([0, 1])(5), 5)
		self.assertEqual(fun.coefficientsToFunction([0, 2])(5), 10)
		self.assertEqual(fun.coefficientsToFunction([1, 2])(5), 11)
	
	def test_matrix(self):
		self.assertEqual(mat.Matrix(2, 2).data, [[0, 0], [0, 0]])
		self.assertEqual((mat.Matrix(2, 2) * 2).data, [[0, 0], [0, 0]])
		self.assertEqual((2 * mat.Matrix(2, 2)).data, [[0, 0], [0, 0]])
		
		matrix = mat.Matrix(2, 2)
		matrix.setAt(0, 0, 1)
		matrix.setAt(1, 1, 1)
		self.assertEqual(matrix.data, [[1, 0], [0, 1]])
		self.assertEqual((2*matrix).data, [[2, 0], [0, 2]])
		self.assertEqual((matrix*2).data, [[2, 0], [0, 2]])
		matrix2 = mat.Matrix(3, 2)
		matrix2.setAt(0, 0, 1)
		matrix2.setAt(0, 1, 1)
		matrix2.setAt(1, 0, 1)
		matrix2.setAt(1, 1, 1)
		matrix2.setAt(2, 0, 1)
		matrix2.setAt(2, 1, 1)
		self.assertEqual((matrix2).data, [[1, 1, 1], [1, 1, 1]])
		self.assertEqual((2 * matrix2).data, [[2, 2, 2], [2, 2, 2]])
		self.assertEqual((matrix * matrix2).data, [[1, 1, 1], [1, 1, 1]])
		self.assertEqual((2 * matrix * matrix2).data, [[2, 2, 2], [2, 2, 2]])
		
		matrix3 = mat.Matrix(2, 2)
		matrix3.setAt(0, 0, 1)
		matrix3.setAt(1, 0, 2)
		matrix3.setAt(0, 1, 0)
		matrix3.setAt(1, 1, 3)
		self.assertEqual((matrix3 * matrix2).data, [[3, 3, 3], [3, 3, 3]])
	
if __name__ == '__main__':
    unittest.main()
