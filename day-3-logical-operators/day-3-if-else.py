print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm: "))

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Pay $12.")
    elif age >= 12:
        print("Pay $7.")
    else:
        print("Pay $5")
else:
    print("You can't ride the rollercoaster.")
