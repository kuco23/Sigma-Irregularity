from math import ceil
from itertools import combinations

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation

def nxConversion(fun):
    def wrapper(G, *args, **kwargs):
        if isinstance(G, list):
            G = neighborListToNx(G)
        return fun(G, *args, **kwargs)
    return wrapper

def sigma_nx(G):
    sm = 0
    for u, v in G.edges():
        d_u, d_v = map(G.degree, (u, v))
        sm += pow(d_u - d_v, 2)
    return sm

def sigma_t_nx(G):
    sm = 0
    for u, v in combinations(G.nodes(), 2):
        d_u, d_v = map(G.degree, (u, v))
        sm += pow(d_u - d_v, 2)
    return sm

def sigmaRatio_nx(G):
    sG, stG = sigma_nx(G), sigma_t_nx(G)
    return stG / sG if sG > 0 else 1

def neighborListToNx(G):
    nx_G = nx.Graph()
    nx_G.add_nodes_from(range(len(G)))
    for u in range(len(G)):
        for v in G[u]:
            nx_G.add_edge(u, v)
    return nx_G

def nxToNeighborList(G):
    return map(
        lambda n: nx.neighbors(G, n),
        G.nodes()
    )

@nxConversion
def simplePlot(G, path=None):
    fig, ax = plt.subplots(figsize=(20, 10))
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(
        G, pos, alpha=0.8,
        node_size=5, node_color='black'
    )
    nx.draw_networkx_edges(G, pos, alpha=0.4)
    plt.axis('off')
    plt.show() if path is None else (
        plt.savefig(
            path
        ), plt.cla()
    )

def simpleSubplot(Gs : list):
    h, w = ceil(len(Gs) / 3), 3
    sp = int(f'{h}{w}1')
    fig, ax = plt.subplots(figsize=(20, 5 * h))
    for G in Gs:
        pos = nx.spring_layout(G)
        plt.subplot(sp)
        plt.axis('off')
        nx.draw_networkx_nodes(
            G, pos, alpha=0.5,
            node_size=5, node_color='black',
            linewidths=2.0
        )
        nx.draw_networkx_edges(G, pos, alpha=0.5, width=1.5)
        sp += 1
    plt.show()

@nxConversion
def simpleWriteG6(G, path, **kwargs):
    nx.write_graph6(G, path, **kwargs)

def simpleReadG6(path):
    return nx.read_graph6(path)
