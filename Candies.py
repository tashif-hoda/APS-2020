#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    sarr=[0 for _ in range(n)]
    dic={}
    for i in range(n):
        if arr[i] in dic:
            dic[arr[i]].append(i)
        else:
            dic[arr[i]]=[]
            dic[arr[i]].append(i)
    # print(dic)
    ac=sorted(dic.keys())
    for ind in ac:
        for i in dic[ind]:
            if sarr[i]==0:
                sarr[i]=1
            if i>=0 and i<n-1:
                if arr[i+1]>arr[i] and sarr[i+1]<=sarr[i]:
                    sarr[i+1]=sarr[i]+1
            if i>0 and i<=n-1:
                if arr[i-1]>arr[i] and sarr[i-1]<=sarr[i]:
                    sarr[i-1]=sarr[i]+1
    # print(sarr)
    return(sum(sarr))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
