def bill_calculator():
    title()
    bill = float(input("Enter the total bill: "))
    tip = int(input("Enter the tip: "))
    people = int(input("Enter people count to split the bill: "))

    bill_split = (bill + tip) / people

    print(f"The split bill between {people} person: {round(bill_split, 2)}")
    execute()


def execute():
    while True:
        question = input("Continue (Y/N): ")
        if question not in {"y", "n"}:
            print("Enter valid input.")
            return execute()
        elif question == "y":
            return bill_calculator()
        elif question == "n":
            print("Terminating program...")
            return
        return bill_calculator()


def title():
    text = """
╔══╗ ╔══╗╔╗   ╔╗       ╔═══╗╔═══╗╔╗   ╔═══╗╔╗ ╔╗╔╗   ╔═══╗╔════╗╔═══╗╔═══╗
║╔╗║ ╚╣╠╝║║   ║║       ║╔═╗║║╔═╗║║║   ║╔═╗║║║ ║║║║   ║╔═╗║║╔╗╔╗║║╔═╗║║╔═╗║
║╚╝╚╗ ║║ ║║   ║║       ║║ ╚╝║║ ║║║║   ║║ ╚╝║║ ║║║║   ║║ ║║╚╝║║╚╝║║ ║║║╚═╝║
║╔═╗║ ║║ ║║ ╔╗║║ ╔╗    ║║ ╔╗║╚═╝║║║ ╔╗║║ ╔╗║║ ║║║║ ╔╗║╚═╝║  ║║  ║║ ║║║╔╗╔╝
║╚═╝║╔╣╠╗║╚═╝║║╚═╝║    ║╚═╝║║╔═╗║║╚═╝║║╚═╝║║╚═╝║║╚═╝║║╔═╗║ ╔╝╚╗ ║╚═╝║║║║╚╗
╚═══╝╚══╝╚═══╝╚═══╝    ╚═══╝╚╝ ╚╝╚═══╝╚═══╝╚═══╝╚═══╝╚╝ ╚╝ ╚══╝ ╚═══╝╚╝╚═╝"""
    print(text)


bill_calculator()
