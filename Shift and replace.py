'''
# Sample code to perform I/O:
 
name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT
 
# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
 
# Write your code here
n=int(input())
a=list(map(int, input().split()))
# a_i=[[a[i],i] for i in range(n)]
nspp={}
mval=float('inf')
cmi=0
for i in range(n):
    if a[i]<n+1:
        diff=abs(i-a[i]+1)
        ix=min(diff, n-diff)
        if ix in nspp:
            nspp[ix]+=1
            if ix+n-nspp[ix]<mval:
                mval=ix+n-nspp[ix]
                cmi=ix
        else:
            nspp[ix]=1
            if ix+n-nspp[ix]<mval:
                mval=ix+n-nspp[ix]
                cmi=ix
 
Q=int(input())
for _ in range(Q):
    x,b=map(int, input().split())
    if a[x-1]<=n: 
        diff=abs((x-1)-a[x-1]+1)
        ix=min(diff, n-diff)
        nspp[ix]-=1
        if ix==cmi: mval+=1
        elif ix+n-nspp[ix]<mval:
            mval=ix+n-nspp[ix]
            cmi=ix
        a[x-1]=b
        if b<=n:
            diff=abs((x-1)-a[x-1]+1)
            ix=min(diff, n-diff)
            if ix in nspp:
                nspp[ix]+=1
                if ix==cmi: mval-=1
                elif ix+n-nspp[ix]<mval:
                    mval=ix+n-nspp[ix]
                    cmi=ix
            else:
                nspp[ix]=1
    else:
        a[x-1]=b
        if b<=n:
            diff=abs((x-1)-a[x-1]+1)
            ix=min(diff, n-diff)
            if ix in nspp:
                nspp[ix]+=1
                if ix==cmi: mval-=1
                elif ix+n-nspp[ix]<mval:
                    mval=ix+n-nspp[ix]
                    cmi=ix
            else:
                nspp[ix]=1
    if mval>n: mval=n
    print(mval)
Language: Python 3
