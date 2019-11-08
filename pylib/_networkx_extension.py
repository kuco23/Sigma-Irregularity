import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation

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