#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    for x in range(1,11):
        print(str(n) + ' x ' + str(x) + ' = ' + str(x*n))