T = int(input())
while T:
    n, p = list(map(int, input().split()))
    d = list(map(int, input().split()))
    if p<d[n-1]:
        print("YES", end=" ")
        for i in range(n-1):
            print(0, end=" ")
        print(1)
    else:
        count=0
        f=False
        for i in d:
            if p%i!=0:
                f=True
                print("YES", end=" ")
                for _ in range(count):
                    print(0, end=" ")
                print(p//i+1, end=" ")
                for _ in range(n-count-1):
                    print(0, end=" ")
                print()
                break
            count+=1
        if f==False:
            fl=False
            for i in range(n-1):
                if d[i+1]%d[i]!=0:
                    print("YES", end=" ")
                    fl=True
                    x=d[i]
                    y=d[i+1]
                    i2=p//d[i+1]-1
                    i1=d[i+1]//d[i]+1
                    for _ in range(i):
                        print(0, end=" ")
                    print(i1, i2, end=" ")
                    for _ in range(i+2, n):
                        print(0, end=" ")
                    print()
                    break
            if fl==False:
                print("NO")
    
    T-=1
