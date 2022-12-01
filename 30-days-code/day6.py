# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    x = int(input().strip())
    for n in range(0, x):
        word = input().strip()
        word1 = ''
        word2 = ''
        for y in range(0, len(word)):
            if(y%2 ==  0):
                word1 += word[y]
            else:
                word2 += word[y]
        print(word1 + ' ' + word2)