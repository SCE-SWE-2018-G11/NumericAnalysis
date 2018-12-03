import math
def findRoots(f, range_start, range_end, iterations=10):
	'''
		Estimates x so that f(x)=0 using secant algorithm.
	'''
	for i in range(iterations):
		print("Iteration num:", i, ", result = ", range_end)
		if f(range_end) - f(range_start) == 0:
			return range_end
		x_temp = range_end - (f(range_end) * (range_end - range_start) * 1.0) / (f(range_end) - f(range_start))
		range_start = range_end
		range_end = x_temp
	return range_end

print("Final c = " , findRoots(lambda x:x**3+2*x**2+10*x-20, 0, 5, 20), "\n")
print("Final mu (1) = " , findRoots(lambda x:math.exp(x)-3*x**2, 2, 5, 20), "\n")
print("Final mu (2) = ", findRoots(lambda x:math.exp(x)-3*x**2, 4, 5, 20))
