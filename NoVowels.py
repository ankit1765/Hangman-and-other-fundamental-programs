#This program takes a message / word / sentence, and returns it
#without the vowels


print"I will turn any message into a code. All voewels will be deleted"
message = raw_input("Enter your message here: ")
newmessage = ""
vowel = "AEIOUYaeiouy"

print"\nThis is the message without vowels\n\n",
for letter in message:
  if letter not in vowel:
    newmessage += letter
print(newmessage)
