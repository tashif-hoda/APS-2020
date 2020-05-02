t=int(input())

while t:
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)
    s=0
    #print(a[0:n//2])
    for i in range(n):
        s+=min(a[i], b[n-i-1])
            
    print(s)
    
    t-=1
