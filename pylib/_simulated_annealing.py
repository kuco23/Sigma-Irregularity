from math import log, exp
from random import random, randint
from copy import deepcopy

from ._base_defs import sigmaRatio
from ._random_graphs import (
    randomConnectedGraph,
    randomSigmaOptAprox
)

def maxSigmaRatio_annealing(
    n, m, nsim, alterLocal,
    defaultG=None
):
    prob = lambda ci, cr, t: exp((ci - cr) / t)
    temp = lambda i: 1 / log(i)
    
    curi = defaultG or randomSigmaOptAprox(n, n // 2, m)
    srat = sigmaRatio(curi)
    best = (deepcopy(curi), srat)
    curr = (deepcopy(curi), srat)
    
    for i in range(2, nsim + 2):
        t = temp(i)
        srat = alterLocal(curi, 5)

        if srat >= curr[1]:
            curr = (deepcopy(curi), srat)
            if srat > best[1]:
                best = (deepcopy(curi), srat)
                
        elif prob(srat, curr[1], t) > random():
            curr = (deepcopy(curi), srat)

    return best
    
