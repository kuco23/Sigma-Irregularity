from types import SimpleNamespace
from collections import deque
from random import sample

nedges = lambda G: sum(map(len, G)) // 2

def removeEdges(G, edges):
    for u, v in edges:
        G[u].remove(v)
        G[v].remove(u)

def addEdges(G, edges):
    for u, v in edges:
        G[u].append(v)
        G[v].append(u)

def bfs(G, s, fun, data):
    marked = [False] * len(G)
    marked[s] = True
    queue = deque([s])
    while queue:
        u = queue.popleft()
        for v in G[u]:
            fun(u, v, marked)
            if data.sentinel: return
            if not marked[v]:
                marked[v] = True
                queue.append(v)

def nonBridges(G, s, lim):
    data = SimpleNamespace(
        sentinel=False,
        edges=set(),
        parent = [None] * len(G)
    )
    
    def fun(u, v, marked):
        if marked[v] and data.parent[u] != v:
            data.edges.add((min(u,v), max(u,v)))
            if len(data.edges) >= lim:
                data.sentinel = True
        elif not marked[v]:
            data.parent[v] = u

    bfs(G, s, fun, data)
    return data.edges

def nonEdgesCoro(G, s):
    n = len(G)
    connected = [False] * n
    marked = [False] * n
    marked[s] = True
    queue = deque([s])
    while queue:
        u = queue.popleft()
        for v in G[u]:
            connected[v] = True
            if not marked[v]:
                queue.append(v)
                marked[v] = True
        for w in sample(range(n), n):
            if not connected[w] and w != u:
                yield (min(u,w), max(u,w))
            else: connected[w] = False

def nonEdges(G, s, lim):
    coro = nonEdgesCoro(G, s)
    edges = set()
    for e in coro:
        edges.add(e)
        if len(edges) >= lim:
            break
    return edges
