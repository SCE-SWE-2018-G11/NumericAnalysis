import math
import GaussAlgo as ga
import numpy
import scipy

AREA_SIZE = 4
GRID_RESOLUTION = 2 # N
HELICOPTER_HEIGHT = 150 # h
MONITOR_PROPORTION_COEF = 0.6844040539 # c
RADIATION_ABSORPTION_COEF = 0.000910007 # mu
RADIATION_BUILDUP_FAC = 3.749545 # k


# --------------------------------------------------------------------
#                            New code
# --------------------------------------------------------------------

pointArray = [(-50, 50), (50, 50), (50, -50), (-50, -50)]
R = scipy.array([[0.0, 0.0, 0.0 ,0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]])
D = scipy.array([[0.0, 0.0, 0.0 ,0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]])

# The measured values vector
M = scipy.array([1250, 1550, 1100, 1400])

def distance(x1, y1, x2, y2):

    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + HELICOPTER_HEIGHT**2)

def detectorResponseToCell(r):
    """
            Given helicopter over a cell, calculate detector response to particular cell
    """
    return (((MONITOR_PROPORTION_COEF) * (1 + (RADIATION_BUILDUP_FAC * r)) * (math.exp(-1 * RADIATION_ABSORPTION_COEF * r))) / (r) ** 2)

def fill_R(pointArray, R):
    ''' Calculate the distance from each cell(=point) to the others'''

    for i in range(AREA_SIZE):
        (x1, y1) = pointArray[i]
        for j in range(AREA_SIZE):
                (x2, y2) = pointArray[j]
                R[i][j] = distance(x1, y1, x2, y2)
    return R

def fill_D(R, D):

    ''' Calculate Dij matrix by the distances that were found '''

    for i in range(AREA_SIZE):
        for j in range(AREA_SIZE):
            D[i][j] = detectorResponseToCell(R[i][j])
    return D

def merge_matrix_vector(D, M):

    ''' merge between D matrix and M measured values vector '''

    M = scipy.array((1250, 1550, 1100, 1400)).reshape(4, 1)
    D = scipy.hstack((D, M))

    return D

# Main

R = fill_R(pointArray, R)
D = fill_D(R, D)

# inverted method
C = ga.invert_matrix(D).dot(M)
print("Inverted method - C :  ", C)

D = merge_matrix_vector(D, M)

# gauss method
C = ga.gauss(D)
print("Gauss method - C:      ", C)

#print(D)
#D = scipy.array([[0.01495167, 0.01212059, 0.01212059 ,0.01034123, 1250],
#                 [0.01495167, 0.01212059, 0.01212059, 0.01034123, 1550],
#                 [0.01495167, 0.01212059, 0.01212059, 0.01034123, 1100],
#                 [0.01495167, 0.01212059, 0.01212059, 0.01034123, 1400]])




'''
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + HELICOPTER_HEIGHT**2)

def detectorResponseToCell(r):
    """
        Given helicopter over a cell, calculate detector response to particular cell
    """
    helicopter_x = (helicopter_cell % GRID_RESOLUTION) * AREA_SIZE
    helicopter_y = (helicopter_cell / GRID_RESOLUTION) * AREA_SIZE
    cell_x = (cell % GRID_RESOLUTION) * AREA_SIZE
    cell_y = (cell / GRID_RESOLUTION) * AREA_SIZE
    r = distance(helicopter_x, helicopter_y, cell_x, cell_y)

    return (((MONITOR_PROPORTION_COEF)* (1 + (RADIATION_BUILDUP_FAC * r)) * (math.exp(-1*RADIATION_ABSORPTION_COEF*r))) /(r)**2)


def detectorResponseToArea(helicopter_cell, contamination_vector):
    """
        Given contamination vector, calculates expected helicopter measurement over a cell
    """
    helicopter_x = (helicopter_cell % GRID_RESOLUTION) * AREA_SIZE
    helicopter_y = (helicopter_cell / GRID_RESOLUTION) * AREA_SIZE
    sum = 0
    for j in range(GRID_RESOLUTION ** 2):
        cell_x = (j % GRID_RESOLUTION) * AREA_SIZE
        cell_y = (j / GRID_RESOLUTION) * AREA_SIZE
        sum += distance(helicopter_x, helicopter_y, cell_x, cell_y) * contamination_vector[j]
    return sum

def detectorResponseMatrix():
    """
        Creates a matrix of detector response over each cell
    """
    vec = []
    for i in range(GRID_RESOLUTION):
        vec2 = []
        for j in range(GRID_RESOLUTION):
            vec2.append(detectorResponseToCell(i, j))
        vec.append(vec2)
    return vec

def calculateContaminationVector(measured_values_vector):
    """
        Given measured values, calculates the radioactive isotope contamination of each grid cell
    """
    response_matrix = scipy.array(detectorResponseMatrix())
    try:
        inv = ga.invert_matrix(response_matrix)
        return inv * scipy.array(measured_values_vector)

    except Exception: # `response_matrix` not invertable
        for i in range(GRID_RESOLUTION):
            response_matrix.append(measured_values_vector[i])
        scipysh = scipy.array(response_matrix)
        return ga.gauss(scipysh)
'''

