t=int(input())
while t:
    n,m=map(int, input().split())
    f=list(map(int, input().split()))
    p=list(map(int, input().split()))
    cost={}
    for i in range(n):
        if f[i] in cost:
            cost[f[i]]+=p[i]
        else:
            cost[f[i]]=0
            cost[f[i]]+=p[i]
    print(min(cost.values()))
    t-=1
