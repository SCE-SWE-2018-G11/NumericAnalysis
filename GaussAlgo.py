import scipy
from scipy import linalg, array
from numpy import matmul

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

def invert_metrix(A):

    try:
        return linalg.inv(A)
    except Exception as e:
        return 'Not inverted!'


def cond(A):
    return Norma(A)* Norma(invert_metrix(A))

def gauss(A):

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
        x[i] = round(A[i][n]/A[i][i],3)
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x


if __name__ == "__main__":

    # Array A is with the final vector added - b
    A = scipy.array([[1, 0, 0, 1], [0, 1, 0, 1], [0, -0.035, 1, 1]])

    print(gauss(A))
    print(Norma(array([[1.01, 0.99, -2], [0.99, 1, 2.01], [0, -1, 2]])))

    a = array([[1.01, 0.99, -2], [0.99, 1, 2.01], [0, -1, 2]])
    print(invert_metrix(a))
    print(cond(a))
    exit()
