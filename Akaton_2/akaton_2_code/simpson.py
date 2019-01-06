from scipy import integrate

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.simps.html
def simpson(y, x):
    return integrate.simps(y, x)

xp = [0, 0.5, 1, 3/2, 2, 5/2, 3]
yp = [1, 32/33, 1/2, 32/275, 1/33, 32/3157, 1/244]
print("Integral:", simpson(yp, xp))