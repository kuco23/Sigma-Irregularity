from operator import eq
from math import ceil, floor
from itertools import combinations
from random import random, randint

from numpy.random import shuffle

from ._random_extension import randomCombinations
from ._edge_tools import addEdges, removeEdges

def randomConnectedEdges(n, m): # O(n^2)
    edge_iter = randomCombinations(range(n))
    parent = list(range(n))
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
        if ccount < n - 1:
            sources = list(map(getSource, (u, v)))
            if not eq(*sources):
                joinSources(*sources)
                ccount += 1
        if len(edges) >= m: break
        if len(edges) - ccount >= chaos_edges: continue
        edges.append((u, v))
    
    return edges

def randomConnectedGraph(n, m):
    graph = [[] for _ in range(n)]
    for n1, n2 in randomConnectedEdges(n, m):
        graph[n1].append(n2)
        graph[n2].append(n1)
    return graph

def randomTree(n): # O(n)
    nodes = list(range(n))
    graph = [[] for _ in nodes]
    shuffle(nodes)
    for i in range(1, n):
        j = nodes[i]
        k = nodes[randint(0, i-1)]
        graph[j].append(k)
        graph[k].append(j)
    return graph

def randomPath(n): # O(n)
    nodes = list(range(n))
    graph = [[] for _ in nodes]
    shuffle(nodes)
    for i in range(n - 1):
        u, v = nodes[i], nodes[i+1]
        graph[u].append(v)
        graph[v].append(u)
    return graph

def randomSubtreeParentList(G): # O(n + m)
    n, edge_counter = len(G), 0
    source = randint(0, n-1)
    marked = [False] * n
    parent = [None] * n
    parent[source] = source
    stack = [source]
    while stack:
        u = stack.pop()
        marked[u] = True
        for v in G[u]:
            if parent[v] is None:
                parent[v] = u
                edge_counter += 1
                if edge_counter == n - 1:
                    return parent
            if not marked[v]:
                stack.append(v)
    raise Exception('Subtree does not exist')

def randomSubtree(G):
    T = [[] for _ in range(len(G))]
    pl = randomSubtreeParentList(G)
    for u, p in enumerate(pl):
        if u != p:
            T[p].append(u)
            T[u].append(p)
    return T

def randomDistributedConnectedGraph(n, p):
    edges = set()
    G = randomTree(n)
    for row in G: row.sort()
    for u in range(n):
        count = 0
        for v in range(u):
            if len(G[u]) > count and v == G[u][count]:
                count += 1
                continue
            if random() < p:
                edges.add((min(u,v), max(u,v)))
    addEdges(G, edges)
    return G

def randomSigmaOptAprox(n, m):
    p = 2 * m / (n * (n - 1))
    nmin, nmax = floor(n / 2), ceil(n / 2)
    G1 = randomDistributedConnectedGraph(nmin, p)
    G2 = randomDistributedConnectedGraph(nmax, 1 - p)
    for row in G2:
        for i in range(len(row)):
            row[i] += nmin
    G1[0].append(nmin)
    G2[0].append(0)
    G1.extend(G2)
    return G1
