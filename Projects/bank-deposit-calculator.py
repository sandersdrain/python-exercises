def deposit_calculator():
    title()
    amount = float(input("Enter the amount(₼): "))
    percent = float(input("Enter the percent(%): "))
    month = int(input("Enter the month(months): "))

    gross_interest_income = amount * percent / 100
    monthly_interest_income = gross_interest_income / month
    tax = monthly_interest_income * 10 / 100

    print(f"Gross interest income: {round(gross_interest_income, 2)}")
    print(f"Monthly interest income: {round(monthly_interest_income, 2) - round(tax, 2)}")
    execute()


def execute():
    while True:
        question = input("Continue (Y/N): ")
        if question not in {"y", "n"}:
            print("Enter valid input.")
            return execute()
        elif question == "y":
            return deposit_calculator()
        elif question == "n":
            print("Terminating program...")
            return
        return deposit_calculator()


def title():
    text = """
╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔══╗╔════╗    ╔═══╗╔═══╗╔╗   ╔═══╗╔╗ ╔╗╔╗   ╔═══╗╔════╗╔═══╗╔═══╗
╚╗╔╗║║╔══╝║╔═╗║║╔═╗║║╔═╗║╚╣╠╝║╔╗╔╗║    ║╔═╗║║╔═╗║║║   ║╔═╗║║║ ║║║║   ║╔═╗║║╔╗╔╗║║╔═╗║║╔═╗║
 ║║║║║╚══╗║╚═╝║║║ ║║║╚══╗ ║║ ╚╝║║╚╝    ║║ ╚╝║║ ║║║║   ║║ ╚╝║║ ║║║║   ║║ ║║╚╝║║╚╝║║ ║║║╚═╝║
 ║║║║║╔══╝║╔══╝║║ ║║╚══╗║ ║║   ║║      ║║ ╔╗║╚═╝║║║ ╔╗║║ ╔╗║║ ║║║║ ╔╗║╚═╝║  ║║  ║║ ║║║╔╗╔╝
╔╝╚╝║║╚══╗║║   ║╚═╝║║╚═╝║╔╣╠╗ ╔╝╚╗     ║╚═╝║║╔═╗║║╚═╝║║╚═╝║║╚═╝║║╚═╝║║╔═╗║ ╔╝╚╗ ║╚═╝║║║║╚╗
╚═══╝╚═══╝╚╝   ╚═══╝╚═══╝╚══╝ ╚══╝     ╚═══╝╚╝ ╚╝╚═══╝╚═══╝╚═══╝╚═══╝╚╝ ╚╝ ╚══╝ ╚═══╝╚╝╚═╝
"""
    print(text)


deposit_calculator()
