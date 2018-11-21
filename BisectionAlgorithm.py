def bisection(a, b, tol):
	'''
		TODO: Docstring
	'''
	def f(x):
		return x ** 3 - 6*x + 9
	
    m = (a + b) / 2.0
    while (b - a) / 2.0 > tol:
        if f(m) == 0:
            return m
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
        m = (a + b) / 2.0
    return m
