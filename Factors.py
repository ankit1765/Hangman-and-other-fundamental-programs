#This program finds the factors of any provided number and tells you
#how many factors there are

num = int(input("Enter a number: "))
count = 1
factors = 0
array = ""


print"\nThe factors for", num, "are: ",
while count <= num:
    if num%count == 0:
        factors += 1
        print"", count,

    count += 1

print"\n"
print"Your number has", factors, "factors"



