# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m =map(int, input().split())
parent=[i for i in range(n+1)]
size=[1 for i in range(n+1)]

def findpar(v):
    if parent[v]==v:
        return v
    parent[v]=findpar(parent[v])
    return parent[v]

def union(a,b):
    a=findpar(a)
    b=findpar(b)
    if a!=b:
        if size[a]<size[b]:
            a,b=b,a
        parent[b]=a
        size[a]+=size[b]

for i in range(m):
    q=input().split()
    if q[0]=='M':
        q[1]=int(q[1])
        q[2]=int(q[2])
        union(q[1], q[2])
    else:
        q[1]=int(q[1])
        print(size[findpar(q[1])])
