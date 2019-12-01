from pathlib import Path
import matplotlib.pyplot as plt

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
    simplePlot, simpleWriteG6, simpleReadG6
)

nsim_global, nsim_local = 200, 20
nrange = range(3, 20)
index, ascende, opts = [], [], []
for i in nrange:
    startedges = i * (i - 1) // 2
    g, rg = maxSigmaRatio_annealing(
        i, startedges, nsim_global,
        globalTwoPartNeighbor
    )
    g, r = maxSigmaRatio_annealing(
        i, startedges, nsim_local,
        localBasicNeighbor
    )
    if i == 10: simplePlot(g)
    opts.append(g)
    ascende.append(r)
    print(i, r)

fig, ax = plt.subplots(figsize=(10, 5))
ax.set_title('Sigma Irregularity')
ax.set_xlabel('Number Of Nodes')
ax.set_ylabel('Sigma Ratio')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

_, c, p = powerAproximation(ascende, 0, 4, 1000, nrange)
ax.plot(nrange, ascende, 'r')
ax.plot(nrange, list(map(lambda n: c * pow(n, p), nrange)), 'g')
plt.show()
