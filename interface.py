from random import randint, random

import networkx as nx
import matplotlib.pyplot as plt

from pylib import (
    sigma, sigma_t, sigmaRatio,
    nonEdges, nonBridges,
    randomConnectedEdges,
    randomConnectedGraph,
    randomSigmaOptAprox,
    maxSigmaRatio_annealing,

    removeEdges,
    addEdges,
    globalNeighbor,
    annealingNeighbor,

    neighborListToNx,
    nxToNeighborList,
    simplePlot
)

order, nsim = 7, 400
startedges = order * (order - 1) // 2

ascende = []
for i in range(10,100):
    startedges = i * (i - 1) // 2
    g, r = maxSigmaRatio_annealing(
        i, startedges, nsim, 
        annealingNeighbor
    )
    ascende.append((i, r))
    print(i, r)

plt.plot(*zip(*ascende))
plt.show()