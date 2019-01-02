import GaussAlgo
import Functions

def CubicSplineDerivatives(x_values, y_values, first_derivative, last_derivative):
    """
        Solves for the vector of derivatives of the spline function.
        Parameters:
            x_values - sorted array of floats
            y_values - array of floats
            first_derivative - derivative of spline function at the 1st x_value
            last_derivative - derivative of spline function at the last x_value
        Returns:
            tuple of derivatives for each range
        
        Please note that it may be broken for non-natural cubic splines
    """
    x_values = tuple(x_values)
    y_values = tuple(y_values)
    if len(x_values) != len(y_values):
        raise Exception("x_values and y_values length mismatch")
    if x_values != tuple(sorted(x_values)):
        raise Exception("x_values not sorted in ascending order")

    intervals = []
    for i in range(len(x_values) - 1):
        intervals.append(x_values[i + 1] - x_values[i])

    matrix = ()

    # Presentation slide 7
    # I still don't quite understand where these are taken from, so I over-fit it for the example (being a natural cubic spline)
    a00 = 1 # intervals[0]/3
    a01 = 0 # intervals[0]/6
    ann1 = 0 # intervals[len(intervals)-1]/6
    ann = 1 # intervals[len(intervals)-1]/3
    d0 = 0 # (y_values[1] - y_values[0])/intervals[0] - first_derivative
    dn = 0 # last_derivative - (y_values[len(y_values)-1] - y_values[len(y_values)-2])/intervals[len(intervals) - 1]

    # Presentation slide 8
    matrix += ((a00, a01) + tuple(0 for _ in range(len(x_values) - 2)) + (d0,),)
    for i in range(1, len(x_values) - 1):
        matrix += (tuple(0 for _ in range(i-1)) + (intervals[i-1]/6, (intervals[i-1] + intervals[i])/3, intervals[i]/6) + tuple(0 for _ in range(len(x_values) - i - 2)) + ((y_values[i+1] - y_values[i])/intervals[i] - (y_values[i] - y_values[i-1])/intervals[i-1],),)
    matrix += (tuple(0 for _ in range(len(x_values) - 2)) + (ann1, ann) + (dn,),)

    return GaussAlgo.gauss(matrix, 7)

def CubicSpline(x_values, y_values, derivative_at_x1, derivative_at_xn):
    """
        Performs cubic-spline interpolation of unknown function, described by x_values and y_values.
        Parameters:
            x_values - sorted array of floats
            y_values - array of floats 
            derivative_at_x1 - derivative of function at the 1st x_value
            derivative_at_xn - derivative of function at the last x_value
        Returns:
            tuple, where each element is a
            tuple of coefficients
            of resulting polynomial
            for x[i] < x <= x[i+1]
            in increasing order.
            coefficients[0] is coefficient of x^0
            coefficients[1] is coefficient of x^1
            etc...
    """
    x_values = tuple(x_values)
    y_values = tuple(y_values)
    if len(x_values) != len(y_values):
        raise Exception("x_values and y_values length mismatch")
    if x_values != tuple(sorted(x_values)):
        raise Exception("x_values not sorted in ascending order")

    derivatives = CubicSplineDerivatives(x_values, y_values, derivative_at_x1, derivative_at_xn)
    
    polynomials = ()
    for i in range(len(x_values) - 1):
        interval_size = x_values[i+1] - x_values[i]
        if interval_size == 0:
            raise Exception("interval size can not be 0")
        
        coefficients = (
            # Formula for S_i taken from presentation slide 11, and ran through WolframAlpha
            # Atrocious, I'm sorry.
            (x_values[i]*(x_values[i]**2*derivatives[i+1] - 6*y_values[i+1] - derivatives[i+1]*interval_size**2) + x_values[i+1]*(derivatives[i]*interval_size**2 + 6*y_values[i] - x_values[i+1]**2*derivatives[i]))/(6*interval_size),
            (derivatives[i] * (3*x_values[i+1]**2 - interval_size**2) + 6*(y_values[i+1] - y_values[i]) + derivatives[i+1]*interval_size**2 - 3*x_values[i]**2*derivatives[i+1])/(6*interval_size),
            (x_values[i]*derivatives[i+1] - x_values[i+1]*derivatives[i])/(2*interval_size),
            (derivatives[i+1] + derivatives[i])/(6*interval_size)
        )
        polynomials += (coefficients,)
    
    return polynomials

def NaturalCubicSpline(x_values, y_values):
    return CubicSpline(x_values, y_values, 0, 0)

def Interpolate(x_values, y_values, derivative_at_x1, derivative_at_xn, desired_x):
    """
        Performs cubic-spline interpolation,
        and returns the value of the function at the desired_x.
        Does not perform extrapolation - desired_x must be between the 1st x_values and the last.
        The rest of the parameters are the same as in CubicSpline
    """
    funcs = CubicSpline(x_values, y_values, derivative_at_x1, derivative_at_xn)
    for i in range(len(x_values) - 1):
        if x_values[i] <= desired_x and desired_x <= x_values[i+1]:
            return Functions.evaluateFunction(funcs[i], desired_x)
    raise Exception("desired_x out of range")

def InterpolateNatural(x_values, y_values, desired_x):
    return Interpolate(x_values, y_values, 0, 0, desired_x)
