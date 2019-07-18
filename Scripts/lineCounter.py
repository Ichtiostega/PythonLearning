import pathlib
import columns

masterCount = 0
countArray = ["Line count", ""]
fileArray = ["File name", ""]
myFiles = pathlib.Path(".").glob("*.py")
for item in list(myFiles):
    myFile = open(item, "r")
    count = 0
    while True:
        s = myFile.readline()
        if s == '':
            break
        count += 1
    countArray.append(str(count))
    masterCount+=count
    fileArray.append(f"{item}")

fileArray.append("")
fileArray.append("Total line count:")
countArray.append("")
countArray.append(str(masterCount))
printArray = [fileArray, countArray]
columns.columnPrint(printArray)