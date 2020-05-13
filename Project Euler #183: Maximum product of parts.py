# Enter your code here. Read input from STDIN. Print output to STDOUT
q = int(input())
cache = [0,0,0,0,0]
e = 2.7182818#28#45904
while q:
    q-=1
    l = int(input())
    res = cache[-1]
    st = len(cache)
    for i in range(st, l+1):
        k = round(i/e)
        while not k%5:
            k/=5
        while not k%2:
            k/=2
        if i%k:
            res+= i
        else:
            res-= i
        cache.append(res)
    print(cache[l])
