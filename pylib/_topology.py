from math import ceil
from random import randint, random

from ._random_graphs import randomSigmaOptAprox
from ._edge_tools import (
    removeEdges, addEdges,
    nonBridges, nonEdges
)

def globalNeighbor(G, lim):
    n, m = len(G), sum(map(len, G))
    m_total = n * (n - 1) // 2
    source = randint(0, n - 1)
    
    def chooseRemoval(k):
        if m < n: return
        nremove = min(k, m - (n - 1))
        remove = nonBridges(G, source, nremove)
        removeEdges(G, remove)
    
    def chooseAddition(k):
        if m >= m_total: return
        nadd = min(k, m_total - m)
        add = nonEdges(G, source, nadd)
        addEdges(G, add)
    
    k = randint(1, lim)
    if random() < 0.5 and m >= n: 
        chooseRemoval(k)
    elif m < m_total or m >= n: 
        chooseAddition(k)

def annealingNeighbor(G, temp):
    n, m = len(G), sum(map(len, G))
    diff = ceil(5 * temp)
    m += randint(-diff, diff)
    G[:] = randomSigmaOptAprox(n, m)