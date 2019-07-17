import pathlib

masterCount = 0
myFiles = pathlib.Path(".").glob("*.py")
for item in list(myFiles):
    myFile = open(item, "r")
    count = 0
    while True:
        s = myFile.readline()
        if s == '':
            break
        count += 1
    masterCount += count
    print(f"{item} has {count} lines of code")
print(f"All lines of code written: {masterCount}")