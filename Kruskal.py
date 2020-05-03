#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(10000000)
#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#
rank=[0 for i in range(3001)]
parent=[i for i in range(3001)]

# def makeset(v):
#     parent[v]=v
#     rank[v]=0
def findpar(v):
    if parent[v]==v:
        return v
    parent[v]=findpar(parent[v])
    return parent[v]

def union(a, b):
    a=findpar(a)
    b=findpar(b)
    if a!=b:
        if rank[a]<rank[b]:
            a,b=b,a
        parent[b]=a
        if rank[a]==rank[b]:
            rank[a]+=1
        return 1
    return 0

def kruskals(g_nodes, g_from, g_to, g_weight):
    # Write your code here
    w=[]
    for i in range(len(g_to)):
        w.append([g_weight[i], g_from[i], g_to[i], g_weight[i]+g_from[i]+g_to[i]])
    w.sort()
    # w.sort(lambda x:x[3])
    # print(w)
    we=0
    for e in w:
        if union(e[1], e[2]):
            we+=e[0]
    return we

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    # Write your code here.
    fptr.write(str(res)+'\n')
    fptr.close()
