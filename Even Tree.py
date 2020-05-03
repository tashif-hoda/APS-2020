#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the evenForest function below.
def dfs(visited, graph, node, size):
    if node not in visited:
        visited.add(node)
        size+=1
        for i in graph[node]:
            size=dfs(visited, graph, i, size)
    return size

def evenForest(t_nodes, t_edges, t_from, t_to):
    # adj={i:[] for i in range(1, t_nodes+1)}
    cuts=0
    for k in range(t_edges):
        adj={i:[] for i in range(1, t_nodes+1)}
        for i in range(t_edges):
            if i!=k:
                adj[t_from[i]].append(t_to[i])
                adj[t_to[i]].append(t_from[i])
        visited=set()
        size=0
        n=dfs(visited, adj, t_from[k], size)
        # print(n)
        if not n&1:
            cuts+=1
        visited.clear()
    # print(adj)
    return cuts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
