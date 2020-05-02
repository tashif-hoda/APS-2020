t=int(input())
day=0
while t:
    n = int(input())
    arr=[[0 for _ in range(4)] for _ in range(4)]
    mval = -999999
    while n:
        m, st = input().split()
        st=int(st)
        m=ord(m)-65
        if st==12:
            st=0
        elif st==3:
            st=1
        elif st==6:
            st=2
        elif st==9:
            st=3
        arr[m][st]+=1
        n-=1
    x1,y1,x2,y2,x3,y3,x4,y4=[0,0,0,0,0,0,0,0]
    mapp=0
    mapparr=[]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if k!=i:
                    for l in range(4):
                        if l!=j:
                            for m in range(4):
                                if m!=k and m!=i:
                                    for n in range(4):
                                        if n!=l and n!=j:
                                            for o in range(4):
                                                if o!=k and o!=m and o!=i:
                                                    for p in range(4):
                                                        if p!=n and p!=l and p!=j:
                                                            
                                                            temp=100*arr[i][j]+75*arr[k][l]+50*arr[m][n]+25*arr[o][p]
                                                            for g in [arr[i][j], arr[k][l], arr[m][n], arr[o][p]]:
                                                                if g==0:
                                                                    temp=temp-100
                                                            if temp>=mval:
                                                                mval=temp
                                                                
                                                                
                                                            
    day+=mval
    print(mval)
    
    t-=1
print(day)
