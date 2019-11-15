from math import log, exp
from random import random, randint
from copy import deepcopy

from ._base_defs import sigmaRatio
from ._random_graphs import (
    randomConnectedGraph,
    randomSigmaOptAprox
)

def maxSigmaRatio_annealing_modified(
    n, m, nsim, alterLocal, alterGlobal
):
    prob = lambda ci, cr, t: exp((ci - cr) / t)
    temp = lambda i: 1 / log(i)
    
    curi = randomSigmaOptAprox(n, m)
    sri = sigmaRatio(curi)
    bes = (deepcopy(curi), sri)
    cur = (deepcopy(curi), sri)

    stucknum = 0
    for i in range(2, nsim + 2):
        t = temp(i)
        sri = alterLocal(curi, 4)

        if sri >= cur[1]:
            cur = (deepcopy(curi), sri)
            if sri > bes[1]:
                bes = (deepcopy(curi), sri)
                
        elif prob(sri, cur[1], t) > random():
            cur = (deepcopy(curi), sri)
            
        else:
            stucknum += 1
            if stucknum > nsim // 4:
                alterGlobal(curi, t)
                stucknum = 0

    return bes
    
