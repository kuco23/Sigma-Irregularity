from itertools import combinations
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
