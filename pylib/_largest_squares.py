from math import sqrt, inf
from operator import mul

def scalarProduct(u, v):
    return sum(map(mul, u, v))

def _diff(c, x, b):
    return sqrt(sum(map(
        lambda y: y * y,
        map(lambda y, d: c * y - d, x, b)
    )))

def powerAproximation(data, p0, p1, k, nrange):
    it, t, n = [], p0, len(data)
    while t <= p1:
        it.append(t)
        t += (p1 - p0) / k

    diffopt, copt, popt = inf, 0, 0
    for p in it:
        rng = [pow(i, p) for i in nrange]
        norm = scalarProduct(rng, rng)
        prod = scalarProduct(data, rng)
        c = prod / norm
        df = _diff(c, rng, data)
        if df < diffopt:
            diffopt = df
            copt, popt = c, p

    return diffopt, copt, popt
