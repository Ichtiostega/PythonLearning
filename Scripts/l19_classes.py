import myHeaders
myHeaders.printl("Classes", 19)

class Point:
    def move(self):
        print("move")
    

    def draw(self):
        print("draw")


point1 = Point()
point1.draw()
point1.x = 10
point1.y = 20
print(point1.x)

point2 = Point()
#print(point2.x)    Error. No x in point2