# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
while t:
    t-=1
    s=input()
    delc=0
    # recc=0
    for i in range(1,len(s)):
        if s[i]=='A' and s[i-1]=='A':
            delc+=1
        elif s[i]=='B' and s[i-1]=='B':
            delc+=1
    print(delc)
