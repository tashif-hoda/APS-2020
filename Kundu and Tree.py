#Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())

par=[i for i in range(n+1)]
size=[1]*(n+1)

def nc3(x):
    return (x*(x-1)*(x-2))//6
def nc2(x):
    return (x*(x-1))//2

def findpar(v):
    if v==par[v]:
        return v
    par[v]=findpar(par[v])
    return par[v]

def union(a,b):
    a=findpar(a)
    b=findpar(b)
    if a!=b:
        if size[b]>size[a]:
            a,b=b,a
        par[b]=a
        size[a]+=size[b]

total=nc3(n)
for i in range(n-1):
    a,b,c=input().split()
    if c=='b':
        union(int(a), int(b))

# pset.remove(0)

for i in range(1,len(par)):
    if i==par[i]:
        total-=nc3(size[par[i]])
        total-=nc2(size[par[i]])*(n-size[par[i]])

print(total%1_000_000_007)
