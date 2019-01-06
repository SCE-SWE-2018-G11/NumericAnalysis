from scipy import integrate

"""
Returns:	
val : float
Gaussian quadrature approximation (within tolerance) to integral.

err : float
Difference between last two estimates of the integral.

"""

f = lambda x: -x**2 + 10*x - 16
result = integrate.quadrature(lambda x: 1/(1 + x**5), 0, 3)

print(result)

#print(1/9.0)  # analytical result
