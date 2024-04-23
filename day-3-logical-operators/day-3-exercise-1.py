# Which number do you want to check?
number = int(input("Enter a number: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
result = number / 2
if result % 1 == 0:
    print(f"{result} even number!")
else:
    print(f"{result} odd number!")
