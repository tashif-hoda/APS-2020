# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
m=int(input())

k=-1

for i in range(n, m):
    if i^(i+1)>k:
        k=i^(i+1)
print(k)
