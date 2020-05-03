'''
# Sample code to perform I/O:
 
name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT
 
# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
 
# Write your code here
t=int(input())
while t:
    t-=1
    s,n,m=input().split()
    n=int(n)
    m=int(m)
    s=list(s)
    sub=s[n:m+1]
    sub.sort(reverse=True)
    s[n:m+1]=sub
    st=""
    for i in s:
        st+=i
    print(st)
