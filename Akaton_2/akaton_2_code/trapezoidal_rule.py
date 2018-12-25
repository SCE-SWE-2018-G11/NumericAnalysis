import numpy as np

def calculate_area(f, a, b, n):
    """Return an approximation to the definite integral of f from a to b
    using the trapezium rule with n intervals.

    """
    x = np.linspace(a, b, n + 1)   # x coords of endpoints of intervals
    print("number of intervals: ", n+1)
    return np.trapz(f(x), x)

print("S = ", calculate_area(lambda x: -x**2 + 10*x - 16, 2, 8, 6))