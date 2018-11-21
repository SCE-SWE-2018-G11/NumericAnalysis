'''
	Convention:
	When passing coefficients of a polynomial, they're in increasing order.
	coefficients[0] is coefficient of x^0
	coefficients[1] is coefficient of x^1
	etc...
'''

def findDerivativeCoefficients(original_coefficients):
	derivative_coefficients = []
	for i in range(1, len(original_coefficients)):
		derivative_coefficients.append(original_coefficients[i] * i)
	return derivative_coefficients

def evaluateFunction(coefficients, x):
	sum = 0
	for i in range(0, len(coefficients)):
		sum += coefficients[i] * pow(x, i)
	return sum
