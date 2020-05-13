# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import floor

def f(b, x):
    return floor(2**(b - x**2)) * 1e-9

u0, b = map(float, input().split())
un = u0
un1 = f(b, un)
for i in range(200):
    un = f(b, un)
    un1 = f(b, un1)
print("{0:.9f}".format(un+un1))
