from random import randint, random

import networkx as nx
import matplotlib.pyplot as plt

from pylib import (
    sigma, sigma_t, sigmaRatio,
    nonEdges, nonBridges,
    randomConnectedEdges,
    randomConnectedGraph,
    randomSigmaOptAprox,
    maxSigmaRatio_annealing_modified,

    removeEdges,
    addEdges,
    localNeighbor,
    globalNeighbor,

    neighborListToNx,
    nxToNeighborList,
    simplePlot
)

ascende = []
s, t, nsim = 3, 200, 100
for i in range(s, t+1):
    startedges = i * (i - 1) // 2
    g, r = maxSigmaRatio_annealing_modified(
        i, startedges, nsim, 
        localNeighbor,
        globalNeighbor
    )
    ascende.append((i, r))
    print(i, r)

plt.plot(*zip(*ascende))
plt.show()
