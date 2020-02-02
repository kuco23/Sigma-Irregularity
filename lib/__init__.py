"""
Support for the Simulated Annealing implementation.
All graphs should be represented as neighbor lists.
Conversions to networkx.Graph object should be
done outside the library, so that it has no dependencies.
"""

from ._base_defs import *
from ._random_graphs import *
from ._topology import *
from ._simulated_annealing import *
from ._networkx_extension import *
from ._largest_squares import *
