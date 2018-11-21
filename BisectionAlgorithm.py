def findRoots(f, range_start, range_end, acceptable_error = 0):
	'''
		Estimates x so that f(x)=0 using bisection algorithm.
	'''
	m = (range_start + range_end) / 2.0
	while (range_end - range_start) / 2.0 > acceptable_error:
		if f(m) == 0:
			return m
		elif f(range_start) * f(m) < 0:
			range_end = m
		else:
			range_start = m
		m = (range_start + range_end) / 2.0
	return m
