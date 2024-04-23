# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = weight / height ** 2
ideal_weight = 106 + (height - 60) * 6

if bmi < 16:
    print(f"Your BMI is {round(bmi, 2)}, Classification - Severe Thinness")
elif bmi < 17:
    print(f"Your BMI is {round(bmi, 2)}, Classification - Moderate Thinness")
elif bmi < 18.5:
    print(f"Your BMI is {round(bmi, 2)}, Classification - Mild Thinness")
elif bmi < 25:
    print(f"Your BMI is {round(bmi, 2)}, Classification - Normal")
elif bmi < 30:
    print(f"Your BMI is {round(bmi, 2)}, Classification - Overweight")
elif bmi < 35:
    print(f"Your BMI is {round(bmi, 2)}, Classification - Obese Class I")
elif bmi < 40:
    print(f"Your BMI is {round(bmi, 2)}, Classification - Obese Class II")
    print(f"Your IBW is {round(ideal_weight, 2)}")
else:
    print(f"Your BMI is {round(bmi, 2)}, Classification - Obese Class III")
