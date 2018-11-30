import numpy as np

def jacobi(A, b, ITERATION_LIMIT = 1000):
    """
        https://en.wikipedia.org/wiki/Jacobi_method
    """
    x = np.zeros_like(b)
    for it_count in range(ITERATION_LIMIT):
        x_new = np.zeros_like(x)

        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]

        if np.allclose(x, x_new, atol=1e-10, rtol=0.):
            break

        x = x_new
    # error = np.dot(A, x) - b
    return x

A1 = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0.0, 3., -1., 8.]])
b1 = np.array([6., 25., -11., 15.])
print(jacobi(A1, b1))
# Should be [1, 2, -1, 1]

A2 = np.array([
    [1., 0., 0.],
    [0., 1., 0.],
    [0., -0.035, 1.]
])
b2 = np.array([1., 1., 1.])
print(jacobi(A2, b2))
# should result in [1, 1, 1.035]

A3 = np.array([
    [2., 1.],
    [5., 7.]
])
b3 = np.array([11., 13.])
print(jacobi(A3, b3))
# should result in [7.111, -3.222]

A4 = np.array([
    [1., 0., 0.],
    [0., 1., 0.],
    [0., 0., 1.]
])
b4 = np.array([1., 1., 1.])
print(jacobi(A4, b4))
# should result in [1, 1, 1]

A5 = np.array([
    [2., -1., 0.],
    [-0.5, 3., -2.],
    [2., 2., 4.]
])
b5 = np.array([1., 1., 1.])
print(jacobi(A5, b5))
# Should be [0.64705882, 0.29411765, -0.22058824]
