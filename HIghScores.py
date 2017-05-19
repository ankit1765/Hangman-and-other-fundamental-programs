#This program asks is a high score displayer.
#It asks the user how many entries they would like to input
#and how many top scores it should display

scores = []

numentries = int(raw_input("How many entries would you like to Enter? "))
numtop = int(raw_input("How many top scores would you like to display? "))

count = 1
while count <= numentries:
    name = raw_input("\nEnter the name: ")
    score = int(raw_input("Enter their scrore: "))
    entry = score, name
    scores.append(entry)
    count += 1 

scores.sort(reverse=True)
scores = scores[0:numtop]

print"\t\t\tTOP", numtop, "\tSCORES\n"
print "\t\t\tPLAYER\tSCORE"
for entries in scores:
    s, p = entries
    print "\t\t\t",p,"\t",s
