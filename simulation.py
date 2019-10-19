from math import e, log
from random import randint, choice, random, sample
from itertools import combinations, product

import matplotlib.pyplot as plt
from numpy.random import shuffle
import networkx as nx

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
    return stG / sG if sG > 0 else 1
        
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
    max_pair = 0, None
    for m in range(n):
        for edges in combinations(alledges, m):
            G = nx.Graph()
            G.add_nodes_from(nodes)
            G.add_edges_from(edges)

            rG = sigmaRatio(G)
            if rG > max_pair[0]:
                max_pair = rG, G
    
    return max_pair

def disturbGraph(G):
    n = len(G)
    nodes = list(range(n))
    edges = list(G.edges())

    def addRandomEdge():
        for e in filter(
            lambda uv: uv[0] != uv[1],
            product(
                sample(nodes, n),
                sample(nodes, n)
            )
        ):
            if not G.has_edge(*e):
                G.add_edge(*e)
                break

    def removeRandomEdge():
        rem_edge = choice(edges)
        G.remove_edge(*rem_edge)

    voidFun = lambda: 0
    if len(edges) == n * (n - 1) // 2:
        addRandomEdge = voidFun
    elif len(edges) == 0:
        removeRandomEdge = voidFun

    choice([
        removeRandomEdge,
        addRandomEdge,
        lambda: (
            removeRandomEdge(),
            addRandomEdge()
        )
    ])()

def maxSigmaRatio_annealing(n, nsim, temperature=None):
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
        function temperature
            decreasing function
            describing the temperature
            lowering process
    """
    temperature = temperature or (lambda i: 1 / log(i))
    prob = lambda ci, cr, t: pow(e, (cr - ci) / t)
    
    _t = nx.gnm_random_graph(n, randint(1, n))
    bes = (_t, sigmaRatio(_t))
    cur = (_t.copy(), bes[1])
    curi = _t.copy()

    for i in range(2, nsim + 2):
        t = temperature(i)
        disturbGraph(curi)
        sri = sigmaRatio(curi)

        if sri >= cur[1]:
            cur = (curi.copy(), sri)
            if sri >= bes[1]:
                bes = (curi.copy(), sri)

        elif prob(sri, cur[1], t) > random():
            cur = (curi.copy(), sri)

    return bes
    

def simpleDraw(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos, node_list = G.edges(), edge_color='r')
    plt.show()


if __name__ == '__main__':
    g, r = maxSigmaRatio_annealing(10, 100)
    simpleDraw(g)
