balance = -30
amount = 100

if(amount >0):
    if(balance >= amount):
        newBalance = balance - amount
        print("Your new balance is:" , newBalance)
    else:
        print("Insufficient balance")
        print("Your balance is: ", balance)
else:
    print("You cannot withdraw (0) or negative amounts")