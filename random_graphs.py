from operator import eq
from itertools import combinations
import numpy as np

def _randomCombinations(L):
    combs = list(combinations(L, 2))
    np.random.shuffle(combs)
    yield from combs

def randomConnectedGraph_kruskal(n, m):
    parent = list(range(n))
    edge_iter = _randomCombinations(parent)
    edges, ccount = [], 0
    chaos_edges = m - (n - 1)

    def getSource(u):
        to_rewire = []
        while parent[u] != u:
            to_rewire.append(u)
            u = parent[u]
        for v in to_rewire:
            parent[v] = u
        return u

    def joinComponents(c1, c2):
        parent[c1] = c2

    for u, v in edge_iter:
        sources = list(map(getSource, (u, v)))
        if not eq(*sources):
            joinComponents(*sources)
            ccount += 1
        elif len(edges) - ccount >= chaos_edges: continue
        elif len(edges) >= m: break
        edges.append((u, v))

    return edges


def randomTree(n):
    nodes = list(range(n))
    edges = []
    shuffle(nodes)
    for i in range(1, n):
        j = nodes[i]
        k = nodes[randint(0, i-1)]
        edges.append((j, k))
    return graph
    
