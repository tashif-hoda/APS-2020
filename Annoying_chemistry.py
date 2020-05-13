import sys
sys.setrecursionlimit(10000000)
 
def gcd(a,b): 
	if a == 0: 
		return b 
	return gcd(b % a, a) 
 
# Function to return LCM of two numbers 
def lcm(a,b): 
	return (a*b) // gcd(a,b) 
 
# Write your code here
x,y,p,q=map(int, input().split())
b3=lcm(lcm(x,p)//p, lcm(y,q)//q)
b1=(b3*p)//x
b2=(b3*q)//y
print(b1, b2, b3)
