from collections import deque

def bridges_bfs(G, s, lim):
    bridges = []
    parent = [None] * len(G)
    marked = [False] * len(G)
    marked[s] = True
    queue = deque([s])
    while queue and len(bridges) < lim:
        u = queue.popleft()
        for v in G[u]:
            if marked[v] and parent[u] != v:
                bridges.append((u, v))
            elif not marked[v]:
                marked[v] = True
                parent[v] = u
                queue.append(v)
    return bridges

def nonedges_bfs(G, s, lim):
    added_edges = []
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
            if not connected[w]:
                added_edges.append((u, w)) 
    return added_edges
