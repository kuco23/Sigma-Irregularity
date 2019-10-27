from collections import deque

def nonbridges_bfs(G, s, lim):
    nonbridges = set()
    parent = [None] * len(G)
    marked = [False] * len(G)
    marked[s] = True
    queue = deque([s])
    while queue:
        u = queue.popleft()
        for v in G[u]:
            if marked[v] and parent[u] != v:
                nonbridges.add((u, v))
                if len(nonbridges) >= lim:
                    return nonbridges
            elif not marked[v]:
                marked[v] = True
                parent[v] = u
                queue.append(v)
    return nonbridges

def nonedges_bfs(G, s, lim):
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
        for w in filter(lambda i: i != u, range(len(G))):
            if not connected[w]:
                added_edges.add((u, w))
                if len(added_edges) >= lim:
                    return added_edges
            else: connected[w] = False
    return added_edges
