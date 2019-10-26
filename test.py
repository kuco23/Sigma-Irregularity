import networkx as nx

import matplotlib.pyplot as plt

from pylib import *

def simplePlot(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=8)
    nx.draw_networkx_edges(G, pos)
    plt.show()

g, r = maxSigmaRatio_annealing(30, 100, 100)
simplePlot(g)
