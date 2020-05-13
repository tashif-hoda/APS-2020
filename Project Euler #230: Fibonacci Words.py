#author: @tashif_hoda
def findlength(n):
    if n == 1:
        return len(A)
    elif n==2:
        return len(B)
    a,b,c,i=len(A),len(B),0,2
    while i<n:
        c=a+b
        a,b=b,c
        i+=1
    return c

def findidx(n) :  
    if n <= 1: 
        return n 
    a,b,c,res = len(A), len(B),0,2
    while c < n: 
        c=a+b            
        res+=1
        a=b 
        b=c    
    return res

q=int(input())
for i in range(q):
    A,B,n=input().split()
    n=int(n)
    i=n
    n=findidx(n)
    while n > 2:
        l=findlength(n-2)
        if i>l:
            i-=l
        else:
            n-=1
        n-=1

    if n==1:
        print(A[i-1])
    else:
        print(B[i-1])
