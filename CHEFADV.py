t=int(raw_input())

while t>0:
    n,m,x,y=map(int, raw_input().split(" "))
    if ((n-1)%x==0 and (m-1)%y==0):
        print "Chefirnemo"
    elif ((n-2))%x==0 and (m-2)%y==0 and n-1>=1 and m-1>=1:
        print "Chefirnemo"
    else:
        print "Pofik"
    t-=1
