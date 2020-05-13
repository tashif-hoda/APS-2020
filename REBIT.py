mod = 998244353

t=int(input())
while t:
    t-=1
    l=input()
    q=0
    stack1=[]
    stack2=[]
    for c in l:
        if c=='#':
            stack2.append([1,1,1,1])
            q+=1
        elif c==')':
            op=stack1.pop()
            x1=stack2.pop()
            x2=stack2.pop()
            x=[0, 0, 0, 0]
            
            if op=='&':
                x[0] = x1[0]*x2[0] + x1[0]*x2[1] + x1[1]*x2[0] + x1[2]*x2[0] + x1[0]*x2[2] + x1[3]*x2[0] + x1[0]*x2[3] + x1[2]*x2[3] + x1[3]*x2[2]
                x[1] = x1[1]*x2[1]
                x[2] = x1[1]*x2[2] + x1[2]*x2[1] + x1[2]*x2[2]
                x[3] = x1[1]*x2[3] + x1[3]*x2[1] + x1[3]*x2[3]
                
            elif op=='|':
                x[0] = x1[0]*x2[0]
                x[1] = x1[0]*x2[1] + x1[1]*x2[0] + x1[1]*x2[1] + x1[2]*x2[1] + x1[1]*x2[2] + x1[3]*x2[1] + x1[1]*x2[3] + x1[2]*x2[3] + x1[3]*x2[2]
                x[2] = x1[0]*x2[2] + x1[2]*x2[0] + x1[2]*x2[2]
                x[3] = x1[0]*x2[3] + x1[3]*x2[0] + x1[3]*x2[3]
                
            elif op=='^':
                x[0] = x1[0]*x2[0] + x1[1]*x2[1] + x1[2]*x2[2] + x1[3]*x2[3]
                x[1] = x1[0]*x2[1] + x1[1]*x2[0] + x1[2]*x2[3] + x1[3]*x2[2]
                x[2] = x1[2]*x2[0] + x1[0]*x2[2] + x1[3]*x2[1] + x1[1]*x2[3]
                x[3] = x1[3]*x2[0] + x1[0]*x2[3] + x1[2]*x2[1] + x1[1]*x2[2]
            
            stack1.pop()
            stack2.append(x)
                
        else:
            stack1.append(c)
    x = stack2.pop()
    q=4**q
    print((x[0]*pow(q, mod-2, mod))%mod, (x[1]*pow(q, mod-2, mod))%mod, (x[2]*pow(q, mod-2, mod))%mod, (x[3]*pow(q, mod-2, mod))%mod)
