from scipy import integrate

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.simps.html
# 1st argument is y values, 2nd argument is x values
print(integrate.simps([0, 5, 8, 9, 8, 5, 0], [2, 3, 4, 5, 6, 7, 8]))
# should be 35.0