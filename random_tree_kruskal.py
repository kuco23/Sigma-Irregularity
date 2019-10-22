from operator import eq
from random import choice, randint
import networkx as nx
import numpy as np

def randomTree_kruskal(n):
    parent = list(range(n))
    graph = nx.Graph()
    graph.add_nodes_from(range(n))

    def getParent(i):
        to_rewire = []
        while parent[i] != i:
            i = parent[i]
            to_rewire.append(i)
        for k in to_rewire:
            parent[k] = i
        return i

    def joinComponents(comp0, comp1):
        parent[comp0] = comp1

    ids = []
    for i in range(n):
        for j in range(i):
            ids.append(i * n + j)
    np.random.shuffle(ids)

    i, nedges = 0, 0
    while nedges < n - 1:
        nodes = (ids[i] // n, ids[i] % n)
        comps = tuple(map(getParent, nodes))
        if not eq(*comps):
            graph.add_edge(*nodes)
            joinComponents(*comps)
            nedges += 1
        i += 1

    return graph

def randomTree_simple(n):
    nodes = list(range(n))
    np.random.shuffle(nodes)

    graph = nx.Graph()
    graph.add_nodes_from(nodes)
    for i in range(1, n):
        j = nodes[i]
        k = nodes[randint(0, i-1)]
        graph.add_edge(j, k)

    return graph

def simpleDraw(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(
        G, pos, node_size=1,
        node_color='red'
    )
    nx.draw_networkx_edges(G, pos)
    plt.show()   
            
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from timeit import timeit

    g = randomTree_simple(100)
    simpleDraw(g)
