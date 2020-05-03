#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
# Complete the bfs function below.
def bfs(n, m, edges, s):
    adj={i:set() for i in range(1,n+1)}
    for i in range(m):
        adj[edges[i][0]].add(edges[i][1])
        adj[edges[i][1]].add(edges[i][0])
    print(adj)
    q=deque()
    visited=[False for _ in range(n+1)]
    visited[s]=True
    q.append(s)
    darr=[-1 for _ in range(n+1)]
    darr[s]=0
    while q:
        x=q.popleft()
        for i in adj[x]:
            if visited[i]==False:
                visited[i]=True
                q.append(i)
                darr[i]=darr[x]+6
    res=[]
    for i in darr[1:]:
        if i:
            res.append(i)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
