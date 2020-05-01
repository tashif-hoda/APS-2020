# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=[]
for _ in range(n):
    l.append(int(input()))
# print(l)
sub=[l[0]]
for i in range(1,n):
    if l[i]>sub[-1]:
        sub.append(l[i])
    # elif l[i]<sub[0]:
    #     sub[0]=l[i]
    else:
        high=len(sub)-1
        low=0
        while high>=low:
            mid=(low+high)//2
            if sub[mid]>=l[i]:
                high=mid-1
            else:
                low=mid+1
            # print(mid)
        sub[low]=l[i]
# print(sub)
print(len(sub))
