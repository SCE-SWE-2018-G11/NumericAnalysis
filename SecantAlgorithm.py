def secant(x0, x1, n):
	'''
		TODO: Docstring
	'''
	def f(x):
		return x ** 3 + x - 1
	
    for i in range(n):
        if f(x1) - f(x0) == 0:
            return x1
        x_temp = x1 - (f(x1) * (x1 - x0) * 1.0) / (f(x1) - f(x0)) #incline between 2 dots
        x0 = x1
        x1 = x_temp
    return x1
