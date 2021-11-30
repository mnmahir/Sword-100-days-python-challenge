# https://docs.python.org/3/tutorial/floatingpoint.html
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = (int(input("What percentage tip you would like to give? 10, 12, or 15? ")) + 100) / 100
pax = int(input("How many people to split the bill? "))

bill_each = (bill / pax) * tip
# bill_each = round(bill_each, 2)
bill_each = "{:.2f}".format(bill_each)  # Same as above but using format method. It will force to print decimal. ie: Instead of 10.1 it will become 10.10

print(type(bill_each))
print(f"Each person should pay: ${bill_each}")