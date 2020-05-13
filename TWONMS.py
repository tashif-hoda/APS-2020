t=int(raw_input())
for i in xrange (t):
    a,b,n=map(int, raw_input().split(" "))
    if n%2!=0:
        a*=2
    print max(a,b)/min(a,b)
