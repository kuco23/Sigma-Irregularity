import networkx as nx
import matplotlib.pyplot as plt

from pylib import *

'''
maxSigmaRatio_annealing(
    nodes, simulation_number,
    temperature = <int>,
    alterState = <function>
)
'''

def simplePlot(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=8)
    nx.draw_networkx_edges(G, pos)
    plt.show()

# funkcija, ki naj bi definirala okolico grafa G
# in G priredila nekega random soseda
# ne vrne nicesar, ampak G spreminja lokalno
def alterState(G):
    ...
    pass

g, r = maxSigmaRatio_annealing(30, 1000, 1000)
print('maximum ratio:', r)
simplePlot(g) # narise graf, ki ga vrne maxSigmaRatio_annealing
