#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0 for i in range(n+1)]
    for query in queries:
        #query[0] = starting index, query[1] = stopping index,
        #query[2] = value to be added
        arr[query[0]-1]+=query[2]
        arr[query[1]]-=query[2]
    maxval = x = 0
    for i in arr:
        x+=i
        if x>maxval:
            maxval = x
    return maxval
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
