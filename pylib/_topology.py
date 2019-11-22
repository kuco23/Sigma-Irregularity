from math import ceil
from random import randint, random, choice

from ._base_defs import sigmaRatio
from ._random_extension import randomPermutations
from ._random_graphs import randomSigmaOptAprox, randomPath
from ._edge_tools import (
    removeEdges, addEdges,
    nonBridges, nonEdges
)

def _nodeWithLargestSigma(G):
    smax, nmax = -1, -1
    for u, line in enumerate(G):
        for v in line:
            aprox = abs(len(G[u]) - len(G[v]))
            if aprox > smax:
                smax, nmax = aprox, (u, v)
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


def globalNeighbor(G, temp):
    n, m = len(G), sum(map(len, G))
    diff = ceil(5 * temp)
    m += randint(-diff, diff)
    G[:] = randomSigmaOptAprox(n, m)
    return sigmaRatio(G)

