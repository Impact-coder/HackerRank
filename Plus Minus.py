#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n=len(arr)
    pos=0
    zero=0
    neg=0
    for i in range (0,len(arr)):
        if arr[i]>0:
            pos +=1
        elif arr[i]<0:
            neg +=1
        elif arr[i]==0:
            zero+=1
    
    p = pos/n
    x = neg/n
    z = float(zero/n)
    print('%.6f'%p)
    print('%.6f'%x)
    print('%.6f'%z)
        
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
