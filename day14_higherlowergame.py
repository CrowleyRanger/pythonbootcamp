import os
import random
import time
import day14_higherlowergame_data as data

def clear_screen():
    os.system("cls")

score = 0
exit_game = False

person1 = random.choice(data.data)
person2 = random.choice(data.data)

# ==================== If both names are the same
while person1 == person2:
    person2 = random.choice(data.data)

while exit_game == False:

    run_game = True
    while run_game == True:
        clear_screen()
        print(f'''
[1] >>> {person1["name"].upper()}: {person1["description"].lower()}, from {person1["country"]}
=============================
[2] >>> {person2["name"].upper()}: {person2["description"].lower()}, from {person2["country"]}

SCORE = {score}
        ''')

        user_answer = ""
        while user_answer != "1" and user_answer != "2":
            user_answer = input("Who has more followers on instagram? [1/2]\n>")

        if user_answer == "1" and person1["follower_count"] > person2["follower_count"]:
            print("CORRECT")
            score += 1
            person2 = random.choice(data.data)
            time.sleep(1)
        elif user_answer == "1" and person1["follower_count"] < person2["follower_count"]:
            print("INCORRECT")
            run_game = False

        elif user_answer == "2" and person1["follower_count"] < person2["follower_count"]:
            print("CORRECT")
            score += 1
            person1 = person2
            person2 = random.choice(data.data)
            time.sleep(1)
        elif user_answer == "2" and person1["follower_count"] > person2["follower_count"]:
            print(f"INCORRECT")
            run_game = False

    ask_user_to_replay = input("Play again? [Y/n]").lower()
    if ask_user_to_replay == "y":
        person1 = random.choice(data.data)
        person2 = random.choice(data.data)
        score = 0
        run_game = True
    else:
        exit_game = True

    
