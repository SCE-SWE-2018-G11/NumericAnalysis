import math
def findRoots(f, range_start, range_end, iterations):
	'''
		Estimates x so that f(x)=0 using secant algorithm.
	'''
	for i in range(iterations):
		if f(range_end) - f(range_start) == 0:
			return range_end
		x_temp = range_end - (f(range_end) * (range_end - range_start) * 1.0) / (f(range_end) - f(range_start))
		range_start = range_end
		range_end = x_temp
		print("Iteration num:", i, ", result = ", range_end)
	return range_end

print(findRoots(lambda x:x**2-2*x, 1, 10,100), "\n")

