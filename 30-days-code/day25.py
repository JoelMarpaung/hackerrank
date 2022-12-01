from math import sqrt
# Enter your code here. Read input from STDIN. Print output to STDOUT
def checkPrime(y):
    for z in range(2,int(sqrt(y)+1)):
            if(y%z == 0):
                return False
    return True
        
    
n = int(input())
for x in range(n):
    y = int(input())
    if(checkPrime(y) and y > 1):
        print('Prime')
    else:
        print('Not prime')
    