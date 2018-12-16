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
