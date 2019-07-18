import myHeaders
myHeaders.printl("Functions", 17)

def greeting():
    print("Hello there!")
    print("General Kenobi!")


print("Start")
greeting()
print("Finish")

def personalized_greeting(name):
    print(f"Hello {name}!")
    print("Nice shoes.")


personalized_greeting("Susan")

def personalized_greeting_defaulted(name = "Operator"):
    print(f"Hello {name}!")
    print("Nice shoes.")


personalized_greeting_defaulted()

def calc_cost(value, shipping, discount):
    return value * (1 - discount) + shipping


print(calc_cost(50, 5, 0.2))
print(calc_cost(discount=0.2, value = 50, shipping = 5))    #Keyword arguments.
print(calc_cost(50, discount=0.2, shipping = 5))            #Keyword arguments have to be at the end of the arg list.