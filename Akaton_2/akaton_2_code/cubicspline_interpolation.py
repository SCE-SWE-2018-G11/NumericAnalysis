#from scipy.interpolate import CubicSpline
#from scipy import linalg

#x_points = [1.0, 2.0, 3.0, 4.0, 5.0]
#y_points = [1.0, 2.0, 1.0, 1.5, 1.0]

#cs = CubicSpline(x_points, y_points, bc_type='natural')
#derivative = cs.derivative()
#print(derivative)
#print(linalg.solve(cs.c, derivative.c))

#!/usr/bin/env python3

import numpy as np
from scipy.interpolate import CubicSpline

# calculate 5 natural cubic spline polynomials for 6 points
# (x,y) = (0,12) (1,14) (2,22) (3,39) (4,58) (5,77)
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([1.0, 2.0, 1.0, 1.5, 1.0])

# calculate natural cubic spline polynomials
cs = CubicSpline(x,y,bc_type='natural')

# show values of interpolation function at x=1.25
print('S(2) = ', cs(2))

## Aditional - find polynomial coefficients for different x regions

# if you want to print polynomial coefficients in form
# S0(0<=x<=1) = a0 + b0(x-x0) + c0(x-x0)^2 + d0(x-x0)^3
# S1(1< x<=2) = a1 + b1(x-x1) + c1(x-x1)^2 + d1(x-x1)^3
# ...
# S4(4< x<=5) = a4 + b4(x-x4) + c5(x-x4)^2 + d5(x-x4)^3
# x0 = 0; x1 = 1; x4 = 4; (start of x region interval)

# show values of a0, b0, c0, d0, a1, b1, c1, d1 ...
cs.c

# Polynomial coefficients for 0 <= x <= 1
a0 = cs.c.item(3,0)
b0 = cs.c.item(2,0)
c0 = cs.c.item(1,0)
d0 = cs.c.item(0,0)

# Polynomial coefficients for 1 < x <= 2
a1 = cs.c.item(3,1)
b1 = cs.c.item(2,1)
c1 = cs.c.item(1,1)
d1 = cs.c.item(0,1)

# 2
a2 = cs.c.item(3,2)
b2 = cs.c.item(2,2)
c2 = cs.c.item(1,2)
d2 = cs.c.item(0,2)



# ...

# Polynomial coefficients for 4 < x <= 5
#a4 = cs.c.item(3,4)
#b4 = cs.c.item(2,4)
#c4 = cs.c.item(1,4)
#d4 = cs.c.item(0,4)

# Print polynomial equations for different x regions
print('S0(0<=x<=1) = ', a0, ' + ', b0, '(x-0) + ', c0, '(x-0)^2  + ', d0, '(x-0)^3')
print('S1(1< x<=2) = ', a1, ' + ', b1, '(x-1) + ', c1, '(x-1)^2  + ', d1, '(x-1)^3')
print('...')
#print('S5(4< x<=5) = ', a4, ' + ', b4, '(x-4) + ', c4, '(x-4)^2  + ', d4, '(x-4)^3')

# So we can calculate S(2) by using equation S1(1< x<=2)
print('S(3) = ', a2 + b2*0.25 + c2*(0.25**2) + d2*(0.25**3))

# Cubic spline interpolation calculus example
    #  https://www.youtube.com/watch?v=gT7F3TWihvk