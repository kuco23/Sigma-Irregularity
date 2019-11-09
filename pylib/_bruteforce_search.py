from itertools import combinations

import networkx as nx

from ._networkx_extension import sigmaRatio_nx



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

            rG = sigmaRatio_nx(G) 
            if (
                (rG > max_pair[1] and nx.is_connected(G)) or
                (not max_pair[0] and nx.is_connected(G))
            ):
                max_pair = G, rG
    
    return max_pair
