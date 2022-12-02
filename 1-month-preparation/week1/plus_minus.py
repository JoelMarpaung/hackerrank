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
    minCount = 0.0;
    plusCount = 0.0;
    zeroCount = 0.0;
    # Write your code here
    for x in range(len(arr)):
        if arr[x] < 0:
            minCount +=1
        elif arr[x] == 0:
            zeroCount += 1
        else:
            plusCount += 1
            
    if plusCount == 0:
        print(0.0)
    else:
        print(str(plusCount/len(arr)))
    
    if minCount == 0:
        print(0.0)
    else:
        print(str(minCount/len(arr)))
        
    if zeroCount == 0:
        print(0.0)
    else:
        print(str(zeroCount/len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
