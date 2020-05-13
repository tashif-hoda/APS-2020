# cook your dish here
t = int(input())
for _ in range(t):
    n,c = list(map(int, input().split()))
    a = list(map(int, input().split()))
    s = sum(a)
    if c>=s:
        print("Yes")
    else:
        print("No")
