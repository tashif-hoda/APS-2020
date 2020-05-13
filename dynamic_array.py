#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    seqList = []
    for i in range(n):
        seqList.append([])
    LastAnswer = 0
    retArr= []
    for i in queries:
        #i[0] is option, i[1] is 'x' i[2] is y
        if i[0]==1:
            seqList[(i[1]^LastAnswer)%n].append(i[2])
        else:
            seq = seqList[(i[1]^LastAnswer)%n]
            LastAnswer = seq[i[2]%len(seq)]
            #print(LastAnswer)
            retArr.append(LastAnswer)
    return retArr
            

    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
