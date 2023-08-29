price = 8000
is_customer = False
manufacture_year = 2010

if  price >= 6000:
    price -= 200
if is_customer:
    price -= 250
if  manufacture_year < 2000:
    price -= 150
else:
    price -= 50

#verkeerde if statement gaat af!

print("Total price is €%0.2f" % price)
