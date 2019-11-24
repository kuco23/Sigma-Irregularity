from math import inf
import heapq as hp
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


def sigmaArgmax(G, lim):
    nodes = [(-1, -1)]
    for u, line in enumerate(G):
        for v in line:
            du, dv = map(len, (G[u], G[v]))
            aprox = abs(du - dv)
            if aprox > hp.nsmallest(1, nodes)[0][0]:
                hp.heappush(
                    nodes,
                    (aprox, (min(u, v)), max(u, v))
                )
                if len(nodes) > lim:
                    hp.heappop(nodes)
    if hp.nsmallest(1, nodes)[0][0] == -1:
        hp.heappop(nodes)
    return nodes


def degreeContinuoutyIndex(G):
    sm = 0
    for u, line in enumerate(G):
        for v in line:
            du, dv = map(len, (G[u], G[v]))
            aprox = abs(du - dv)
            if aprox > 1: sm += 1
    return sm
