import myHeaders
myHeaders.printl("Random Number Generator", 24)

import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10,20))

people = ["Jimmy", "Kim", "Henry"]
print(f"Leader:\t{random.choice(people)}")


class Dice:
    def roll(self):
        return (random.randint(1,6),random.randint(1,6))


dice = Dice()
print(dice.roll())
print(dice.roll())
print(dice.roll())
print(type(dice.roll()))