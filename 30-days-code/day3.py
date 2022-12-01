#!/bin/python3

import math
import os
import random
import re
import sys

def evenOdd(number):
    if(number%2==0):
        return True
    else:
        return False

def printWeird(number, status):
    if(status and number in range(2,5)):
        print("Not Weird")
    elif(status and number in range(6,20)):
        print("Weird")
    elif(status and number > 20):
        print("Not Weird")
    else:
        print("Weird")

if __name__ == '__main__':
    N = int(input().strip())
    printWeird(N, evenOdd(N))
    
