T=int(raw_input())

for j in range(T):
    N,U,D=raw_input().split(" ")
    N=int(N)
    U=int(U)
    D=int(D)
    H=raw_input().split(" ")
    H=map(int, H)
    H=[0]+H+[0]
    n=0
    for i in range(1,N+1):
        if (H[i]<=H[i+1] and H[i+1]-H[i]>U):
            break
        elif (H[i]>H[i+1] and H[i]-H[i+1]>D):
            n+=1
        if (n>1):
            break
    print i
