from random import randint, choice

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation

from pylib import *

n, m, nsim = 40, 300, 1000

fig, ax = plt.subplots(figsize=(6,4))
G = neighborListToNx(randomTree(n))
pos = nx.spring_layout(G)

generator = maxSigmaRatio_annealing(
    n, m, nsim, annealingNeighbor
)

ns = [0]

def update(num):
    try: G = neighborListToNx(next(generator))
    except StopIteration: return print(ns[0])

    ns[0] = sigmaRatio(G)
    ax.clear()
    nx.draw_networkx_edges(G, pos=pos, alpha=0.5)
    nx.draw_networkx_nodes(G, pos=pos, node_size=7)

    ax.set_xticks([])
    ax.set_yticks([])

ani = matplotlib.animation.FuncAnimation(
    fig, update, frames=6, interval=50,
    repeat = True
)
plt.show()
