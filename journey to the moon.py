# Enter your code here. Read input from STDIN. Print output to STDOUT\
# Complete the journeyToMoon function below.
import sys

def dfs_count(graph, visited, node, count):
    if visited[node]==False:
        visited[node]=True
        count+=1
        for n in graph[node]:
            count = dfs_count(graph, visited, n, count)
    return count
        
sys.setrecursionlimit(1500)
n,p= input().split()
n = int(n)
p = int(p)

astronaut = []
for _ in range(p):
    astronaut.append(list(map(int, input().split())))
graph=[[] for _ in range(n)]
for i in range(p):
    graph[astronaut[i][0]].append(astronaut[i][1])
    graph[astronaut[i][1]].append(astronaut[i][0])

countarr=[]
visited=[False for _ in range(n)]
for i in range(n):
    if visited[i]==False:
        count=0
        count = dfs_count(graph, visited, i, count)
        countarr.append(count)

if len(countarr)>1:
    res=countarr[0]*countarr[1]
    csum=countarr[0]+countarr[1]
    for i in countarr[2:]:
        res+=csum*i
        csum+=i
    print(res)
else:
    print(0)
