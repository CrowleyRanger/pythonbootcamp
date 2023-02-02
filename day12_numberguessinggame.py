import os
import random

def clear_screen():
    os.system("cls")

def header():
    clear_screen()
    print("========== GUESS A NUMBER ==========\n")
    print(f"LIFES: {life}")
    print(f"STATUS: {status}\n")

# ==================== DIFFICULTY
difficulty_chosen = ""
while difficulty_chosen != "1" and difficulty_chosen != "2":
    clear_screen()
    print("========== GUESS A NUMBER ==========\n")
    difficulty_chosen = input("Select a difficulty:\n[1] Easy\n[2] Hard\n>").lower()
    if difficulty_chosen == "1":
        life = 10
    elif difficulty_chosen == "2":
        life = 5

# ==================== RANDOM NUMBER
random_number = random.randint(0, 100)

# ==================== MAIN
status = "Welcome!"
guess = 101
while guess != random_number:
    header()
    guess = int(input("Guess a integer number between 0 - 100:\n>"))

    if life == 0:
        status = R"You're out of lifes..."
        header()
        print("... YOU LOST ...\n")
    elif guess == random_number:
        status = f"{guess} is the right word!"
        header()
        print("!!! YOU WON !!!\n")
    else:
        life -= 1
        if guess > random_number:
            status = f"{guess} is too high!"
            header()
        elif guess < random_number:
            clear_screen()
            status = f"{guess} is to low!"
            header()