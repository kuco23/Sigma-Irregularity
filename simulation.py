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
    localNeighbor, globalNeighbor,
    
    neighborListToNx, nxToNeighborList,
    simplePlot
)

<<<<<<< HEAD:interface.py
s, t, nsim = 2, 50, 400
=======
ascende = []
s, t, nsim = 3, 200, 100
>>>>>>> 8d4ede8fd58263a1bb8278f9329cb42fdae15cce:simulation.py
for i in range(s, t+1):
    startedges = i * (i - 1) // 2
    g, r = maxSigmaRatio_annealing_modified(
        i, startedges, nsim,
        localNeighbor,
        globalNeighbor
    )
    # simplePlot(neighborListToNx(g))
    ascende.append((i, r))
    print(i, r)

plt.plot(*zip(*ascende))
plt.show()
