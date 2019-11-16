from operator import add

import networkx as nx

files = map(lambda x: f'graph{x}c.g6', range(9,10))

pairs = []
for file in files:
    Gn = nx.read_graph6(file)
    pair = [0,0]
    for G in G8:
        r = sigmaRatio_nx(G)
        if r > pair[0]:
            pair[0] = r
            pair[1] = G
    pairs.append(pair)
