#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the andProduct function below.
def andProduct(a, b, l):
    for i in l:
        if a+i<b:
            a&=a+i
    return a&b

    



if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    l = [2**i for i in range(0, 32)]
    n = int(input())
    for n_itr in range(n):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = andProduct(a, b, l)

        fptr.write(str(result) + '\n')

    fptr.close()
