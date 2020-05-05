#!/bin/python3

import os
import sys

#
# Complete the componentsInGraph function below.
#

def findpar(v, parent):
    if parent[v]==v:
        return v
    parent[v]=findpar(parent[v], parent)
    return parent[v]

def union(a,b, parent, size):
    a=findpar(a, parent)
    b=findpar(b, parent)
    if a!=b:
        if size[a]<size[b]:
            a,b=b,a
        parent[b]=a
        size[a]+=size[b]

def componentsInGraph(gb):
    n=len(gb)
    parent=[i for i in range(2*(n+1))]
    size=[1 for i in range(2*(n+1))]
    for i in gb:
        union(i[0], i[1], parent, size)
    mini=sys.maxsize
    maxi=-sys.maxsize-1
    for i in range(1, 2*n+1):
        if size[findpar(i, parent)]<mini and size[findpar(i, parent)]>1:
            mini=size[findpar(i, parent)]
        if size[findpar(i, parent)]>maxi:
            maxi=size[findpar(i, parent)]
    return [mini, maxi]
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    res = componentsInGraph(gb)

    fptr.write(str(res[0])+' '+str(res[1]))
    fptr.write('\n')

    fptr.close()
