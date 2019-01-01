from scipy import integrate
import numpy as np

f2 = lambda x: -x**2 + 10*x - 16
f = lambda x: 1/np.sqrt(np.pi) * np.exp(-x**2)
result = integrate.romberg(f2, 2, 8, show=True)
print(result)

