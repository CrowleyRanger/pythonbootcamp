from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What do you want? [{options}]")
    drink = menu.find_drink(choice)
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            money_machine.process_coins()
            coffe_maker.make_coffee(drink)