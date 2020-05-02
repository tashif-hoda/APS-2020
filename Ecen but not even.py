t = int(input())

while t:
    n = int(input())
    s = input()
    no=0
    pr=""
    for i in s:
        if int(i)&1:
            pr+=i
            no+=1
        if no>=2:
            break
    if no<2:
        print(-1)
    else:
        print(pr)
    
    t-=1
