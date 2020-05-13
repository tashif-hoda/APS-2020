from __future__ import division, print_function
import bisect
import math
# import heapq
import itertools
import sys
# from collections import deque
from atexit import register
# from collections import Counter
from functools import reduce
# sys.setrecursionlimit(10000000)
if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream
 
 
if sys.version_info[0] < 3:
    class dict(dict):
        """dict() -> new empty dictionary"""
        def items(self):
            """D.items() -> a set-like object providing a view on D's items"""
            return dict.iteritems(self)
 
        def keys(self):
            """D.keys() -> a set-like object providing a view on D's keys"""
            return dict.iterkeys(self)
 
        def values(self):
            """D.values() -> an object providing a view on D's values"""
            return dict.itervalues(self)
 
    input = raw_input
    range = xrange
 
    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip
 
 
def sync_with_stdio(sync=True):
    """Set whether the standard Python streams are allowed to buffer their I/O.
 
    Args:
        sync (bool, optional): The new synchronization setting.
 
    """
    global input, flush
 
    if sync:
        flush = sys.stdout.flush
    else:
        sys.stdin = stream(sys.stdin.read())
        input = lambda: sys.stdin.readline().rstrip('\r\n')
 
        sys.stdout = stream()
        register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))

def main():
    table=[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
    def csb(num):
        sbc=0
        while num:
            sbc+=table[num&0xf]
            num=num>>4
        return sbc
    t=int(input())
    while t:
        n,q=map(int, input().split())
        a=list(map(int, input().split()))
        oc=0
        for i in a:
            if csb(i)&1:
                oc+=1
        ec=n-oc
        for _ in range(q):
            qu=int(input())
            if csb(qu)&1:
                print(oc, ec)
            else:
                print(ec, oc)
            
        t-=1
if __name__ == '__main__':
    sync_with_stdio(False)
    main()
