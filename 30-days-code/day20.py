#!/bin/python3

import math
import os
import random
import re
import sys

def bubleSort(arr):
    numberOfSwaps = 0
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                numberOfSwaps+=1
    return numberOfSwaps

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    n = bubleSort(arr)
    print('Array is sorted in '+ str(n) +' swaps.')
    print('First Element: '+str(arr[0]))
    print('Last Element: '+str(arr[len(arr)-1]))
    # Write your code here
