#!/bin/python3

import sys

def toys(w):
    # Complete this function
    w.sort()
    n=len(w)
    m=w[0]
    groups=1
    for i in range(1,len(w)):
        if w[i]-m>4:
            m=w[i]
            groups+=1
    return groups

if __name__ == "__main__":
    n = int(input().strip())
    w = list(map(int, input().strip().split(' ')))
    result = toys(w)
    print(result)
