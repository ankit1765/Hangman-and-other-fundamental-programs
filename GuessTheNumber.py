#This program creates a very simple game where the user chooses a range
#in which the computer will pick a random number
#The user must guess the number by getting feedback everytime they take a guess
#It incorperates the sleep function to mimic the "computer thinking" process


import random
import time

playagain = 0

while playagain == 0:

    range = int(input("What is the range, 0 to: "))
    var = random.randrange(range)
    numuser = range + 1000
    count = 0

    while numuser != var:
        numuser = int(input("\nEnter your guess here: "))

        
        print".",
        time.sleep(0.3)
        print".",
        time.sleep(0.2)
        print".",
        time.sleep(0.1)
        
        if numuser > var:
            print("Your guess is too high!")

        elif numuser < var:
            print("Your guess is too low!")

        count += 1

    print"You did it in", count, "guesses"

    playagain = int(input("Press 0 to play again, or 1 to quit"))
    print("\n")
