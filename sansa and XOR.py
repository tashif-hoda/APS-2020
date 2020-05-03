#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sansaXor function below.
#ceil()
def sansaXor(arr, n):
    #nel = math.ceil(n/2)
    if n&1:
        xsum=arr[0]
        for i in range(2, n, 2):
            xsum^=arr[i]
        return xsum
            
    else:
        return 0
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr, n)

        fptr.write(str(result) + '\n')

    fptr.close()
