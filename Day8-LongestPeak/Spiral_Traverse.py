def spiralTraverse(array):
    result = []
    startingRow, startingColumn, endingRow, endingColumn = 0, 0, len(array)-1, len(array[0])-1

    while startingRow <=  endingRow and startingColumn <= endingColumn:
        
        for i in range(startingColumn,endingColumn+1):
            result.append(array[startingRow][i])

        for i in range(startingRow+1,endingRow+1):
            result.append(array[i][endingColumn])

        for i in range(endingColumn-1,startingColumn-1,-1):
            if startingRow == endingRow:
                break
            result.append(array[endingRow][i])

        for i in range(endingRow-1, startingRow,-1):
            if startingColumn == endingColumn:
                break
            result.append(array[i][startingColumn])

        startingRow+=1
        startingColumn+=1
        endingRow-=1
        endingColumn-=1

    return result

print(spiralTraverse([
    [1, 2, 3, 4],
    [12, 13, 14, 5], 
    [11, 16, 15, 6], 
    [10, 9, 8, 7]]))