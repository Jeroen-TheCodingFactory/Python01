price = int(input("Enter the price of the product: €"))
age = int(input("Enter the age of the customer: "))

if(age <= 10 or age >= 60):
    price /= 2
else:
    price *= 0.9

print("The price for this customer is: €%.2f" % price)