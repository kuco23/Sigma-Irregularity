from math import ceil
from random import randint, random, choice

from ._base_defs import sigmaRatio
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

def _nodeWithLargestSigma(G):
    smax, nmax = -1, -1
    for u, line in enumerate(G):
        for v in line:
            du, dv = map(len, (G[u], G[v]))
            aprox = abs(du - dv)
            if aprox > smax:
                smax = aprox
                nmax = u, v
    return nmax

def _testSwitch(G, source, r, a):
    n, m = len(G), sum(map(len, G))
    m_total = n * (n - 1) // 2
    removed, added = [], []
        
    if m >= n:
        nremove = min(r, m - (n - 1))
        removed = nonBridges(G, source, nremove)
        removeEdges(G, removed)
            
    if m < m_total:
        nadd = min(a, m_total - m)
        added = nonEdges(G, source, nadd)
        addEdges(G, added)
            
    sigma = sigmaRatio(G)
    addEdges(G, removed)
    removeEdges(G, added)
    return sigma, removed, added

def localNeighbor(G, diff):
    n, lim = len(G), ceil(diff) + 1
    source = choice(_nodeWithLargestSigma(G))
    perms = randomPermutations(
        range(lim), reversed(range(lim))
    )

    sigma_opt, rem_opt, add_opt = 0, [], []
    for _, (r, a) in zip(range(lim), perms):
        if not (r or a): continue
        sigma, *diff = _testSwitch(G, source, r, a)
        if sigma > sigma_opt:
            rem_opt, add_opt = diff
            sigma_opt = sigma
    
    addEdges(G, add_opt)
    removeEdges(G, rem_opt)
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
    G[:] = randomSigmaOptAprox(n, 0.1)
    return sigmaRatio(G)

