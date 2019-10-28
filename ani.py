import matplotlib.pyplot as plt
import matplotlib.animation
import networkx as nx

from random import randint, choice

from pylib import *

fig, ax = plt.subplots(figsize=(6,4))

G = nx_randomConnectedGraph(30, 200)
pos = nx.spring_layout(G)

def update(num):
    ax.clear()

    G = nx_randomConnectedGraph(30, randint(30, 200))
    pos = nx.spring_layout(G)
    nx.draw_networkx_edges(G, pos=pos, alpha=0.5)
    nx.draw_networkx_nodes(G, pos=pos, node_size=7)

    ax.set_xticks([])
    ax.set_yticks([])

ani = matplotlib.animation.FuncAnimation(
    fig, update, frames=6, interval=100,
    repeat = True
)
plt.show()
