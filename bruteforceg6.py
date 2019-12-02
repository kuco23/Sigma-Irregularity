from operator import add
from pathlib import Path
import networkx as nx
from pylib import sigmaRatio_nx

files = Path().cwd() / 'g6data'
pairs = []
for file in files.iterdir():
    if file.suffix != '.g6': continue
    Gn = nx.read_graph6(file)
    pair = [0,0]
    for G in Gn:
        r = sigmaRatio_nx(G)
        if r > pair[0]:
            pair = [r, G]
    pairs.append(pair)
