t=int(input())

while t:
    n,k=list(map(int, input().split()))
    a=list(map(int, input().split()))
    psl=[0]*(n+1)
    psr=[0]*(n+1)
    for i in range(1,n+1):
        psl[i]=(a[i-1]%k+psl[i-1])
        psr[n-i]=(k-a[n-i]%k+psr[n-i+1])
    #print(psl, psr)
    for i in range(1,n+1):
        if psl[i]>=psr[i]:
            print(psl[i]-psr[i])
            break
    t-=1
