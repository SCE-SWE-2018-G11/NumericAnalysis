import scipy.interpolate._cubic as interpolate
import numpy as np

cubin = interpolate.CubicSpline([1,2,3,4,5],[1,2,1,1.5,1])
print(cubin)


