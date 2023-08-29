is_certified = True
years_experience = 8

if is_certified and years_experience == 4:
    print("Salary is €4000")
elif is_certified and years_experience == 5:
    print("Salary is €4500")
elif is_certified and years_experience >= 6:
    print("Salary is €5000")
else:
    print("Sorry, rejected")