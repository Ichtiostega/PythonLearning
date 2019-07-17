import myHeaders
myHeaders.printp("Guessing Game")

answer = 5
print("\nGuess a number from 1 to 10")
guessNum = 1
while guessNum <= 3:
    guess = int(input(f"Guess number {guessNum}: "))
    if guess == answer:
        print("You won!")
        break
    guessNum += 1
else:
    print("You failed!")