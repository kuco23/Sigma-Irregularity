from math import log, exp
from random import randint, random
from itertools import combinations

import matplotlib.pyplot as plt
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

def maxSigmaRatio_annealing(
    n, nsim, starting_edges=0, temperature=1
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
        float temperature
            starting temperature
    """
    m_total = n * (n - 1) // 2
    
    prob = lambda ci, cr, t: exp((ci - cr) / t)
    temp = lambda i: temperature / log(i)
    rand_graph = lambda m=0: nx.gnm_random_graph(
        n, m or randint(1, m_total)
    )
    
    curi = nx.gnm_random_graph(n, starting_edges)
    sri = sigmaRatio(curi)
    bes = (curi.copy(), sri)
    cur = (curi.copy(), sri)

    for i in range(2, nsim + 2):
        t = temp(i)
        curi = rand_graph()
        sri = sigmaRatio(curi)

        if sri >= cur[1]:
            cur = (curi, sri)
            if sri > bes[1]:
                bes = (curi, sri)

        elif prob(sri, cur[1], t) > random():
            cur = (curi, sri)

    return bes
    

def simpleDraw(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(
        G, pos, node_size=5,
        node_color='red'
    )
    nx.draw_networkx_edges(G, pos)
    plt.show()


if __name__ == '__main__':
    g, r = maxSigmaRatio_annealing(30, 10000, temperature=5)
    print(r)
    simpleDraw(g)
