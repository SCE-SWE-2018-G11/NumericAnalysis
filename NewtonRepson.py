from math import *

def findRoots(f, derivative, x0=1):
	'''
		Estimates x so that f(x)=0 using newton-repson algorithm.
	'''
	acceptable_error = 1e-3
	
	x = float(x0)
	while abs(f(x)) > acceptable_error:
		x = x - f(x) / derivative(x)
	return x
