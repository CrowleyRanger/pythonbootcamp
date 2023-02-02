import os
import animation
from resources import MENU
from resources import resources


# ==================== DEFAULT RESOURCES ==================== #
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 10.00

def coffee_machine():
    return f'''
        /~~~~~~~~/|
       / /######/ / |
      / /______/ /  |   🔵 WATER = {water}ml
     ============ /||   ⚪ MILK = {milk}ml
     |__________|/ ||   🟤 COFFEE = {coffee}g
      |\__,,__/    ||
      | __,,__     ||
      |_\====/%____||
      | /~~~~\ %  / |   💵 MONEY = ${money}
     _|/      \%_/  |
    | |        | | /
    |__\______/__|/
    ~~~~~~~~~~~~~~
    '''

# ==================== FUNCTIONS ==================== #
def clear_screen():
    os.system("cls")

def water_cost(drink):
    return MENU[drink]["ingredients"]["water"]
def milk_cost(drink):
    return MENU[drink]["ingredients"]["milk"]
def coffee_cost(drink):
    return MENU[drink]["ingredients"]["coffee"]
def money_cost(drink):
    return MENU[drink]["cost"]

def drink_affordable(drink):
    if water >= water_cost(drink) and milk >= milk_cost(drink) and coffee >= coffee_cost(drink) and money >= money_cost(drink):
        return True
    return False
def consume_resource(drink):
    global water
    water -= water_cost(drink)
    global milk
    milk -= milk_cost(drink)
    global coffee
    coffee -= coffee_cost(drink)
    global money
    money -= money_cost(drink)

# ==================== PRESS A BUTTON(MAIN) ==================== #
buttons = ["1", "2", "3", "off", "report"]
button_pressed = None
machine_pwr = True
clear_screen()
while machine_pwr == True:
    button_pressed = None
    while button_pressed not in buttons:
        clear_screen()
        print(coffee_machine())
        button_pressed = input("What would you like?\n[1] Espresso\n[2] Latte\n[3] Cappuccino\n>").lower()

    if button_pressed == "off":
        machine_pwr = False

    if button_pressed == "report":
        print(f'''
    Water: {water}ml
    Milk: {milk}ml
    Coffee: {coffee}g
    Money: ${money}
        ''')

    if button_pressed == "1":
        if drink_affordable("espresso") == True:
            consume_resource("espresso")
            animation.filling_cup_animation()
            print("Here's you espresso!: ☕")
        else:
            print("Not enough resources...")
    elif button_pressed == "2":
        if drink_affordable("latte") == True:
            consume_resource("latte")
            animation.filling_cup_animation()
            print("Here's you latte!: ☕")
        else:
            print("Not enough resources...")
    elif button_pressed == "3":
        if drink_affordable("cappuccino") == True:
            consume_resource("cappuccino")
            animation.filling_cup_animation()
            print("Here's you cappuccino!: ☕")
        else:
            print("Not enough resources...")
    
    ask_user_to_power_off = input("\nTurn off machine? [Y/n]").lower()
    if ask_user_to_power_off == "y":
        machine_pwr = False

