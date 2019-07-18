import myHeaders
myHeaders.printl("Inheritance", 21)

class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("Woof")


class Cat(Mammal):
    def screech(self):
        print("Meow")


dog1 = Dog()
dog1.walk()

cat = Cat()
cat.walk()
cat.screech()