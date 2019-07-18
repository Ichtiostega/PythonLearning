import myHeaders
myHeaders.printl("If Statements", 10)

is_hot = bool(int(input('Is it warm? ')))
is_cold = bool(int(input('Is it cold? ')))

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day\nWear warm clothes")
else:
    print("It's a lovely day!")
print('Enjoy your day')

if is_hot and is_cold:
    print("It's some anomaly")
if (is_hot or is_cold) and not (is_hot == is_cold):
    print("Extreme weather")

temperature = int(input("What is the temperature? "))

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

while True:
    nick = input("Try a nick: ")
    if len(nick) < 3:
        print("Must be at least 3 letters long")
        continue
    elif len(nick) > 20:
        print("Must be at most 20 letters long")
        continue
    else:
        print("Great nick!")
        break