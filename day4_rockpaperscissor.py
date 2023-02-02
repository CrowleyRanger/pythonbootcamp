import random
import time

print("""
================================================
==== Welcome to Rock, Paper, Scissors game! ====
================================================
""")

# ASCII ART

ascii_rock = """> ROCK
    _______
---/   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

ascii_paper = """> PAPER
     _______
---/    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

ascii_scissors = """> SCISSORS
    _______
---/   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# ROCK: 1, PAPER: 2, SCISSORS: 3
respective_choice = {1: ascii_rock, 2: ascii_paper, 3: ascii_scissors}

# ==================== INPUT
user_input = "0"
while True:
    user_input = input("What do you choose?\n[1] Rock\n[2] Paper\n[3] Scissors\n>")
    if user_input == "1" or user_input == "2" or user_input == "3":
        break
user_input = int(user_input)
print("You chose:\n" + respective_choice[user_input])

machine_choosing_message = print("Machine choosing...")
time.sleep(1)

machine_input = random.randint(1, 3)
print("Machine chose:\n" + respective_choice[machine_input])


# ==================== WIN MESSAGES
print_user_win = "\n======== YOU WON! ========\n"
print_machine_win = "\n======== MACHINE WON... ========\n"
print_draw = "\n======== GAME DRAW ========\n"

# ==================== POSSIBLE COMBINATIONS IN WHICH ---> FIRST NUMBER: user input & SECOND NUMBER: machine input
list_user_win = [13, 21, 32]
user_machine_num = user_input*10 + machine_input

# ==================== CHECK WINNER
time.sleep(1)
if user_input != machine_input:
    if user_machine_num in list_user_win:
        print(print_user_win)
    else:
        print(print_machine_win)
else:
    print(print_draw)

