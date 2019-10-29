from math import log, exp
from random import random, randint

from ._base_defs import sigmaRatio
from ._random_graphs import (
    randomConnectedGraph
)

def maxSigmaRatio_annealing(
    n, m, nsim, temperature, alterState
):
    m_total = n * (n - 1) // 2
    
    prob = lambda ci, cr, t: exp((ci - cr) / t)
    temp = lambda i: temperature * log(nsim) / log(i)
    
    curi = randomConnectedGraph(n, m)
    sri = sigmaRatio(curi)
    bes = (curi.copy(), sri)
    cur = (curi.copy(), sri)

    for i in range(2, nsim + 2):
        t = temp(i)
        alterState(curi)
        sri = sigmaRatio(curi)

        if sri >= cur[1]:
            cur = (curi.copy(), sri)
            if sri > bes[1]:
                bes = (curi.copy(), sri)
                
        elif prob(sri, cur[1], t) > random():
            cur = (curi.copy(), sri)

    return bes
    
