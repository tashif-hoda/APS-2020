def stringify(l):
    s=""
    for i in l:
        s+=str(i)
    return s
    
m,s=map(int, input().split())
mc=m
sc=s
ans=[]
rans=[]
if sc>mc*9 or sc==0 and mc>1:
    ans=[-1]
    rans=[-1]
elif mc==1 and sc==0:
    ans=[0]
    rans=[0]
else:
    while m:
        if s>=9:
            s-=9
            rans.append(9)
        elif s<9 and s>0:
            rans.append(s)
            s=0
        else:
            rans.append(0)
        m-=1
    ans=rans.copy()
    if mc>2 and sc>1:
        fl=0
        for i in range(mc-1):
            if ans[i]<9:
                ans[i]-=1
                fl=1
                if ans[i]==-1:
                    ans[i]=0
                    ans[i-1]=8
                break
        if fl:
            ans[mc-1]=1
        ans=ans[::-1]
    elif mc==2 and sc>9:
        ans=ans[::-1]
    elif mc==2 and sc<=9:
        ans[0]-=1
        ans[1]=1
        ans=ans[::-1]
        
print(stringify(ans), stringify(rans))
