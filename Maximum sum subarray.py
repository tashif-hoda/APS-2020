#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.
def maxSubarray(arr):
    maxg=-sys.maxsize-1
    maxc=0
    msss=0
    pos=False
    for i in range(len(arr)):
        if arr[i]>0:
            msss+=arr[i]
            pos=True
        maxc+=arr[i]
        if maxc>maxg:
            maxg=maxc
        if maxc<0:
            maxc=0
    if pos:
        return [maxg, msss]
    else:
        return [maxg, maxg]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
