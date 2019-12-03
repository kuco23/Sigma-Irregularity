from pathlib import Path
import matplotlib.pyplot as plt

'''
from pylib import (
    sigma, sigma_t, sigmaRatio, sigmaArgmax,
    powerAproximation, degreeContinuoutyIndex,
    
    randomConnectedEdges,
    randomConnectedGraph,
    randomTree,
    randomSigmaOptAprox,
    
    maxSigmaRatio_annealing,

    localBasicNeighbor, globalBasicNeighbor,
    globalTwoPartNeighbor,
    
    neighborListToNx, nxToNeighborList,
    simplePlot, simpleWriteG6, simpleReadG6, simpleSubplot
)

nsim_global, nsim_local = 50, 30
nrange = range(3, 8)
index, ascende, opts = [], [], []
for i in nrange:
    startedges = i * (i - 1) // 2
    g, rg = maxSigmaRatio_annealing(
        i, startedges, nsim_global + i // 2,
        globalTwoPartNeighbor
    )
    g, r = maxSigmaRatio_annealing(
        i, startedges, nsim_local,
        localBasicNeighbor
    )
    opts.append(neighborListToNx(g))
    ascende.append(r)
    print(i, r)
'''

def setAxDefaults(ax, title, xlab, ylab):
    ax.set_title(title)
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
    
import json
with open('test_results/degree_diff_500.json', 'r') as file:
    diff = json.load(file)

node_range = range(3, 3 + len(diff))
count, deg_sum = list(zip(*diff))

'''
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_title('Sigma Irregularity')
ax.set_xlabel('Number Of Nodes')
ax.set_ylabel('Sigma Ratio')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
'''

from pylib import squares
with open('test_results/degree_distribution_500.json') as file:
    deg_distrib = json.load(file)

mn, mx, avg = list(zip(*deg_distrib))
node_range = range(3, 3 + len(deg_distrib))

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 50))
setAxDefaults(ax1, '', '', 'Minimalna stopnja')
setAxDefaults(ax2, '', '', 'Maksimalna stopnja')
setAxDefaults(ax3, '', '', 'Povpreèna stopnja')

ax1.plot(node_range, mn, 'purple')
ax2.plot(node_range, mx, 'orange')
ax3.plot(node_range, avg, 'red')
plt.show()
