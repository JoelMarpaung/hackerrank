#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    minSum = 0
    maxSum = 0
    # Write your code here
    for x in range(len(arr)):
        val = sum(arr) - arr[x]
        if(x==0):
            minSum = val
            maxSum = val
        else:
            maxSum = max(maxSum, val)
            minSum = min(minSum, val)
            
    print(str(minSum) + ' ' + str(maxSum))
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
