from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


menu_available = menu.get_items()
print(f"What would you like :{menu_available}: ")
choice = input("Enter your drink: ")
your_drink = menu.find_drink(choice)


coffee_maker.report()
if coffee_maker.is_resource_sufficient(your_drink):
    if money_machine.make_payment(your_drink.cost):
        coffee_maker.make_coffee(your_drink)

