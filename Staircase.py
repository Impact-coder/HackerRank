#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for j in range(0,n):
        i = n-j-1
        while(i>0):     
            print(" ",end='')
            i -=1
        
        i=0
        while(i<=j):     
            print("#",end='')
            i +=1
        print("")

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
