#!/bin/python3

import math
import os
import random
import re
import sys

N = 6

def findMax(arr):
    max_sum = -9999999
    for i in range(0, N-2):
        for j in range(0, N-2):
            sum_arr = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            
            max_sum = max(max_sum, sum_arr)
    
    return max_sum
            

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    print(str(findMax(arr)))
    
