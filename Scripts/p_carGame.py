import myHeaders
myHeaders.printp("Car Game")

is_started = False

while True:
    playerInput = input(">").lower()
    if playerInput == "start":
        if is_started:
            print("Already started")
        else:
            print("Car started...Ready to go!")
            is_started = True
    elif playerInput == "stop":
        if is_started:
            print("Car stopped")
            is_started = False
        else:
            print("Car already stopped")
    elif playerInput == "help":
        print("Start\t-\tStarts the car\nStop\t-\tStops the car\nQuit\t-\tQuits the game")
    elif playerInput == "quit":
        break
    else:
        print("I don't understand...")