from math import log, exp
from random import randint, random
from itertools import combinations, product

import matplotlib.pyplot as plt
import networkx as nx

from ._neighbor import bridges_bfs, nonedges_bfs
from ._random_graphs import (
    randomConnectedGraph_kruskal_generator
)

def sigma(G):
    sm = 0
    for u, v in G.edges():
        d_u, d_v = map(G.degree, (u, v))
        sm += pow(d_u - d_v, 2)
    return sm

def sigma_t(G):
    sm = 0
    for u, v in combinations(G.nodes(), 2):
        d_u, d_v = map(G.degree, (u, v))
        sm += pow(d_u - d_v, 2)
    return sm

def sigmaRatio(G):
    sG, stG = sigma(G), sigma_t(G)
    return stG / sG if sG > 0 else 0
        
def maxSigmaRatio_bruteforce(n):
    """
    Tests all the possible (including isomorphic)
    graphs on n vertices and returns the 
    pair (sG, G) at which the maximum of the 
    irregularity-ratio is reached

    :params
        int n (graph vertices number)
    """
    nodes = list(range(n))
    alledges = list(combinations(nodes, 2))
    max_pair = None, 0
    for m in range(n):
        for edges in combinations(alledges, m):
            G = nx.Graph()
            G.add_nodes_from(nodes)
            G.add_edges_from(edges)

            rG = sigmaRatio(G)
            if rG > max_pair[1]:
                max_pair = G, rG
    
    return max_pair

def newState(G):
    node = randint(0, len(G) - 1)
    remove = bridges_bfs(G, node, 1)
    add = nonedges_bfs(G, node, 5)
    opt_ratio, opt_edge_alt = 0, (None, None)

    def edgeAlter(edge_add, edge_rem):
        if edge_add is not None:
            G.add_edge(*edge_add)
        if edge_rem is not None:
            G.remove_edge(*edge_rem)

    def testEdgeReplacement(edge_add, edge_rem):
        edgeAlter(edge_add, edge_rem)
        r = sigmaRatio(G)
        edgeAlter(edge_rem, edge_add)
        return r

    for aedge, redge in product(
        add + [None], remove + [None]
    ):
        r = testEdgeReplacement(aedge, redge)
        if opt_ratio < r:
            opt_ratio = r
            opt_edge_alt = (aedge, redge)

    edgeAlter(*opt_edge_alt)


def randomConnectedGraph(n, m):
    g = nx.Graph()
    g.add_nodes_from(range(n))
    gen = randomConnectedGraph_kruskal_generator(n, m)
    for u, v in gen: g.add_edge(u, v)
    return g
    
def maxSigmaRatio_annealing(n, nsim, temperature=1):
    """
    implements the simulated annealing
    algorithm
    
    :params -- positional
        int n
            graph vertices number
        int nsim
            number of randomly
            tested graphs
            
    :params -- keyworded
        float temperature
            starting temperature
    """
    m_total = n * (n - 1) // 2
    
    prob = lambda ci, cr, t: exp((ci - cr) / t)
    temp = lambda i: temperature / log(i)
    rand_graph = lambda m=0: nx.gnm_random_graph(
        n, m or randint(1, m_total)
    )
    
    curi = randomConnectedGraph(
        n, randint(0, m_total)
    )
    sri = sigmaRatio(curi)
    bes = (curi.copy(), sri)
    cur = (curi.copy(), sri)

    for i in range(2, nsim + 2):
        print(bes[1])
        t = temp(i)
        newState(curi)
        sri = sigmaRatio(curi)

        if sri >= cur[1]:
            cur = (curi.copy(), sri)
            if sri > bes[1]:
                bes = (curi.copy(), sri)

        elif prob(sri, cur[1], t) > random():
            cur = (curi.copy(), sri)

    return bes
    
