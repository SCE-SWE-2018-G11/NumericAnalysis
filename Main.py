import math

area_size = 4
grid_resolution = 4 # N
radiation_buildup_factor = 1 # k
measurement_height = 10 # h
monitor_proportion_coefficient = 1 # c
radiation_absorbtion_coefficient = 1 # μ
measurements_vector = [0, 0, 0, 0] # M

def calculateRadioactivity(heli_x, heli_y):
    def calculateDistance(point_x, point_y):
        return math.sqrt((heli_x - point_x) ** 2 + (heli_y, point_y) ** 2 + measurement_height ** 2)

    radioactivity = 0
    for i in range(grid_resolution):
        for j in range(grid_resolution):
            distance = calculateDistance(j * area_size, i * area_size) # R
            nom = monitor_proportion_coefficient * (1 + radiation_buildup_factor * distance) * math.exp(-1 * radiation_absorbtion_coefficient * distance)
            denom = distance ** 2
            radioactivity += nom / denom
    return radioactivity

def calculateCoefficientsMatrix():
    coefficients_matrix = []# D
    for i in range(grid_resolution):
        vec = []
        for j in range(grid_resolution):
            vec.append(calculateRadioactivity(j * area_size, i * area_size))
        coefficients_matrix.append(vec)
    return coefficients_matrix

def calculateRadioactiveIsotopes(measurements):
    coefficients_matrix = calculateCoefficientsMatrix() # D
    # TODO: Check if matrix is invertible
    # TODO: If not, calculate somehow else (gauss elim?)
    inverted = invertMatrix(coefficients_matrix)
    return inverted * measurements

calculateRadioactiveIsotopes(measurements_vector)
