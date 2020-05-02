def check_taxi(s):
    cprev = s[0]
    for c in s[1:]:
        if c=='-': continue
        if c != cprev:
            return False
    return True

def check_pizza(s):
    cprev = s[0]
    for c in s[1:]:
        if c=='-': continue
        if c>=cprev:
            return False
        cprev = c
    return True
    
t = int(input())
op_t,op_p,op_g="","",""
pmax,tmax,gmax = -1,-1,-1
for _ in range(t):
    n,name = input().split()
    n = int(n)
    num = {'p' : 0, 't' : 0, 'g' : 0}
    for i in range(n):
        s = input()
        if check_taxi(s):
            num['t']+=1
        elif check_pizza(s):
            num['p']+=1
        else:
            num['g']+=1
    if num['t']>tmax:
        tmax = num['t']
        op_t = name
    elif num['t'] == tmax:
        op_t+=", "+name
    if num['p']>pmax:
        pmax = num['p']
        op_p = name
    elif num['p'] == pmax:
        op_p+=", "+name
    if num['g']>gmax:
        gmax = num['g']
        op_g = name
    elif num['g'] == gmax:
        op_g+=", "+name
    
print("If you want to call a taxi, you should call: "+op_t+".")
print("If you want to order a pizza, you should call: "+op_p+".")
print("If you want to go to a cafe with a wonderful girl, you should call: "+op_g+".")
