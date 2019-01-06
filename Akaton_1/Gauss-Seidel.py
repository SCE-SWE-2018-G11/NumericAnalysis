import numpy as np
from scipy.linalg import solve

def gaussSeidel(A, b, x, n):

    L = np.tril(A)
    U = A - L
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        print('\n', 'Iter ', i, ':')
        print("x=>", x)
    return x

'''___MAIN___'''

A = np.array([[5.0, -1.0, 2.0], [3.0, 8.0, -2.0], [1.0, 1.0, 4.0]])
b = [12, -25, 6.0]
x = [0, 0, 0]

n = 10

gaussSeidel(A, b, x, n)

exit()
#print (solve(A, b))