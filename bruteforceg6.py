from operator import add

import networkx as nx

from pylib import sigmaRatio_nx

files = map(
    lambda x: f'_data/graph{x}c.g6',
    range(5,10)
)

pairs = []
for file in files:
    Gn = nx.read_graph6(file)
    pair = [0,0]
    for G in Gn:
        r = sigmaRatio_nx(G)
        if r > pair[0]:
            pair[0] = r
            pair[1] = G
    pairs.append(pair)