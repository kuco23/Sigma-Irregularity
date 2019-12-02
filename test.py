from pylib import (
    randomConnectedGraph,
    randomPath,
    
    removeEdges, addEdges,
    
    localBasicNeighbor,
    globalBasicNeighbor,
    globalTwoPartNeighbor,

    maxSigmaRatio_annealing,

    simplePlot,
    neighborListToNx,
)

g, r = maxSigmaRatio_annealing(
    20, 80, 200, globalTwoPartNeighbor
)

g, r = maxSigmaRatio_annealing(
    20, 80, 200, localBasicNeighbor,
    defaultG = g
)

simplePlot(g)
