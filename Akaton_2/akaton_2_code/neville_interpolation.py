def neville(datax, datay, x):
    """
    Finds an interpolated value using Neville's algorithm.
    Input
      datax: input x's in a list of size n
      datay: input y's in a list of size n
      x: the x value used for interpolation
    Output
      p[0]: the polynomial of degree n
    """
    n = len(datax)
    p = n*[0]
    for k in range(n):
        for i in range(n-k):
            if k == 0:
                p[i] = datay[i]
            else:
                p[i] = ((x-datax[i+k])*p[i]+ \
                        (datax[i]-x)*p[i+1])/ \
                        (datax[i]-datax[i+k])
            print('P{0}{1} = {2}'.format(i, k, p[i]))
    return ('Result => P{0}{1}({3}) = {2}'.format(i, k, p[0],x))

p = neville([1.0, 2.0, 6.0], [1.0, -1.0, 4.0], 4)
print(p)