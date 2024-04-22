age = input("Enter your age: ")

# 🚨 Don't change the code above 👆
# Write your code below this line 👇

life_expectancy = 90 * 52.1428571

current_weeks = int(age) * 52.1428571

weeks_left = round(life_expectancy - current_weeks)

print(f"You have {weeks_left} weeks left.")
