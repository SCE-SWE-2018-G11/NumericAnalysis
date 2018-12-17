import numpy as np
from scipy.linalg import solve

def gaussSeidel(A, b, x, n):

    L = np.tril(A)
    U = A - L
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        print ('\n','Iter ', i, ':')
        print(x)
    return x

'''___MAIN___'''

A = np.array([[1/2, 1/3, 1/4], [1/3, 1/4, 1/5], [1/4, 1/5, 1/6]])
b = [0.95, 0.67, 0.52]
x = [1, 1, 1]

n = 100

gaussSeidel(A, b, x, n)

exit()
#print (solve(A, b))