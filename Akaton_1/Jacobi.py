import scipy
import numpy as np


def Jacobi(A, b, x, n):
    D = np.diag(A)
    R = A - np.diagflat(D)

    for i in range(n):
        x = (b - np.dot(R, x)) / D
        print("Iteration {0}: {1}".format(i, x))
    return x

Jacobi(np.array([[5.0, -1.0, 2.0], [3.0, 8.0, -2.0],
                        [1.0, 1.0, 4.0]]), [12, -25, 6.0], np.array([0.0, 0.0, 0.0]), 22)

