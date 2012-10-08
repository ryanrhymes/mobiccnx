#!/usr/bin/env python
# 
# This script reads in the topology file, then embeds the graph into
# hyperbolic plane. Each node will be allocated a pair of coordinates
# in the two dimensional Poincare disk. The complex number is used to
# represent coordinates.
#
# Usage: appname TOPOLOGY_FILE
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

class GreedyEmbedding(object):
    """Embed a graph into hyperbolic space.
    REMARK: every edge has weight one!"""

    def __init__(self):
        pass

    def load_graph(self, ifn):
        """Load graph from a file"""
        vertex = set()
        edge = set()
        for line in open(ifn, 'r').readlines():
            line = line.strip()
            if line.startswith('#') or len(line) == 0:
                continue

            m = re.search(r"(\S+)\s*->\s*(\S+)\s*", line).groups()
            vr1, vr2 = sorted(m)
            vertex.add(vr1)
            vertex.add(vr2)
            edge.add(tuple(sorted([vr1,vr2])))
        return vertex, edge

    def kruskal_mst(self, vertex, edge):
        """Given the graph, use Kruskal algorithm to calculate
        minimum spanning tree."""
        S = sorted(edge, reverse=True)
        F = dict()
        for x in vertex:
            F[x] = [[x], []]

        while len(S):
            x, y= S.pop()
            sA = [ (k, v[0]) for k, v in F.items() if x in v[0] ][0]
            sB = [ (k, v[0]) for k, v in F.items() if y in v[0] ][0]
            if sA != sB:
                F[sA[0]][0] += F[sB[0]][0]
                F[sA[0]][1] += F[sB[0]][1] + [(x, y)]
                F.pop(sB[0])
        mst = F.values()[0][1]
        return mst

    def max_degree(self, mst):
        """Given a tree, return its degree, and the node with the
        greatest degree."""
        d = dict()
        for x, y in mst:
            d[x] = d.get(x, 0) + 1
            d[y] = d.get(y, 0) + 1
        return sorted([ (v, k) for k, v in d.items() ], reverse=True)[0]

    def neighbors(self, node, graph):
        """Given the node and the graph, return the node's
        neighbors."""
        neighbors = set()
        for x, y in graph:
            if node in (x, y):
                neighbors.add(x)
                neighbors.add(y)
        neighbors.remove(node)
        return sorted(neighbors)

    def embed(self, tree):
        """Given a spanning tree, embed it into two dimensional half
        Poincare plane."""
        degree, root = self.max_degree(tree)
        C = {root:{'c': (0-0j), 'a': cmath.pi, 'b': 2 * cmath.pi}}
        S = [root] # nodes need to be visited
        Z = []     # nodes have been visted
        while len(S):
            pn = S.pop()
            Z.append(pn)
            for n in self.neighbors(pn, tree):
                if n in Z:
                    continue
                S.insert(0, n)
                an = C[pn]['a']
                bn = (an + C[pn]['b']) / 2.0
                C[pn]['a'] = bn
                cp, r2 = self.poincare_circle(cmath.exp(complex(0, an)), 
                                              cmath.exp(complex(0, bn)))
                c = r2 / (C[pn]['c'].conjugate() - cp.conjugate()) + cp
                an = (an + bn) / 2.0
                C[n] = {'c': c, 'a': an, 'b': bn}
        return C

    def poincare_circle(self, a, b):
        """Given two ideal points in a Poincare plane, calculate the
        center and quadratic radius of the Euclidean circle which
        contains this geodesic."""
        m = (a + b) / 2.0
        cp = 1.0 / m.conjugate()
        r2 = 1.0 / abs(m)**2 - 1.0 
        return cp, r2

    def distance(self, c1, c2):
        """Given any two coordinates in two dimensional Poincare disk,
        calculate the distance between them."""
        d = cmath.acosh(2 * abs(c1 - c2)**2 / ((1 - abs(c1)**2) * (1 - abs(c2)**2)) + 1)
        d = abs(d)
        return d

    def output(self, C):
        """Given the node <-> coordinates mapping, output the mapping
        on the screen. The coordinates are complex numbers."""
        for n in sorted(C.keys()):
            #print "%s\t%s\t%f\t%f" % (n, C[n]['c'], C[n]['a'], C[n]['b'])
            print "%s %f %f" % (n, C[n]['c'].real, C[n]['c'].imag)
        pass

    pass

if __name__=="__main__":
    graph_file = sys.argv[1]
    greed = GreedyEmbedding()
    vertex, edge = greed.load_graph(graph_file)
    kmst = greed.kruskal_mst(vertex, edge)
    mapping = greed.embed(kmst)
    greed.output(mapping)

    sys.exit(0)
