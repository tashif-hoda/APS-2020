#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
t = int(sys.stdin.readline())

for t_itr in range(t):
    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    # edges = []
    adj=[[] for i in range(n+1)]
    inserted=[0 for i in range(n+1)]
    # inserted2=[0 for i in range(n+1)]
    for _ in range(m):
        i=map(int, sys.stdin.readline().rstrip().split())
        if not adj[i[0]] or not adj[i[1]]:
            adj[i[0]].append([i[2], i[1]])
            adj[i[1]].append([i[2], i[0]])
            inserted[i[0]]+=1
            inserted[i[1]]+=1
        else:
            match=True
            if inserted[i[0]]<20 and inserted[i[1]]<20:
                match=False
                for x in adj[i[0]]:
                    if x[1]==i[1]:
                        if x[0]>i[2]:
                            match=True
                            x[0]=i[2]
                            break
                for x in adj[i[1]]:
                    if x[1]==i[0]:
                        if x[0]>i[2]:
                            x[0]=i[2]
                            break
            if not match:
                adj[i[0]].append([i[2], i[1]])
                adj[i[1]].append([i[2], i[0]])

    s = int(sys.stdin.readline())
    
    q=[]
    dist=[float('inf') for _ in range(n+1)]
    dist[s]=0
    heapq.heappush(q,[dist[s],s])
    while q:
        x=heapq.heappop(q)
        # print(x, end=" ")
        for i in adj[x[1]]:
            if x[0]+i[0]<dist[i[1]]:
                dist[i[1]]=x[0]+i[0]
                heapq.heappush(q, [dist[i[1]], i[1]])
    for x in dist[1:]:
        if x!=0 and x<float('inf'):
            sys.stdout.write(str(x)+" ")
        if x==float('inf'):
            sys.stdout.write(str(-1)+" ")
