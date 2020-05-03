#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def pr(a):
    for i in a:
        print(i, end=" ")
    print()

def insertionSort1(n, arr):
    temp=arr[n-1]
    for i in range(n-2, -1, -1):
        if arr[i]>temp:
            arr[i+1]=arr[i]
            pr(arr)
        else:
            arr[i+1]=temp
            pr(arr)
            return
    arr[0]=temp
    pr(arr)
    return
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
