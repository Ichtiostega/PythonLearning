import myHeaders
myHeaders.printl("Dictionaries", 16)

customer = {
    "name":         "John Smith",
    "age":          30,
    "is_verified":  True,
}

print(customer["name"])

print(customer.get("birthdate"))
print(customer.get("birthdate", "jan 1 1980"))  #jan 1 1980 default value
print(customer.get("birthdate"))

customer["name"] = "kapitan John Smith"
print(customer.get("name"))

customer["birthdate"] = "feb 2 1990"
print(customer.get("birthdate"))

#Number spell

numbers = {
    "0":    "zero",
    "1":    "one",
    "2":    "two",
    "3":    "three",
    "4":    "four",
    "5":    "five",
    "6":    "six",
    "7":    "seven",
    "8":    "eight",
    "9":    "nine"
}

number = str(input("Phone:\t"))
numberSpelled = ''
for digit in number:
    numberSpelled += numbers.get(digit, "!") + "\t"
print(numberSpelled)