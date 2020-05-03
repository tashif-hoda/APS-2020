t=int(input())
while t:
    t-=1
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()
    m1=float('inf')
    mi=0
    ao=0
    bo=0
    for i in range(n-1):
        val=(a[i]&a[i+1])^(a[i]|a[i+1])
        if val<m1:
            m1=val
    # print(a)
    # print(ao,bo)
    print(m1)
