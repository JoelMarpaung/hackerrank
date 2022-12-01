#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    binary = str(format(n, 'b'))
    arr_bin = binary.split('0')
    max_num = 0
    for x in range(0, len(arr_bin)):
        if(max_num < len(arr_bin[x])):
            max_num = len(arr_bin[x])
    print(max_num)
