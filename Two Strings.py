# Enter your code here. Read input from STDIN. Print output to STDOUT

p=int(input())

while p:
    p-=1
    s1=input()
    s2=input()
    se1=set()
    flag=True
    for c in s1:
        se1.add(c)
    for c in s2:
        if c in se1:
            print("YES")
            flag=False
            break
    if flag:
        print("NO")
