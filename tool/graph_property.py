#!/usr/bin/env python
# 
# This script reads in the topology file, then calcluate graph
# properties like: average degree, average path length, diameter.
#
# Usage: appname TOPOLOGY_FILE
#
# Liang Wang @ Dept. of Computer Science, Univ. of Helsinki, Finland
# 2012.11.03 created
#

import re
import os
import sys
import mpmath
import itertools

def load_graph(ifn):
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

def neighbors(node, graph):
    """Given the node and the graph, return the node's
    neighbors."""
    neighbors = set()
    for x, y in graph:
        if node in (x, y):
            neighbors.add(x)
            neighbors.add(y)
        neighbors.remove(node)
    return sorted(neighbors)

def diameter(vertex, edge):
    """Calculate the diameter of a graph"""
    pass

def path(m, n, edge):
    """Given """
    pass

def weight(m, n, links):
    """Given two vertices, return the weight of corresponding edge."""
    link = tuple(sorted([m, n]))
    w = 1 if link in links else float("Inf")
    w = 0 if m==n else w
    return w

def floyd_warshall(routers, links):
    """Use Floyd-Warshall algorithm to calculate the shortest path
    between any two nodes."""
    path = {}
    next = {}

    # Initialize
    for i, j in itertools.product(routers, repeat=2):
        path[(i, j)] = weight(i, j, links)

    for k in routers:
        for i in routers:
            for j in routers:
                if path[(i, k)] + path[(k, j)] < path[(i, j)]:
                    path[(i, j)] = path[(i, k)] + path[(k, j)]
                    next[(i, j)] = k
    return path, next

def fw_get_path(i, j, path, next):
    """Reconstruct the shortest path between two nodes, given the
    output from floyd_warshall algorithm."""
    if path[(i, j)]==float('Inf'):
        return None
    if not next.has_key((i, j)):
        return []
    itm = next[(i, j)]
    return fw_get_path(i, itm, path, next) + [itm] + fw_get_path(itm, j, path, next)

def build_pathdict(routers, links):
    """Reconstruct the shortest path between two nodes, given the
    output from floyd_warshall algorithm."""
    pathdict = {}
    routers = sorted(routers)
    path, next = floyd_warshall(routers, links)
    for i, j in itertools.permutations(routers, 2):
        p = fw_get_path(i, j, path, next)
        pathdict[(i, j)] = [i] + p + [j]
    return pathdict

if __name__=="__main__":
    graph_file = sys.argv[1]
    vertex, edge = load_graph(graph_file)
    pathdict = build_pathdict(vertex, edge)

    print pathdict

    sys.exit(0)
