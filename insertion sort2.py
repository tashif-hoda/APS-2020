#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.\
def pr(a):
    for i in a:
        print(i, end=" ")
    print()

def insertionSort2(n, arr):
    for i in range(1, len(arr)):
        for j in range(0, i+1):
            if arr[i]<arr[j]:
                temp=arr[i]
                for k in range(i, j, -1):
                    arr[k]=arr[k-1]
                arr[j]=temp
        pr(arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
