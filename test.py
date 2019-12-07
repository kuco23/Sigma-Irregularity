from pathlib import Path
import matplotlib.pyplot as plt

from pylib import (
    sigma, sigma_t, sigmaRatio, sigmaArgmax,
    powerAproximation, degreeContinuoutyIndex,
    
    randomConnectedEdges,
    randomConnectedGraph,
    randomTree,
    randomSigmaOptAprox,
    
    maxSigmaRatio_annealing,

    localBasicNeighbor, globalBasicNeighbor,
    globalTwoPartNeighbor,
    
    neighborListToNx, nxToNeighborList,
    simplePlot, simpleWriteG6, simpleReadG6, simpleSubplot
)

nsim_global, nsim_local = 400, 100
nrange = range(25, 60, 5)
sigma_growth = []
for i in nrange:
    ropt, gopt = 0, None
    for _ in range(100):
        startedges = i * (i - 1) // 2
        g, rg = maxSigmaRatio_annealing(
            i, startedges, nsim_global + i // 2,
            globalTwoPartNeighbor
        )
        g, r = maxSigmaRatio_annealing(
            i, startedges, nsim_local,
            localBasicNeighbor
        )
        if r >= ropt:
            ropt = r
            gopt = g
    simplePlot(gopt, path=f'riste/graph_{i}')
    sigma_growth.append(ropt)
    print(i, ropt)

with open('riste_shit.txt', 'a') as riste:
    riste.writelines(list(map(str, sigma_growth)))
