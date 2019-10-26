from math import log, exp
from random import randint, random, choice
from itertools import combinations, product

import matplotlib.pyplot as plt
import networkx as nx

from ._base_defs import sigmaRatio
from ._edge_selection import bridges_bfs, nonedges_bfs
from ._random_graphs import (
    randomConnectedGraph_kruskal_generator
)

def randomConnectedGraph(n, m):
    g = nx.Graph()
    g.add_nodes_from(range(n))
    gen = randomConnectedGraph_kruskal_generator(n, m)
    for u, v in gen: g.add_edge(u, v)
    return g

def newState(G):
    node = randint(0, len(G) - 1)
    
    remove = bridges_bfs(G, node, 2)
    add = nonedges_bfs(G, node, 2)

    def testRemoval(edge):
        G.remove_edge(*edge)
        r = sigmaRatio(G)
        G.add_edge(*edge)
        return r

    def testAddition(edge):
        G.add_edge(*edge)
        r = sigmaRatio(G)
        G.remove_edge(*edge)
        return r

    opt_rem = max(((testRemoval(e), e) for e in remove), default=(-1,0))
    opt_add = max(((testAddition(e), e) for e in add), default=(-1,0))

    if opt_rem >= opt_add:
        G.remove_edge(*opt_rem[1])
    else:
        G.add_edge(*opt_rem[1])
    
def maxSigmaRatio_annealing(
    n, nsim, temperature=1, alterState=newState
):
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
        :params -- keyworded
        function temperature
            starting temperature
        function alterState
            function altering its
            argument to produce
            graph's neighbor
    """
    m_total = n * (n - 1) // 2
    
    prob = lambda ci, cr, t: exp((ci - cr) / t)
    temp = lambda i: temperature / log(i)
    rand_graph = lambda: nx.gnm_random_graph(
        n, randint(n, m_total)
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
        alterState(curi)
        sri = sigmaRatio(curi)

        if sri >= cur[1]:
            cur = (curi.copy(), sri)
            if sri > bes[1]:
                bes = (curi.copy(), sri)

        elif prob(sri, cur[1], t) > random():
            cur = (curi.copy(), sri)

    return bes
    
