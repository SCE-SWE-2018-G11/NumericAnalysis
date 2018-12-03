import math
import GaussAlgo as ga
import numpy
import scipy

AREA_SIZE = 4
GRID_RESOLUTION = 2 # N
HELICOPTER_HEIGHT = 150 # h
MONITOR_PROPORTION_COEF = 1 # c
RADIATION_ABSORPTION_COEF = 1 # mu
RADIATION_BUILDUP_FAC = 1 # k

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + HELICOPTER_HEIGHT**2)

def detectorResponseToCell(helicopter_cell, cell):
    """
        Given helicopter over a cell, calculate detector response to particular cell
    """
    helicopter_x = (helicopter_cell % GRID_RESOLUTION) * AREA_SIZE
    helicopter_y = (helicopter_cell / GRID_RESOLUTION) * AREA_SIZE
    cell_x = (cell % GRID_RESOLUTION) * AREA_SIZE
    cell_y = (cell / GRID_RESOLUTION) * AREA_SIZE
    d = distance(helicopter_x, helicopter_y, cell_x, cell_y)
    return (MONITOR_PROPORTION_COEF * (1 + RADIATION_BUILDUP_FAC * HELICOPTER_HEIGHT) * math.exp(-1 * RADIATION_ABSORPTION_COEF * d)) / d**2

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

    except _: # `response_matrix` not invertable
        for i in range(GRID_RESOLUTION):
            response_matrix.append(measured_values_vector[i])
        scipysh = scipy.array(response_matrix)
        return ga.gauss(scipysh)

print(calculateContaminationVector([1, 1]))

'Caluclate distances'
print("R(1,1) =", distance(-50,50, 50,50))
print("R(1,2) =", distance())
