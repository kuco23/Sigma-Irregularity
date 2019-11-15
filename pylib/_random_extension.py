from itertools import combinations, product
from numpy.random import shuffle

def randomCombinations(L):
    """Keep it small!"""
    combs = list(combinations(L, 2))
    shuffle(combs)
    yield from combs

def randomPermutations(L1, L2):
    """Keep it small!"""
    perms = list(product(L1, L2))
    shuffle(perms)
    yield from perms
    
    
