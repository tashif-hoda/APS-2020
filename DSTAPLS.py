# cook your dish here
t = int(input())
while t > 0:
    n,k = input().split(" ")
    n = int(n)
    k = int(k)
    
    if n%(k**2):
        print ("YES")
    else:
        print("NO")
    
    t = t-1
