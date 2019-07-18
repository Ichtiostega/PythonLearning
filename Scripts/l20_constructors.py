import myHeaders
myHeaders.printl("Construtors", 20)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def move(self):
        print("move")
    

    def draw(self):
        print("draw")


point = Point(10,20)
print(f"Point coords: ({point.x}, {point.y})")
point.x = 15
print(f"Point coords: ({point.x}, {point.y})")

class Person:
    def __init__(self, name):
        self.name = name
    

    def talk(self):
        print(f"I am {self.name}!")


tony = Person("Iron Man")
tony.talk()