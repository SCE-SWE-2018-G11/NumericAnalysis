from scipy import integrate

"""
Returns:	
val : float
Gaussian quadrature approximation (within tolerance) to integral.

err : float
Difference between last two estimates of the integral.

"""

f = lambda x: -x**2 + 10*x - 16
result = integrate.quadrature(f, 2.0, 8.0)

print(result)

#print(1/9.0)  # analytical result
