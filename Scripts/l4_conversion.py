import myHeaders
myHeaders.printl("Type conversion", 4)

birth_year = input('Birth year: ')
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age)

weight_p = float(input("What is your weight in punds? "))
print(weight_p * 0.4536)