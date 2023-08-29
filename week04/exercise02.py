secret = 4
character= input("Guess a number from 1 to 5: ")

if secret == int(character):
    print("Number ", character, " is correct")
else:
    print("Number ", character, " is incorrect")


