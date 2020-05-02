T=int(raw_input())
while T>0:
    n=int(raw_input())
    a=raw_input().strip().split(" ")
    aset=set(a)
    print n-len(aset)
    T-=1
