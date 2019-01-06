import scipy.interpolate as interpol
import matplotlib.pyplot as p
import numpy as np

# Example - some points in an array
points_table = [(2, -3.6), (3, 1.25), (6, 4.1)]
#points_table = [(0.2, 0.198669), (0.3, 0.295520), (0.4, 0.389418), (0.5, 0.479426)]

# We choose 3 points from the table, so that the function f(x) will be in order 2
xp = [points_table[0][0], points_table[1][0], points_table[2][0]]
yp = [points_table[0][1], points_table[1][1], points_table[2][1]]

# We calculate lagrange interpolation by sending 3 points and receiving function back
f = interpol.lagrange(xp, yp)
#print(f)

# Now if we wish to get particular value of some x that
# is not in the table, we just place x in the function, for example - x = 2.5
x = 4
print('f({0}) = {1}'.format(x, f(x)))

# Show the function on the screen
# arr_x_values = range(0, 1)
#
# p.plot(arr_x_values, f(arr_x_values).astype(np.int))
# p.show()