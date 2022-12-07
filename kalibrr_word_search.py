
def searchWord(n, m, arr, word):
    matrix = wordMatrix(n, m, arr, word)
    counter = 0

    if len(matrix[0]) > 0:
        for startPosition in (matrix[0]):
            right, diagonalRightBottom, bottom, diagonalLeftBottom, left, diagonalLeftTop, top, diagonalRightTop = True, True, True, True, True, True, True, True
            for i in range(1, len(word)):
                char = word[i]
                if (right):
                    rightKey = (startPosition[0], startPosition[1]+i)
                    if rightKey not in matrix[i]:
                        right = False
                if (diagonalRightBottom):
                    diagonalRightBottomKey = (startPosition[0] + (i*1), startPosition[1]+ (i*1))
                    if diagonalRightBottomKey not in matrix[i]:
                        diagonalRightBottom = False
                if (bottom):
                    bottomKey = (startPosition[0] + (i*1), startPosition[1])
                    if bottomKey not in matrix[i]:
                        bottom = False
                if (diagonalLeftBottom):
                    diagonalLeftBottomKey = (startPosition[0] + (i*1), startPosition[1] + (i*-1))
                    if diagonalLeftBottomKey not in matrix[i]:
                        diagonalLeftBottom = False
                if (left):
                    leftKey = (startPosition[0], startPosition[1] + (i*-1))
                    if leftKey not in matrix[i]:
                        left = False
                if (diagonalLeftTop):
                    diagonalLeftTopKey = (startPosition[0] + (i*-1), startPosition[1] + (i*-1))
                    if diagonalLeftTopKey not in matrix[i]:
                        diagonalLeftTop = False
                if (top):
                    topKey = (startPosition[0] + (i*-1), startPosition[1])
                    if topKey not in matrix[i]:
                        top = False
                if (diagonalRightTop):
                    diagonalRightTopKey = (startPosition[0] + (i*-1), startPosition[1] + (i*1))
                    if diagonalRightTopKey not in matrix[i]:
                        diagonalRightTop = False


            if (right):
                counter += 1
            if (diagonalRightBottom):
                counter += 1
            if (bottom):
                counter += 1
            if (diagonalLeftBottom):
                counter += 1
            if (left):
                counter += 1
            if (diagonalLeftTop):
                counter += 1  
            if (top):
                counter += 1
            if (diagonalRightTop):
                counter += 1 
                
    return counter


def wordMatrix(n, m, arr, word):
    wordMatrix = []
    for i in range(len(word)):
        wordMatrix.append(matchLetter(n, m, word[i], arr))
    return wordMatrix


def matchLetter(n, m, char, arr):
    matches = []
    for i in range(n):
        for j in range(m):
            if char == arr[i][j]:
                matches.append((i, j))
    return matches


x = int(input().strip())
data = []
for i in range(x):
    n = int(input().strip())
    m = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(str, input().rstrip())))
    word = input().strip()
    data.append(searchWord(n, m, arr, word))

for y in range(x):
    print('Case '+str(y+1)+': '+ str(data[y]))



