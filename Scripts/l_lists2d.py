import myHeaders
myHeaders.printl("Lists2d", 13)

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(f"Element (1,2): {matrix[1][2]}")

for row in matrix:
    for element in row:
        print(element)