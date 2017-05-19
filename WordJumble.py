#This Project is a WORD JUMBLE game
#The user must 

import random

words = ("printer", "paper", "computer", "office", "pen", "monitor","stapler",
         "pencil", "keyboard", "mouse", "door", "certificate", "Secretary", "Window", "onion",
         "juice", "popcorn", "salad", "orange", "Apple", "Apricot", "Avocado", "Banana", "Blackberry",
         "Blueberry", "laptop", "remote","blanket","basket")

print"Welcome to the Word Jumble game!"
print"\nYou will recieve a word in the incorrect order, you must guess the word"
print"The HINT: You may find these objects in an Office Environment"
raw_input("Press Enter to start the game. ")

playagain = 0

while playagain == 0:
    num = random.randrange(0, len(words))
    word = words[num] #word is a string of the word we got!
    actualword = word
    length = len(word) #length of the word be got
    jumbled = "" #the jumbled word string
    guess = "" #the word that the user will guess

    while len(jumbled) != length:
        numletter = random.randrange(0, len(word))
        jumbled += word[numletter]
        word = word[0:numletter] + word[ numletter+1 : len(word)]

    print"\nYOUR JUMBLED WORD IS:  ", jumbled,
    guess = raw_input("\tENTER YOU GUESS: ")

    while guess.lower() != actualword.lower():
        print"                       ", jumbled,
        guess = raw_input("\tENTER YOU GUESS: ")

    print"\nYou got it! Great job!",

    playagain = int(raw_input("Enter 0 to play again, or 1 to quit: "))

print"THANKYOU FOR PLAYING - MACHUPWORDS"
