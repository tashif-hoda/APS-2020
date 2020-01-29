s1=input()
s2=input()

l=[[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]

for i in range(1, len(s1)+1):
	for j in range(1, len(s2)+1):
		if s1[i-1]==s2[j-1]:
			l[i][j]=l[i-1][j-1]+1
			#print(l)
		else:
			l[i][j] = max(l[i-1][j], l[i][j-1])

print(l[i][j])
