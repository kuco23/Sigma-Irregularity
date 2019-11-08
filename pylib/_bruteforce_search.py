from itertools import combinations

import networkx as nx

def _sigma(G):
    sm = 0
    for u, v in G.edges():
        d_u, d_v = map(G.degree, (u, v))
        sm += pow(d_u - d_v, 2)
    return sm

def _sigma_t(G):
    sm = 0
    for u, v in combinations(G.nodes(), 2):
        d_u, d_v = map(G.degree, (u, v))
        sm += pow(d_u - d_v, 2)
    return sm

def _sigmaRatio(G):
    sG, stG = _sigma(G), _sigma_t(G)
    return stG / sG if sG > 0 else 1

def maxSigmaRatio_bruteforce(n):
    m_total = n * (n - 1) // 2
    nodes = list(range(n))
    alledges = list(combinations(nodes, 2))
    max_pair = None, 0
    for m in range(m_total):
        for edges in combinations(alledges, m):
            G = nx.Graph()
            G.add_nodes_from(nodes)
            G.add_edges_from(edges)

            rG = _sigmaRatio(G) 
            if (
                (rG > max_pair[1] and nx.is_connected(G)) or
                (not max_pair[0] and nx.is_connected(G))
            ):
                max_pair = G, rG
    
    return max_pair
