import math as mt

def isPrime(n) : 
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

def Factors(n, k): 
	
	# list to store all prime factors of n 
	a=0
	
	#insert all 2's in list 
	while n % 2 == 0: 
		a+=1 
		n = n // 2
		
	# n must be odd at this point 
	# so we skip one element(i=i+2) 
	for i in range(3, mt.ceil(mt.sqrt(n)), 2): 
		while n % i == 0: 
			n = n // i; 
			a+=1 
			
	# This is to handle when n>2 and 
	# n is prime 
	if n > 2: 
		a+=1 
		
	# if size(a)<k,k factors are not possible 
	if a < k: 
		return False
	else:
	    return True
	
# 	for i in range(k - 1, len(a)): 
# 		product *= a[i] 
# 	print(product)

t= int(input())
while t:
    t-=1
    x,k=map(int, input().split())
    if Factors(x,k):
        print(1)
    else:
        print(0)
