import scipy
from scipy import linalg, array

def Norma(A):
    sum = 0
    temp_sum = 0
    for i in range (len(A)):
        if temp_sum >= sum:
            sum = temp_sum
        temp_sum=0
        for j in range (len(A)):
            temp_sum += abs(A[i][j])
    return sum

def invert_matrix(A):
    return linalg.inv(A)


def cond(A):
    return Norma(A)* Norma(invert_matrix(A))

def gauss(A, rounding_precision = 3):
    A = list(list(x) for x in A) # Convert to list in case we're given tuple

    n = len(A)

    for i in range(0, n):
        # Search for maximum in this column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n+1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        # Make all rows below this one 0 in current column
        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i, n+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        # Round - approximation
        x[i] = round(A[i][n]/A[i][i],rounding_precision)
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x

def interpulation(gausssolution,x):
    return gausssolution[0]*(x**2) + gausssolution[1]*x + gausssolution[2]

#A = scipy.array([[4, 2, 1, -3.5], [9, 3, 1, 1.25], [36, 6, 1, 4.1]])
#print(interpulation(gauss(A),3.83))




