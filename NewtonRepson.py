from math import *

def NR(f, f_tag, x0):
	'''
		TODO: Docstring
	'''
	eps = 1e-3
	
    x = float(x0)
    while abs(f(x)) > eps:
        x = x - f(x) / f_tag(x)
    return f(x)
