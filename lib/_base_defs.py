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

def sigmaUpdate(G, edge, added):
    sgn = [1, -1][added]
    diff = 0
    s, t = edge
    ds, dt = map(len, (G[s], G[t]))
    G[s].sort(), G[t].sort()
    ns, nt = G[s], G[t]
    i, j = 0, 0
    while i < len(ns) and j < len(nt):
        if i == len(ns): u = -1
        elif j == len(nt): v = -1
        else: u, v = ns[i], ns[j]
        if u <= v:
            i += 1
            du = len(G[u])
            diff += sgn * 2 * (dt - (du + sgn)) + 1
        if v <= u:
            j += 1
            dv = len(G[v])
            diff += sgn * 2 * (ds - (dv + sgn)) + 1
    return diff
        
def sigmaArgmax(G):
    edge, sup = None, -1
    for u, line in enumerate(G):
        for v in line:
            du, dv = map(len, (G[u], G[v]))
            aprox = abs(du - dv)
            if aprox > sup:
                sup = aprox
                edge = (u, v)
    return edge

def degreeContinuoutyIndex(G):
    sm = 0
    for u, line in enumerate(G):
        for v in line:
            du, dv = map(len, (G[u], G[v]))
            aprox = abs(du - dv)
            if aprox > 1: sm += 1
    return sm
