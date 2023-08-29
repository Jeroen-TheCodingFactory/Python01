price = 8000
is_customer = False
manufacture_year = 2010

if price >= 6000:
    price -= 200
elif is_customer:
    price -= 250
elif manufacture_year < 2011:
    price -= 150
else:
    price -= 50

print("Total price is €%.2f" % price)