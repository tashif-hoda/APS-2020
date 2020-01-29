def max_prod(n):
	a=[0]*n
	for i in range(2, n):
		for j in range(1, i//2+1):
			a[i] = max(a[i], j*(i-j), j*a[i-j])
	return a

n = int(input())
print(max_prod(n))
