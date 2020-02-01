n=int(input())
arr = [0 for i in range(n+1)]
arr[0]=1
seq=list(map(int, input().split())
for x in seq:
	for i in range(x, n+1):
		if arr[i-x] != 0:
			arr[i]+=arr[i-x]

print(arr[n])
