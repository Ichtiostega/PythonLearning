import myHeaders
myHeaders.printl("Files and Directories", 25)

from pathlib import Path

# Absolute path
#/home/documents
# Relative path - from current directory

path = Path("ecommerce")
print(path.exists())    #true
path = Path("Emails")
print(path.exists())    #false
path.mkdir()
print(path.exists())    #true
path.rmdir()
print(path.exists())    #false

path = Path("..")
for file in path.glob("*"):
    print(file)