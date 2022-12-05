#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    arrTime = s.split(':')
    numberHour = int(arrTime[0])
    numberMinute = int(arrTime[1])
    numberSecond = arrTime[2]
    hour = ''
    if 'AM' in s:
        if numberHour == 12 and (numberMinute > 0 or numberMinute == 0):
            numberHour = '00'
        else:
            numberHour = str(numberHour).zfill(2)
        numberMinute = str(numberMinute).zfill(2)
        numberSecond = numberSecond.replace('AM','')
    else:
        if numberHour < 12:
            numberHour = str(numberHour + 12).zfill(2)
        else:
            numberHour = str(numberHour).zfill(2)
        numberMinute = str(numberMinute).zfill(2)
        numberSecond = numberSecond.replace('PM','')
    
    return numberHour + ':' + numberMinute + ':' + numberSecond

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
