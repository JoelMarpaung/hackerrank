# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    phones = {}
    for x in range(0,n):
        phone = input()
        phone = phone.split()
        phones[phone[0]] = phone[1]
        
    while True:
        try:
            phone = input()
            if phone in phones.keys():
                print(phone+'='+phones[phone])
            else:
                print('Not found')
        except:
            break