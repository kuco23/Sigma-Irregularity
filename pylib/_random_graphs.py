from operator import eq
from itertools import combinations
from random import randint
from numpy.random import shuffle

def _randomCombinations(L):
    combs = list(combinations(L, 2))
    shuffle(combs)
    yield from combs

def randomConnectedEdges(n, m):
    edge_iter = _randomCombinations(range(n))
    parent = list(range(n))
    graph = [[] for _ in range(n)]
    chaos_edges = m - (n - 1)

    def getSource(u):
        to_rewire = []
        while parent[u] != u:
            to_rewire.append(u)
            u = parent[u]
        for v in to_rewire:
            parent[v] = u
        return u

    def joinSources(c1, c2):
        parent[c1] = c2

    edges, ccount = [], 0
    for u, v in edge_iter:
        sources = list(map(getSource, (u, v)))
        if not eq(*sources):
            joinSources(*sources)
            ccount += 1
        elif len(edges) >= m: break
        elif len(edges) - ccount >= chaos_edges: continue
        edges.append((u, v))
    
    return edges

def randomConnectedGraph(n, m):
    graph = [[] for _ in range(n)]
    for n1, n2 in randomConnectedEdges(n, m):
        graph[n1].append(n2)
        graph[n2].append(n1)
    return graph

def randomTree(n):
    nodes = list(range(n))
    graph = [[] for _ in nodes]
    shuffle(nodes)
    for i in range(1, n):
        j = nodes[i]
        k = nodes[randint(0, i-1)]
        graph[j].append(k)
        graph[k].append(j)
    return graph
    
