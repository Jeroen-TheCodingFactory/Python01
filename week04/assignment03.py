name = input("Enter the player's name: ")
age = int(input("Enter the age of " + name))
height = int(input("Enter the height of Jack in cm"))

if(age >= 16 and age < 31 and height >= 180):
    print(name," is selected")
else:
    print(name, " is rejected")