import math 

def case(a,b,k):
    if (k > b):
        return 0
    else:
        x = int(math.floor(b/k))
        if(a>k):
            if(a%k == 0):
                x -= (int(math.floor(a/k))-1)
            else:
                x -= int(math.floor(a/k))
        return x

x = int(input().strip())
for i in range(x):
    a = int(input().strip())
    b = int(input().strip())
    k = int(input().strip())
    print('Case '+str((i+1))+': '+ str(case(a,b,k)))


#input
# 1
# 3934
# 8426
# 9126
#output
# Case 1: 0