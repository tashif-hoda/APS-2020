T=int(raw_input())
while T>0:
    n=int(raw_input())
    l=0
    for i in range(n):
        p,q,d=raw_input().strip().split(" ")
        p=int(p)
        q=int(q)
        d=int(d)
        p1=float(p)*(100+d)/100
        p1=(p1*(100-d)/100)
        l+=(p-p1)*q
    print l    
    T-=1
