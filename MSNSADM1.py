# cook your dish here
t = int(input())
while t > 0:
    n = input()
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    
    score = []
    for i in range(len(a)):
        sc = 20*a[i]-10*b[i]
        if sc > 0:
            score.append(sc)
        else:
            score.append(0)
            
    print (max(score))
    t = t-1
