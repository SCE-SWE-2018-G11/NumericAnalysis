from math import *

def findRoots(f, derivative, x0=1):
	'''
		Estimates x so that f(x)=0 using newton-repson algorithm.
	'''
	acceptable_error = 1e-3

	x = float(x0)
	i = 0
	while abs(f(x)) > acceptable_error:
		x = x - f(x) / derivative(x)
		print("Iteration {0} = {1}".format(i, x))
		i += 1
	return x

print("result:", findRoots(lambda x:x**2-2*x, lambda x:2*x-2,800 ),"\n")