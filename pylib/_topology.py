from math import ceil
from random import randint, random

from ._base_defs import sigmaRatio
from ._random_extension import randomPermutations
from ._random_graphs import randomSigmaOptAprox
from ._edge_tools import (
    removeEdges, addEdges,
    nonBridges, nonEdges
)

def localNeighbor(G, lim):
    n, m, lim = len(G), sum(map(len, G)), ceil(lim)+1
    m_total = n * (n - 1) // 2
    source = randint(0, n - 1)

    def testSwitch(r, a):
        removed, added = [], []
        
        if m >= n:
            nremove = min(r, m - (n - 1))
            remove = nonBridges(G, source, nremove)
            removeEdges(G, remove)
            
        if m < m_total:
            nadd = min(a, m_total - m)
            add = nonEdges(G, source, nadd)
            addEdges(G, add)
            
        sigma = sigmaRatio(G)
        addEdges(G, removed)
        removeEdges(G, added)
        return sigma, removed, added

    perms = randomPermutations(
        range(lim), reversed(range(lim))
    )

    sigma_opt, rem_opt, add_opt = 0, [], []
    for _, (r, a) in zip(range(lim), perms):
        if not (r or a): continue
        sigma, *diff = testSwitch(r, a)
        if sigma > sigma_opt:
            rem_opt, add_opt = diff
            sigma_opt = sigma

    addEdges(G, rem_opt)
    removeEdges(G, add_opt)
    return sigma_opt


def globalNeighbor(G, temp):
    n, m = len(G), sum(map(len, G))
    diff = ceil(5 * temp)
    m += randint(-diff, diff)
    G[:] = randomSigmaOptAprox(n, m)
    

def nodeDegreeDiffNeighbor(G, temp):
    NotImplemented

