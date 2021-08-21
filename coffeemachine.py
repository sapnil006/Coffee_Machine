MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "cost": 1.5,
        },

    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
            "cost": 2.5,
        },

    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
            "cost": 3.0,
        },

    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money": 0.00,
}
# print(type(MENU["latte"]["ingredients"]["cost"]))

# TODO: 5. Process coins.


def process_coins():
    print("please insert coins")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickle = int(input("how many nickels?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    total = quarters + dimes + nickle + pennies
    return total

# TODO: 6. Check transaction successful?


def transaction_checker():
    your_price = process_coins()
    if your_price > MENU[choice]["ingredients"]["cost"]:
        change = your_price - MENU[choice]["ingredients"]["cost"]
        your_change = round(change, 2)
        print(f"your change: ${your_change}")
        resources["Money"] = resources["Money"] + MENU[choice]["ingredients"]["cost"]
    elif your_price == MENU[choice]["ingredients"]["cost"]:
        print("Thank You,Visit again!")
        resources["Money"] = resources["Money"] + MENU[choice]["ingredients"]["cost"]
    else:
        print("refunded")
        exit()


while 1:
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

    choice = input("What would you like? (espresso/latte/cappuccino):")

    # TODO: 3. Print report.

    def report():

        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"Money: ${resources['Money']}")


    def resource_checker():

        if choice == 'espresso':
            if resources["water"] >= 50 and resources["coffee"] >= 18:
                transaction_checker()
                resources["water"] = resources["water"] - 50
                resources["coffee"] = resources["coffee"] - 18
                print(f"Here is your {choice} ")

            else:
                print("sorry,stock not available")
        elif choice == 'cappuccino':
            if resources["water"] >= 250 and resources["coffee"] >= 24 and resources["milk"] >= 100:
                transaction_checker()
                resources["water"] = resources["water"] - 250
                resources["coffee"] = resources["coffee"] - 24
                resources["milk"] = resources["milk"] - 100
                print(f"Here is your {choice} ")

            else:
                print("sorry,not available")
        elif choice == 'latte':
            if resources["water"] >= 100 and resources["coffee"] >= 24 and resources["milk"] >= 150:
                transaction_checker()
                resources["water"] = resources["water"] - 100
                resources["coffee"] = resources["coffee"] - 24
                resources["milk"] = resources["milk"] - 150
                print(f"Here is your {choice} ")

            else:
                print("sorry,not available")
        elif choice == 'report':
            report()
        # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
        elif choice == "off":
            exit()
    resource_checker()
# TODO: 7. Make Coffee.
