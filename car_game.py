command = ""  # ("") it has no character in it
started = False

while True:  # all command executed repeatedly until break
    command = input("> ").lower()  # if we add lower to input function we dont have to (.lower) everytime
    if command == "start":
        if started:
            print("Its already started")
        else:
            started = True
            print("Car Started...Ready to go")

    elif command == "stop":
        if not started:
            print("Its already stopped")
        else:
            started = False
            print("Car Stopped.")

    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that ")




