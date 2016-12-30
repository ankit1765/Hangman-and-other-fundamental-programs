# THIS PROGRAM USES STRINGS, TUPLES, AND LIST MANIPULATION TO
# PRODUCE THE HANGMAN GAME FOR CHILDREN


import random

hangman = (
"""
    ||========||
    ||        ||
    ||        |
    ||
    ||
    ||
             """,
"""
   ||========||
   ||        ||
   ||        |
   ||        O
   ||
   ||
   ||
              """,
"""
   ||========||
   ||        ||
   ||        |
   ||        O
   ||        |
   ||
   ||
              """,
"""
  ||========||
  ||        ||
  ||        |
  ||        O
  ||        |_
  ||
  ||
              """,
"""
  ||========||
  ||        ||
  ||        |
  ||        O
  ||       _|_
  ||
  ||
              """,
"""
 ||========||
 ||        ||
 ||        |
 ||        O
 ||       _|_
 ||        |
 ||
            """,
"""
||========||
||        ||
||        |
||        O
||       _|_
||        |
||       /
            """,
"""
||========||
||        ||
||        |
||        O
||       _|_
||        |
||       / \  """,

"""
||========||
||        ||
||        |
||        O
||      \_|_
||        |
||       / \ """,
"""
||========||
||        ||
||        |
||        O
||      \_|_/
||        |
||       / \ """)

#(0,1,2,3,4,5,6,7,8,9) ---> REFERENCE FOR HANGMANS

playagain = 0

while playagain == 0:

    words = ("COMPUTER", "TELEVISION", "CERTIFICATE", "OFFICE", "MONITOR", "KEYBOARD", "DRIVEWAY", "STAIRCASE")
    num = random.randrange(0, len(words))
    word = words[num] #Word contains the string of the randomly chosen word
    man = 0
    usedletters = ""
    countused = 0

    wordlist = [] #wordlist is a list version of the word
    count = 0
    for letters in word:
        wordlist += word[count]
        count += 1

    modifiedword = [] #modifiedword starts out as list that contains spaces (# of spaces = # of letters in word)
    for letters in word:
        modifiedword += "_"

    origword = wordlist[:] #Preserve the original wordlist by copying to origword

    while modifiedword != origword: #modifiedword starts as spaces, but will ultimately become origword as user takes guesses
        inputletter = raw_input("\n\nGuess a letter: ")
        inputletter = inputletter.upper() #for consistency, take users letter and make it capital.

        if inputletter in wordlist: #if the users letter is in the wordlist, then get the index of the letter in word list
            index = wordlist.index(inputletter)
            wordlist[index] = "_"   #and place a _ in place of it
            modifiedword[index] = inputletter #while adding that letter to the modifiedword list at the same location
            print"Great Job!", inputletter, "is in the word!"

        elif inputletter not in wordlist:
            man += 1 #adding an element to the hangedman
            print"Sorry,", inputletter, "isn't in the word."

        print(hangman[man])
        usedletters += inputletter

        print"You've guessed the following letters: ",
        for lets in usedletters:
            print(lets),

        print"\nSo far, the word is: ",
        for lets in modifiedword:
            print(lets),

        if man >= 9:
            print"\n\nSORRY, BUT YOU HAVE HANGED THE MAN. PLEASE TRY AGAIN NEXT TIME"
            print"\nThe word was", word
            break
        
    if man < 9:
        print"\n\nCongrats, you are done!"

    playagain = int(raw_input("\nENTER 0 TO PLAYAGAIN OR 1 TO QUIT: "))
