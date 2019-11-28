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
    
    neighborListToNx, nxToNeighborList, simplePlot,
)

nsim_global, nsim_local = 200, 20
nrange = range(3, 50)
index, ascende = [], []
for i in nrange:
    startedges = i * (i - 1) // 2
    g, r = maxSigmaRatio_annealing(
        i, startedges, nsim_global,
        globalTwoPartNeighbor
    )
    g, r = maxSigmaRatio_annealing(
        i, startedges, nsim_local,
        localBasicNeighbor
    )
    index.append(degreeContinuoutyIndex(g))
    ascende.append(r)
    print(i, r)

_, c, p = powerAproximation(ascende, 0, 4, 1000, nrange)
plt.plot(nrange, ascende, 'r')
plt.plot(nrange, list(map(lambda n: c * pow(n, p), nrange)), 'g')
plt.plot(nrange, index, 'b')
plt.show()
