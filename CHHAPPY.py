T=int(raw_input())
while T>0:
    n=int(raw_input())
    a=map(int, raw_input().split(" "))
    b=list(set(a))
    c=[]
    for i in b:
        
        c.append(a[i-1])
   # print(b,c)
    if len(c)==len(set(c)):
        print "Poor Chef"
    else:
        print "Truly Happy"
    T-=1
