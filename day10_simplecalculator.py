import os

logo = '''
░█▀▀░█▀█░█░░░█▀▀░█░█░█░░░█▀█░▀█▀░█▀█░█▀▄
░█░░░█▀█░█░░░█░░░█░█░█░░░█▀█░░█░░█░█░█▀▄
░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀
'''
log_table = "CALCULATION: "

def clear_screen():
    os.system("cls")

def header():
    clear_screen()
    print(logo)
    print(log_table)

header()

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def power(n1, n2):
    return n1 ** n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power
}

# ==================== MAIN
exit_prog = False
while exit_prog == False:
    log_table = "CALCULATION: "
    header()
    num1 = float(input("\nType the first number:\n>"))
    log_table += f" {num1}"
    header()

    print("")
    for i in operations:
        print(f"[{i}]")

    selected_operator = input("\nSelect an operation above:\n>")
    log_table += f" {selected_operator}"
    header()

    num2 = float(input("\nType the second number:\n>"))
    log_table += f" {num2}"
    header()

    result = operations[selected_operator](num1, num2)

    proceed = True
    while proceed == True:
        ask_user_to_proceed = ""
        while ask_user_to_proceed != "y" and ask_user_to_proceed != "n":
            log_table = "CALCULATION:"
            log_table += f" {result}"
            header()
            ask_user_to_proceed = input(f"\nDo you what to proceed calculations with {result}? [Y/n]").lower()

            if ask_user_to_proceed == "n":
                proceed = False
            else:            
                header()
                for i in operations:
                    print(f"[{i}]")
                selected_operator = input("\nSelect an operation above:\n>")
                log_table + f" {selected_operator}"
                
                header()
                num3 = float(input("\nType the next number:\n>"))
                result = operations[selected_operator](result, num3)

    ask_user_to_exit = ""
    while ask_user_to_exit != "y" and ask_user_to_exit != "n":
        ask_user_to_exit = input("\nDo you want to restart the calculation? [Y/n]").lower()

    if ask_user_to_exit == "n":
        exit_prog = True
    else:
        exit_prog = False                