import matplotlib.pyplot as plt
import matplotlib.animation
import networkx as nx

from random import randint, choice

from pylib import *

def neighborListToNx(G):
    nx_G = nx.Graph()
    nx_G.add_nodes_from(range(len(G)))
    for u in range(len(G)):
        for v in G[u]:
            nx_G.add_edge(u, v)
    return nx_G

def nx_randomConnectedGraph(n, m):
    g = randomConnectedGraph(n, m)
    return neighborListToNx(g)

def nx_randomTree(n):
    g = randomTree(n)
    return neighborListToNx(g)

fig, ax = plt.subplots(figsize=(6,4))

G = nx_randomTree(30)
pos = nx.spring_layout(G)

def update(num):
    ax.clear()

    G = nx_randomTree(30)
    nx.draw_networkx_edges(G, pos=pos, alpha=0.5)
    nx.draw_networkx_nodes(G, pos=pos, node_size=7)

    ax.set_xticks([])
    ax.set_yticks([])

ani = matplotlib.animation.FuncAnimation(
    fig, update, frames=6, interval=50,
    repeat = True
)
plt.show()
