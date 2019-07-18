import myHeaders
myHeaders.printl("Exceptions", 18)


try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("You antered a nan.")
except ZeroDivisionError:
    print("0 is an invalid value.")