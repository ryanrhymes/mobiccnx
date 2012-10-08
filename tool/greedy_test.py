#!/usr/bin/env python
# 
# This script tests the functions in GreedyEmbedding. It also shows
# how to calculate the distance of any two points in Poincare disk.
#
# Reference: 
# R. Kleinberg - Geographic routing using hyperbolic space
# A. Cvetkovski - Hyperbolic Embedding and Routing for Dynamic Graphs
#
# Liang Wang @ Dept. of Computer Science, Univ. of Helsinki, Finland
# 2012.10.07 created
#

import re
import os
import sys
import cmath
import itertools

from greedy_embedding import GreedyEmbedding

def test_every_two_nodes(mapping, greed):
    """Go through all the node pairs, and calculate the distance."""
    for x, y in itertools.combinations(sorted(mapping.keys()), 2):
        print x, y, ":", greed.distance(mapping[x]['c'], mapping[y]['c'])
    pass

def test_greedy_property(mapping, greed, graph):
    """Test if the embedding is a valid greedy embedding. Namely,
    given any destination, one node always has a neighbor who is
    closer to the destination than him."""
    for m in sorted(mapping.keys()):
        found_0 = True
        cm = mapping[m]['c']
        for n in sorted(mapping.keys()):
            if m == n:
                continue
            found_1 = False
            cn = mapping[n]['c']
            dm = greed.distance(cm, cn)
            for p in greed.neighbors(m, graph):
                cp = mapping[p]['c']
                dp = greed.distance(cp, cn)
                if dp < dm:
                    found_1 = True
                    break
            if not found_1:
                found_0 = False
                break
        if found_0:
            print m, "\t...... OK"
        else:
            print m, "\t...... ERROR"
    pass

if __name__=="__main__":
    graph_file = sys.argv[1]
    greed = GreedyEmbedding()
    vertex, edge = greed.load_graph(graph_file)
    kmst = greed.kruskal_mst(vertex, edge)
    mapping = greed.embed(kmst)

    # The first test
    print "\n" + "="*50
    print "Print out the distance of all node pairs\n"
    test_every_two_nodes(mapping, greed)

    # The second test
    print "\n" + "="*50
    print "Test the greedy embedding validity\n"
    test_greedy_property(mapping, greed, edge)

    sys.exit(0)
