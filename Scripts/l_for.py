import myHeaders
myHeaders.printl("For Loops", 11)

for item in 'Python':
    print(item)

for item in ['Mosh', 'John', 'Sarah']:
    print(item)

for item in range(5,10,2):
    print(item)

prices = [10, 42, 13, 27, 43]
value = 0
for price in prices:
    value += price
print(f"Sum: {value}")

for x in range(2):
    for y in range(3):   
        print(f"({x},{y})")

numbers = [2, 2, 2, 2, 5]

for nr in numbers:
    line = ''
    for i in range(nr):
        line += 'x'
    print(line)