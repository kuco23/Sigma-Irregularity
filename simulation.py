from random import randint, random

import networkx as nx
import matplotlib.pyplot as plt

from pylib import (
    sigma, sigma_t, sigmaRatio,
    nonEdges, nonBridges,
    
    randomConnectedEdges,
    randomConnectedGraph,
    randomTree,
    randomSigmaOptAprox,
    
    maxSigmaRatio_annealing_modified,

    removeEdges, addEdges,
    localBasicNeighbor, globalBasicNeighbor,
    globalTwoPartNeighbor,
    
    neighborListToNx, nxToNeighborList,
    simplePlot
)

ascende = []
s, t, nsim = 7, 200, 200
for i in range(s, t+1):
    startedges = i * (i - 1) // 2
    g, r = maxSigmaRatio_annealing_modified(
        i, startedges, nsim,
        localBasicNeighbor,
        globalTwoPartNeighbor
    )
    simplePlot(
        neighborListToNx(g),
        f'_opts/img{i}_{round(r)}.png'
    )
    ascende.append((i, r))
    print(i, r)

plt.plot(*zip(*ascende))
plt.show()
