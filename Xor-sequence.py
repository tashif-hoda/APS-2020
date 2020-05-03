#!/bin/python3

import os
import sys

#
# Complete the xorSequence function below.
#
def xorSequence(l, r):
    n=l+4-l%4
    m=r-r%4
    t=m if (m-n)%8==0 else m+2
    for i in range(l, n):
        if i%4==0:
            t^=i
        elif i%4==1:
            t^=1
        elif i%4==2:
            t^=i+1
        # print(i, "a")
    for i in range(m+1, r+1):
        if i%4==0:
            t^=i
        elif i%4==1:
            t^=1
        elif i%4==2:
            t^=i+1
        # print(i, "b")
    # print("done")
    return t
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        lr = input().split()

        l = int(lr[0])

        r = int(lr[1])

        result = xorSequence(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
