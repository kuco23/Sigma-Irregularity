from itertools import combinations

def sigma(G):
    sm = 0
    for u in range(len(G)):
        for v in G[u]:
            d_u, d_v = map(len, (G[u], G[v]))
            sm += pow(d_u - d_v, 2)
    return sm // 2

def sigma_t(G):
    sm = 0
    for u, v in combinations(range(len(G)), 2):
        d_u, d_v = map(len, (G[u], G[v]))
        sm += pow(d_u - d_v, 2)
    return sm

def sigmaRatio(G):
    sG, stG = sigma(G), sigma_t(G)
    return stG / sG if sG > 0 else 0

