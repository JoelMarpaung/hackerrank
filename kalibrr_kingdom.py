
def findAndContest(maps, visited, tempFraction, row, col, x,  y):
    if(x < 0 or x >= row):
        return
        
    if(y < 0 or y >= col):
        return
            
    if(visited[x][y]):
        return
            
    visited[x][y] = True
    if(maps[x][y] == '#'):
        return
            
    if(maps[x][y] != '.'):
        tempFraction.add(maps[x][y])
        

    findAndContest(maps,visited,tempFraction,row,col,x,y+1)
    findAndContest(maps,visited,tempFraction,row,col,x,y-1)
    findAndContest(maps,visited,tempFraction,row,col,x+1,y)
    findAndContest(maps,visited,tempFraction,row,col,x-1,y)
    return

import sys
sys.setrecursionlimit(500000)
dataFraction = []
dataConquer = []
number = int(input().strip())
for i in range(number):
    n = int(input().strip())
    m = int(input().strip())
    maps = []
    visited = []
    tempFractions = set()
    fractions = {}

    for j in range(n):
        maps.append(list(map(str, input().rstrip())))
    
    for j in range(n):
        arr = []
        for k in range(m):
            arr.append(False)
        visited.append(arr)

    conquer = 0

    for x in range(n):
        for y in range(m):
            tempFractions = set()
            findAndContest(maps, visited, tempFractions, n, m, x, y)

            if(len(tempFractions) > 1):
                conquer += 1
            else:
                for tempITR in tempFractions:
                    frac = tempITR
                    if(frac in fractions):
                        fractions[frac] = fractions[frac] + 1
                    else:
                        fractions[frac] = 1
    dataFraction.append(fractions)
    dataConquer.append(conquer)

for i in range(number):
    print('Case '+ str(i+1)+':')
    for key, value in sorted(dataFraction[i].items()):
        print(key + ' ' + str(value))

    print('contested '+ str(dataConquer[i]))
    