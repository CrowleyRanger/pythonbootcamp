import random
import hangman_module
import os
 
def clear_screen():
    os.system('cls')

play_again = True
while play_again == True:

    clear_screen()

    random_name = random.choice(hangman_module.wordlist)

    display = []
    guessed_letters = []
    for letter in range(0, len(random_name)):
        display += "_"

    life = 6
    info = "Welcome!"

    print(hangman_module.mass_effect_hangman)
    print("INFO:", info)
    print("\n\n")
    print("".join(display))
    print(f"\n{hangman_module.life_stage[life]}\n")

    while True:
        guess = input("Guess a letter in the name of a random Mass Effect's crew member:\n> ").lower()

        if guess not in guessed_letters:
            guessed_letters.append(guess)

        clear_screen()

        if guess in display:
            info = f"You already guessed '{guess}'..."

        for position in range(len(random_name)):
            letter = random_name[position]
            if letter == guess:
                display[position] = letter

        if "_" not in display:
            print("\n====== YOU WON! ======\n")
            print(f"Expected name: {''.join(random_name).upper()}\n")
            break

        if guess not in random_name:
            life -= 1
            if life == 0:
                print("\n====== YOU LOST ======\n")
                print(f"Expected name: {''.join(random_name).upper()}\n")
                break
            else:
                info = f"'{guess}' is a wrong letter..."

        print(hangman_module.mass_effect_hangman)
        print("INFO:", info)
        print(f"GUESSED LETTERS: {', '.join(guessed_letters)}")
        print("\n")
        print("".join(display))
        print(f"\n{hangman_module.life_stage[life]}\n")

    ask_user_to_play_again = input("Play again? [Y/n]").lower()
    if ask_user_to_play_again == "y":
        continue
    else:
        play_again = False