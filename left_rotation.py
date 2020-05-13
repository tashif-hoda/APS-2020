#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    arr = []
    arr.extend(a[d%n:])
    arr.extend(a[0:d%n])
    for i in range(n):
        print(arr[i], end=" ")
