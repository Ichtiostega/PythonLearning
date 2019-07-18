import myHeaders
myHeaders.printl("Lists", 13)

names = ['Walt', 'Jesse', 'Mike', 'Saul', 'Hank']
print(names)
print(names[-2])
print(names[2:4])

numbers = [3, 1, 4, 4, 8, 2, 1]

maximum = numbers[0]
for value in numbers:
    if maximum < value:
        maximum = value
print(maximum)

print(numbers)
numbers.append(13)
print(numbers)
numbers.insert(0, 10)
print(numbers)
numbers.remove(1)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.index(8))
print(50 in numbers)
print(numbers.count(4))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
numbers.append(10)
print(f"{numbers}\n{numbers2}")
numbers.clear()
print(numbers)

dupeList = [4, 4, 6, 3, 4, 6, 1, 1]

for item in dupeList:
    for iterator in range(dupeList.count(item) - 1):
        dupeList.remove(item)
print(dupeList)

######################  Tuples  ############################

numbers = [1, 2, 3]
t_numbers = (1, 2, 3)
print(t_numbers[1])
#t_numbers[1] = 4        TypeError: 'tuple' object does not support item assignment