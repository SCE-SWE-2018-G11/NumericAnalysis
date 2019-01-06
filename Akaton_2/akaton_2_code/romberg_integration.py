
from scipy import integrate
import numpy as np

def romberg(f, a, b):

    return integrate.romberg(f, a, b, show=True)
print("Integral: ", romberg(lambda x: 1/(1+ x**5), 0, 3))
