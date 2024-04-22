print("Welcome to the tip calculator!")

bill = float(input("Enter the total bill: ₼ "))
tip_percent = int(input("Enter the tip (10, 12, or 15): "))
people = int(input("Enter people count to split the bill: ₼ "))

# Splitting bill between persons (no tip)
bill_split = bill / people

# Splitting tip between persons
tip_split = bill_split * tip_percent / 100

# The amount of bill each person pays (with tip)
bill_and_tip = bill_split + tip_split

# Formating
bill_and_tip = "{:.2f}".format(bill_and_tip)
print(f"{people} person should pay: ₼ {bill_and_tip}")

# bill_and_tip = tip_percent / 100 * bill + bill
