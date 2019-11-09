import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation

def sigma_nx(G):
    sm = 0
    for u, v in G.edges():
        d_u, d_v = map(G.degree, (u, v))
        sm += pow(d_u - d_v, 2)
    return sm

def sigma_t_nx(G):
    sm = 0
    for u, v in combinations(G.nodes(), 2):
        d_u, d_v = map(G.degree, (u, v))
        sm += pow(d_u - d_v, 2)
    return sm

def sigmaRatio_nx(G):
    sG, stG = sigma_nx(G), sigma_t_nx(G)
    return stG / sG if sG > 0 else 1

def neighborListToNx(G):
    nx_G = nx.Graph()
    nx_G.add_nodes_from(range(len(G)))
    for u in range(len(G)):
        for v in G[u]:
            nx_G.add_edge(u, v)
    return nx_G

def nxToNeighborList(G):
    return map(
        lambda n: nx.neighbors(G, n),
        G.nodes()
    )

def simplePlot(G):
    G = neighborListToNx(G)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=5)
    nx.draw_networkx_edges(G, pos)
    plt.show()
