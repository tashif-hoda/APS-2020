#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.
def dfs(visited, graph, node, roads):
    if node not in visited:
        roads+=1
        visited.add(node)
        for i in graph[node]:
            roads=dfs(visited, graph, i, roads)
    return roads
        

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib<=c_road:
        return n*c_lib
    else:
        visited=set()
        adj={}
        for i in range(len(cities)):
            if cities[i][0] in adj:
                adj[cities[i][0]].append(cities[i][1])
            else:
                adj[cities[i][0]]=[cities[i][1]]
            if cities[i][1] in adj:
                adj[cities[i][1]].append(cities[i][0])
            else:
                adj[cities[i][1]]=[cities[i][0]]
        totcost=0
        for i in range(1, n+1):
            if i in adj:
                if i not in visited:
                    nr=-1
                    nr=dfs(visited, adj, i, nr)
                    # print(nr)
                    totcost+=nr*c_road+c_lib
            else:
                totcost+=c_lib
        return totcost
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
