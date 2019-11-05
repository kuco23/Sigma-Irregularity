from copy import deepcopy
from random import randint, random

from ._base_defs import sigmaRatio
from ._edge_selection import nonBridges, nonEdges
from ._random_graphs import randomConnectedGraph

nedges = lambda G: sum(map(len, G)) // 2

def removeEdges(G, edges):
    for u, v in edges:
        G[u].remove(v)
        G[v].remove(u)

def addEdges(G, edges):
    for u, v in edges:
        G[u].append(v)
        G[v].append(u)

def globalNeighbor(G, k):
    GC = deepcopy(G)
    source = randint(0, len(G)-1)
    if random() < 0.5:
        edges = nonBridges(G, source, k)
        removeEdges(GC, edges)
    else:
        edges = nonEdges(G, source, k)
        addEdges(edges)
    return GC
    
def bestLocalNeighbor(G, k):
    return NotImplemented

def VNS(n, k_max):
    m_total = n * (n - 1) // 2

    def VNLS(x, xr):
        k, b = 1, False
        while k < k_max:
            y, yr = bestLocalNeighbor(G, k)
            if yr >= xr:
                x, xr = y, yr
                b = True
            k = k + 1
            if k == k_max and b: k = 1
        return x, xr
    
    while condition_not_met:
        k = 1
        m = randint(n-1, m_total)
        x = randomConnectedGraph(n, m)
        xr = sigmaRatio(G)
        while k < k_max:
            x = neighborhood(x, k)
            y, yr = VLNS(x, xr)
            if yr >= xr:
                x, xr = y, yr
                k = 1
            else: k += 1
            
    return x
        
            
