import os


def bmi_ibw_calculator():
    title()
    height_in_centimeters = float(input("Enter your height in centimeters: "))
    weight_in_kilograms = float(input("Enter your weight in kilograms: "))

    height_in_inches = height_in_centimeters / 2.54
    weight_in_pounds = weight_in_kilograms * 2.20462262
    bmi = weight_in_pounds / (height_in_inches ** 2) * 703
    ideal_weight = 50 + 2.3 * (height_in_inches - 60)
    lose_weight = weight_in_kilograms - ideal_weight

    if bmi < 16:
        print(f"Your BMI: {round(bmi, 2)}, Classification - Severe Thinness")
    elif bmi < 17:
        print(f"Your BMI: {round(bmi, 2)}, Classification - Moderate Thinness")
    elif bmi < 18.5:
        print(f"Your BMI: {round(bmi, 2)}, Classification - Mild Thinness")
    elif bmi < 25:
        print(f"Your BMI: {round(bmi, 2)}, Classification - Normal")
    elif bmi < 30:
        print(f"Your BMI: {round(bmi, 2)}, Classification - Overweight")
    elif bmi < 35:
        print(f"Your BMI: {round(bmi, 2)}, Classification - Obese Class I")
    elif bmi < 40:
        print(f"Your BMI: {round(bmi, 2)}, Classification - Obese Class II")
    else:
        print(f"Your BMI: {round(bmi, 2)}, Classification - Obese Class III")

    print(f"Your IBW: {round(ideal_weight, 2)} kg")
    print(f"You need to lose: {round(lose_weight, 2)} kg")

    execute()


def execute():
    while True:
        question = input("Continue (Y/N): ")
        if question not in {"y", "n"}:
            print("Enter valid input.")
            return execute()
        elif question == "y":
            return bmi_ibw_calculator()
        elif question == "n":
            print("Terminating program...")
            return
        return bmi_ibw_calculator()


def title():
    text = """
╔══╗ ╔═╗╔═╗╔══╗    ╔═══╗╔═╗ ╔╗╔═══╗    ╔══╗╔══╗ ╔╗╔╗╔╗    ╔═══╗╔═══╗╔╗   ╔═══╗╔╗ ╔╗╔╗   ╔═══╗╔════╗╔═══╗╔═══╗
║╔╗║ ║║╚╝║║╚╣╠╝    ║╔═╗║║║╚╗║║╚╗╔╗║    ╚╣╠╝║╔╗║ ║║║║║║    ║╔═╗║║╔═╗║║║   ║╔═╗║║║ ║║║║   ║╔═╗║║╔╗╔╗║║╔═╗║║╔═╗║
║╚╝╚╗║╔╗╔╗║ ║║     ║║ ║║║╔╗╚╝║ ║║║║     ║║ ║╚╝╚╗║║║║║║    ║║ ╚╝║║ ║║║║   ║║ ╚╝║║ ║║║║   ║║ ║║╚╝║║╚╝║║ ║║║╚═╝║
║╔═╗║║║║║║║ ║║     ║╚═╝║║║╚╗║║ ║║║║     ║║ ║╔═╗║║╚╝╚╝║    ║║ ╔╗║╚═╝║║║ ╔╗║║ ╔╗║║ ║║║║ ╔╗║╚═╝║  ║║  ║║ ║║║╔╗╔╝
║╚═╝║║║║║║║╔╣╠╗    ║╔═╗║║║ ║║║╔╝╚╝║    ╔╣╠╗║╚═╝║╚╗╔╗╔╝    ║╚═╝║║╔═╗║║╚═╝║║╚═╝║║╚═╝║║╚═╝║║╔═╗║ ╔╝╚╗ ║╚═╝║║║║╚╗
╚═══╝╚╝╚╝╚╝╚══╝    ╚╝ ╚╝╚╝ ╚═╝╚═══╝    ╚══╝╚═══╝ ╚╝╚╝     ╚═══╝╚╝ ╚╝╚═══╝╚═══╝╚═══╝╚═══╝╚╝ ╚╝ ╚══╝ ╚═══╝╚╝╚═╝"""
    print(text)


bmi_ibw_calculator()
