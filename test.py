from pylib import (
    randomConnectedGraph,
    randomPath,
    
    removeEdges, addEdges,
    
    localNeighbor,
    globalNeighbor,

    maxSigmaRatio_annealing_modified,
    maxSigmaRatio_bruteforce,

    simplePlot,
    neighborListToNx,
)


g, r = maxSigmaRatio_annealing_modified(
    9, 30, 100, localNeighbor, globalNeighbor
)

'''
G = randomPath(10)
i = 0
while True:
    i = (i + 1) % 10
    edges = nearDegree(G, i, 2)
    addEdges(G, edges)
    simplePlot(neighborListToNx(G))
'''

G, r = maxSigmaRatio_annealing_modified(40, 100, 2000, localNeighbor, globalNeighbor)
G_nx = neighborListToNx(G)
simplePlot(G_nx)
