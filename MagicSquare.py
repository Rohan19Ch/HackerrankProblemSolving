def formingMagicSquare(s):
    possibleSquares = [[8,1,6,3,5,7,4,9,2], [6,1,8,7,5,3,2,9,4], [2,9,4,7,5,3,6,1,8], [4,9,2,3,5,7,8,1,6], [8,3,4,1,5,9,6,7,2], [6,7,2,1,5,9,8,3,4], [4,3,8,9,5,1,2,7,6], [2,7,6,9,5,1,4,3,8]]
    oneDSquare = []
    for i in s:
        oneDSquare+=i
    print(oneDSquare)
    diffList = []
    for i in range(8):
        diff = 0
        for j in range(9):
            diff += abs(possibleSquares[i][j] - oneDSquare[j])
        diffList.append(diff)
    print(diffList)
    return min(diffList)  
s = [[2,2,7], [8,6,4], [1,2,9]]
print(formingMagicSquare(s))