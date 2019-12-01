from math import ceil
from random import randint, randrange, random, choice

from ._base_defs import sigmaRatio, sigmaArgmax
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

def _chooseSource(G):
    return sorted(
        sigmaArgmax(G),
        key=lambda i: len(G[i])
    )

def localBasicNeighbor(G, diff):
    n, m = len(G), sum(map(len, G)) // 2
    m_total = n * (n - 1) // 2
    asource, rsource = _chooseSource(G)

    k = randrange(0, 11)
    nadd = m_total - m if m + k > m_total else k
    nrem = 0 if m - k < n - 1 else 10 - k
    to_add = nonEdges(G, asource, nadd) if nadd else []
    to_rem = nonBridges(G, rsource, nrem) if nrem else []
    
    sigma_opt = -1
    for u in to_add:
        addEdges(G, [u])
        r = sigmaRatio(G)
        if r >= sigma_opt: sigma_opt = r
        else: removeEdges(G, [u])
        
    for u in to_rem:
        removeEdges(G, [u])
        r = sigmaRatio(G)
        if r >= sigma_opt: sigma_opt = r
        else: addEdges(G, [u])
    
    return sigma_opt

def globalBasicNeighbor(G, temp):
    n, m = len(G), sum(map(len,G)) // 2
    m_max = n * (n - 1) // 2
    G[:] = randomConnectedGraph(
        n, randint(
            max(m-3, n-1),
            min(m+3, m_max)
    ))
    return sigmaRatio(G)

def globalTwoPartNeighbor(G, temp):
    n, m = len(G), sum(map(len, G))
    l = max(map(len, map(lambda u: G[u], sigmaArgmax(G))))
    nsplit = round(l + 0.1 * randint(-1, 1) * n / 10)
    if not 0 < nsplit < n: nsplit = n // 2
    G[:] = randomSigmaOptAprox(
        n, nsplit, 0.01 * randrange(0, 25)
    )
    return sigmaRatio(G)
