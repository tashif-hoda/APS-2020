'''
# Sample code to perform I/O:
 
name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT
 
# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
 
# Write your code here
n=int(input())
gr=[[1 if i!=j else 0 for i in range(100)] for j in range(100)]
le=[]
c=0
for _ in range(10):
    x=map(int, input().split())
    le.extend(x)
#coordinate compression
temp=sorted(le)
dic={}
v=0
for i in range(100):
    dic[temp[i]]=v
    v+=1
for i in range(100):
    le[i]=dic[le[i]]
#coordinate compression end
# lol=[]
# lol.append(le[0:10])
# lol.append(le[10:20])
# lol.append(le[20:30])
# lol.append(le[30:40])
# lol.append(le[40:50])
# lol.append(le[50:60])
# lol.append(le[60:70])
# lol.append(le[70:80])
# lol.append(le[80:90])
# lol.append(le[90:100])
# print(gr[0][0])
st=1
en=10
while en<=100:
    for j in le[st:en]:
        gr[le[st-1]][j]=0
        gr[j][le[st-1]]=0
    st+=10
    en+=10
for i in range(100):
    for j in range(100):
        if gr[i][j]==0:
            c+=1
# print((c//2)-100)
# for x in gr:
#     print(x)
print((n*(n-1)-(c-100))//2)
