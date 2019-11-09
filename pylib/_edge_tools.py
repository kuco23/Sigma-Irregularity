from types import SimpleNamespace
from collections import deque

def removeEdges(G, edges):
    for u, v in edges:
        G[u].remove(v)
        G[v].remove(u)

def addEdges(G, edges):
    for u, v in edges:
        G[u].append(v)
        G[v].append(u)

def nonBridges(G, s, lim):
    non_bridges = set()
    parent = [None] * len(G)
    marked = [False] * len(G)
    marked[s] = True
    queue = deque([s])
    while queue:
        u = queue.popleft()
        for v in G[u]:
            if marked[v] and parent[u] != v:
                non_bridges.add((min(u,v), max(u,v)))
                if len(non_bridges) >= lim:
                    return non_bridges
            elif not marked[v]:
                marked[v] = True
                parent[v] = u
                queue.append(v)
    return non_bridges

def nonEdges(G, s, lim):
    added_edges = set()
    connected = [False] * len(G)
    marked = [False] * len(G)
    marked[s] = True
    queue = deque([s])
    while queue and len(added_edges) < lim:
        u = queue.popleft()
        for v in G[u]:
            connected[v] = True
            if not marked[v]:
                queue.append(v)
                marked[v] = True
        for w in range(len(G)):
            if not connected[w] and w != u:
                added_edges.add((min(u,v), max(u,v)))
                if len(added_edges) >= lim:
                    return added_edges
            else: connected[w] = False
    return added_edges
