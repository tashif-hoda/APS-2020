import math as mt
MAXN = 100001
spf = [0 for i in range(MAXN)] 
def sieve(): 
    spf[1] = 1
    for i in range(2, MAXN): 
        spf[i] = i 
    for i in range(4, MAXN, 2): 
        spf[i] = 2
    for i in range(3, mt.ceil(mt.sqrt(MAXN))): 
        if (spf[i] == i): 
            for j in range(i*i, MAXN, i):  
                if spf[j] == j: 
                    spf[j] = i 
def getFactorization(x): 
    dic = {1:1}
    while (x != 1): 
        if spf[x] in dic:
            dic[spf[x]]+=1
        else:
            dic[spf[x]]=1
        x = x//spf[x] 
    return dic
sieve()
T = int(input())
while T:
    n,m = list(map(int, input().split()))
    x=list(map(int, input().split()))
    y=list(map(int, input().split()))
    c=1
    psq=set()
    while c**2<100001:
        psq.add(c**2)
        c+=1
    xs = set(x)
    ys = set(y)
    ntri=0
    for i in x:
        if i<0:
            fact_dict = getFactorization(abs(i))
            factors = fact_dict.keys()
            mult=1
            for xi in factors:
                if fact_dict[xi]&1:
                    mult*=xi
            for j in psq:
                if mult*j in xs:
                    if mt.sqrt(-i*mult*j) in ys:
                        ntri+=1
                    if -1*mt.sqrt(-i*mult*j) in ys:
                        ntri+=1
        elif i==0:
            ntri+=(len(x)-1)*len(y)
    for i in y:
        if i<0:
            fact_dict = getFactorization(abs(i))
            factors = fact_dict.keys()
            mult=1
            for xi in factors:
                if fact_dict[xi]&1:
                    mult*=xi
            for j in psq:
                if mult*j in ys:
                    if mt.sqrt(-i*mult*j) in xs:
                        ntri+=1
                    if -1*mt.sqrt(-i*mult*j) in xs:
                        ntri+=1
        elif i==0:
            ntri+=len(x)*(len(y)-1)
    print(ntri)
    T-=1
