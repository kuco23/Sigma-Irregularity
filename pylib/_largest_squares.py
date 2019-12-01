from math import sqrt, inf
from operator import mul

def scalarProduct(u, v):
    return sum(map(mul, u, v))

def _diff(c, x, b):
    return sqrt(sum(map(
        lambda y: y * y,
        map(lambda y, d: c * y - d, x, b)
    )))

def squares(x, a):
    norm = scalarProduct(x, x)
    prod = scalarProduct(x, a)
    c = prod / norm
    return c, _diff(c, x, a)

def powerAproximation(data, p0, p1, k, nrange):
    it, t, n = [], p0, len(data)
    while t <= p1:
        it.append(t)
        t += (p1 - p0) / k

    diffopt, copt, popt = inf, 0, 0
    for p in it:
        x = [pow(i, p) for i in nrange]
        c, d = squares(x, data)
        if d < diffopt:
            diffopt = d
            copt, popt = c, p

    return diffopt, copt, popt
