import  math

def findRoots(f, range_start, range_end, acceptable_error = 0):
	'''
		Estimates x so that f(x)=0 using bisection algorithm.
	'''
	count = 1
	m = (range_start + range_end) / 2.0
	while (range_end - range_start) / 2.0 > acceptable_error:
		print("Iteration num:", count, ", result =", m)
		if f(m) == 0:
			return m
		elif f(range_start) * f(m) < 0:
			range_end = m
		else:
			range_start = m
		m = (range_start + range_end) / 2.0
		count +=1
	return m

print("Final c = ", findRoots(lambda x:x**3+2*x**2+10*x-20, 0, 5, 0)/2,"\n")
print("Final mu (1) = ", findRoots(lambda x:math.exp(x)-3*x**2, 0, 5, 0.001)/1000, "\n")
print("Final mu (2) = ", findRoots(lambda x:math.exp(x)-3*x**2, 2, 5, 0.001)/1000)


