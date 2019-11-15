from pylib import (
    randomConnectedGraph,
    
    removeEdges,
    nonBridges,
    
    localNeighbor,
    globalNeighbor,

    maxSigmaRatio_annealing_modified,

    simplePlot,
    neighborListToNx,
)


g, r = maxSigmaRatio_annealing_modified(
    10, 10, 1000, localNeighbor, globalNeighbor
)

print(r)
nG = neighborListToNx(g)
simplePlot(nG)
