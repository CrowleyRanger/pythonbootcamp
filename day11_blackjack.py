import os
import random
import blackjack_module

# ==================== DECLARATIONS ==================== #
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_status = ""

# ==================== FUNCTIONS ==================== #
def clear_screen():
    os.system("cls")

def sum_cards(cards):
    sum = 0
    for card in cards:
        sum += card
    return sum

def random_card():
    rand_card = random.choice(cards)
    return rand_card

def score(cards):
    score = sum_cards(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    if score == 21 and len(cards) == 2:
        return 0
    return score

def header():
    clear_screen()
    print(blackjack_module.logo)

def hands_status():
    user_hand_status = f"YOUR HAND ....... {user_hand} ---> SCORE: {score(user_hand)}"
    machine_hand_status = f"MACHINE HAND .... {false_machine_hand} ---> SCORE: ?"
    print(user_hand_status)
    print(machine_hand_status)

def check_busted():
    global new_card_loop
    global game_status

    if score(user_hand) == score(machine_hand) and score(user_hand) > 21:
        game_status = blackjack_module.message_draw
        new_card_loop = False

    elif score(user_hand) > 21:
        game_status = blackjack_module.message_busted
        new_card_loop = False

    elif score(machine_hand) > 21:
        game_status = blackjack_module.message_machine_busted
        new_card_loop = False
    
# ==================== MAIN ==================== #
exit_game = False
while exit_game == False:

    user_hand = []
    machine_hand = []
    false_machine_hand = []

    for _ in range(2):
        user_hand.append(random_card())
        machine_hand.append(random_card())
    false_machine_hand.append(machine_hand[0])
    false_machine_hand.append("?")

    # Check if blackjack is working
    #user_hand = [11, 10]
    #machine_hand = [11, 10]

    new_card_loop = True

# Check blackjack
    if score(user_hand) == 0:
        game_status = blackjack_module.message_blackjack_you_won
        new_card_loop = False

    elif score(machine_hand) == 0:
        game_status = blackjack_module.message_blackjack_you_lost
        new_card_loop = False

# If busted, the game ends here.
    check_busted()

    while new_card_loop == True:
        header()
        hands_status()
        
        add_new_card = input("\nAdd a new card? [Y/n]").lower()
        if add_new_card == "y":
            user_hand.append(random_card())
            machine_hand.append(random_card())
            false_machine_hand.append("?")
            check_busted()
        else:
            new_card_loop = False
            
            if score(user_hand) == score(machine_hand):
                game_status = blackjack_module.message_draw

            elif score(user_hand) > 21:
                game_status = blackjack_module.message_busted

            elif score(machine_hand) > 21:
                game_status = blackjack_module.message_machine_busted

            elif score(user_hand) > score(machine_hand):
                game_status = blackjack_module.message_you_won

            elif score(user_hand) < score(machine_hand):
                game_status = blackjack_module.message_you_lost

    header()
    user_hand_status = f"YOUR HAND ....... {user_hand} ---> SCORE: {score(user_hand)}"
    machine_hand_status = f"MACHINE HAND .... {machine_hand} ---> SCORE: {score(machine_hand)}"
    print(user_hand_status)
    print(machine_hand_status)
    print(game_status)
    ask_user_to_exit = input("\nDo you want to exit? [Y/n]").lower()
    if ask_user_to_exit == "y":
        exit_game = True
    else:
        exit_game = False

