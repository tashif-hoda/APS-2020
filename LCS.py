# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int, input().split())

a=list(map(int, input().split()))
b=list(map(int, input().split()))
s1=[0]
s2=[0]
for i in range(n): s1.append(a[i])
for i in range(m): s2.append(b[i])

lcs=[[0 for j in range(m+1)] for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if s1[i]==s2[j]:
            lcs[i][j]=1+lcs[i-1][j-1]
        else:
            lcs[i][j]=max(lcs[i-1][j], lcs[i][j-1])
    
i=n
j=m
stack=[]
while i>0 and j>0:
    if lcs[i][j]==lcs[i-1][j-1]+1 and lcs[i][j]!=max(lcs[i-1][j], lcs[i][j-1]):
        stack.append(s1[i])
        i-=1
        j-=1
    else:
        if lcs[i][j]==lcs[i-1][j]:
            i-=1
        else:
            j-=1
while stack: print(stack.pop(), end=" ")
