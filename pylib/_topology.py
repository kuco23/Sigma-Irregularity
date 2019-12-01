from math import ceil
from random import randint, randrange, random, choice

from ._base_defs import sigmaRatio, sigmaArgmax, sigmaUpdate
from ._random_extension import randomPermutations
from ._random_graphs import (
    randomSigmaOptAprox,
    randomPath,
    randomConnectedGraph
)
from ._edge_tools import (
    removeEdges, addEdges,
    nonBridges, nonEdges
)

def _chooseSources(G):
    return sorted(
        sigmaArgmax(G),
        key=lambda i: len(G[i])
    )

def localBasicNeighbor(G):
    n, m = len(G), sum(map(len, G)) // 2
    m_total = n * (n - 1) // 2
    asource, rsource = _chooseSources(G)

    k = randrange(0, 11)
    nadd = m_total - m if m + k > m_total else k
    nrem = 0 if m - k < n - 1 else 10 - k
    to_add = nonEdges(G, asource, nadd) if nadd else []
    to_rem = nonBridges(G, rsource, nrem) if nrem else []
    
    sigma_opt = 0
    for e in to_add:
        addEdges(G, [e])
        diff = sigmaUpdate(G, e, True)
        if diff > 0: removeEdges(G, [e])
        
    for e in to_rem:
        removeEdges(G, [e])
        diff = sigmaUpdate(G, e, False)
        if diff > 0: addEdges(G, [e])
    
    return sigmaRatio(G)

def globalBasicNeighbor(G):
    n, m = len(G), sum(map(len,G)) // 2
    m_max = n * (n - 1) // 2
    G[:] = randomConnectedGraph(
        n, randint(
            max(m-3, n-1),
            min(m+3, m_max)
    ))
    return sigmaRatio(G)

def globalTwoPartNeighbor(G):
    n, m = len(G), sum(map(len, G))
    l = max(map(len, map(lambda u: G[u], sigmaArgmax(G))))
    nsplit = round(l + 0.1 * randint(-1, 1) * n / 10)
    if not 0 < nsplit < n: nsplit = n // 2
    G[:] = randomSigmaOptAprox(
        n, nsplit, 0.01 * randrange(0, 25)
    )
    return sigmaRatio(G)
