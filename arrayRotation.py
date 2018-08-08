#!/bin/python
#array rotation problem on hackerrank
#https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    l=len(a)
    t1=a[0:d]
    t2=a[d:l]
    newlist=t2+t1
    return newlist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
