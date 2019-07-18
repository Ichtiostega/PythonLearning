def columnPrint(items):
    maxStringLength = []
    for row in items:
        tempMax = 0
        for item in row:
            if len(item) > tempMax:
                tempMax = len(item)
        maxStringLength.append(tempMax)
    for i in range(len(items[0])):
        lineStr = ""
        for row in range(len(items)):
            tmpString =  items[row][i]
            tmpString += " " * (maxStringLength[row] - len(tmpString) + 4)
            lineStr += tmpString
        print(lineStr)
