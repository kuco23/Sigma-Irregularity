from random import randint, random

import networkx as nx
import matplotlib.pyplot as plt

from pylib import (
    sigma, sigma_t, sigmaRatio,
    nonEdges, nonBridges,
    randomConnectedEdges,
    randomConnectedGraph,
    maxSigmaRatio_annealing
)

def simplePlot(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=5)
    nx.draw_networkx_edges(G, pos)
    plt.show()

def neighborListToNx(G):
    nx_G = nx.Graph()
    nx_G.add_nodes_from(range(len(G)))
    for u in range(len(G)):
        for v in G[u]:
            nx_G.add_edge(u, v)
    return nx_G

# funkcija, ki naj bi definirala okolico grafa G
# in G priredila nekega random soseda.
# Ne vrne nicesar, ampak G spreminja lokalno
def alterState(G):
    order = len(G)
    nb = nonBridges(G, randint(0, order - 1), 4)
    ne = nonEdges(G, randint(0, order - 1), 4)
    if nb and random() < 0.5:
        e1, e2 = nb.pop()
        G[e1].remove(e2)
        G[e2].remove(e1)
    elif ne:
        e1, e2 = ne.pop()
        G[e1].append(e2)
        G[e2].append(e1)


g, r = maxSigmaRatio_annealing(
    30, 60, 100, 100, alterState
)
print('maximum ratio:', r)

simplePlot(neighborListToNx(g))
