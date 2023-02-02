import os

logo = '''
  _____                              _____ _       _               
 / ____|                            / ____(_)     | |              
| |     __ _  ___  ___  __ _ _ __  | |     _ _ __ | |__   ___ _ __ 
| |    / _` |/ _ \/ __|/ _` | '__| | |    | | '_ \| '_ \ / _ \ '__|
| |___| (_| |  __/\__ \ (_| | |    | |____| | |_) | | | |  __/ |   
 \_____\__,_|\___||___/\__,_|_|     \_____|_| .__/|_| |_|\___|_|   
                                            | |                    
                                            |_|           
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
string_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def clear_screen():
    os.system("cls")

def header():
    clear_screen()
    print(logo)

def caesar_cipher(text, shift, option):
    global crypt
    crypt = ""

    # DEFAULT: encrypt
    if option == "decrypt":
        shift = - shift

    for position in range(len(text)):
        letter = text[position]
        letter_alphabet_position = alphabet.index(letter)
        shifted_letter_alphabet_position = letter_alphabet_position + shift

        # alphabet loop
        if abs(shifted_letter_alphabet_position) >= len(alphabet): # Not > 26 because position starts at 0!
           shifted_letter_alphabet_position = shifted_letter_alphabet_position % len(alphabet)

        shifted_letter = alphabet[shifted_letter_alphabet_position]
        crypt += shifted_letter
    return crypt

# ==================== THREAD
while True:
# ==================== OPTION LOOP
    direction = ""
    while direction != "1" and direction != "2":
        header()
        direction = input("What do you want to do?\n1. Encrypt\n2. Decrypt\n>")

# ==================== TEXT LOOP
    only_letters = False
    alert_message = False
    while only_letters == False:
        only_letters = True 
        header()

        if alert_message == True:
            print("[!] Please, only type letters.")

        text = input("Type your message:\n>").lower()

        for i in text:
            if i not in alphabet:
                only_letters = False
                alert_message = True

# ==================== SHIFT LOOP
    only_numbers = False
    while only_numbers == False:
        only_numbers = True
        header()
        shift = input("Type the shift number:\n>")
        for i in shift:
            if i not in string_numbers:
                only_numbers = False
    shift = int(shift)

# ==================== ENCRYPTION/DECRYPTION
    if direction == "1":
        header()
        caesar_cipher(text, shift, "encrypt")
    elif direction == "2":
        header()
        caesar_cipher(text, shift, "decrypt")

# ==================== ASK TO EXIT LOOP
    exit_program = ""
    while exit_program != "y" and exit_program != "n":
        if direction == "1":
            header()
            print(f"======== ENCRYPTED: {crypt} ========")
            exit_program = input("\nExit program? [Y/n]").lower()
            if exit_program == "y":
                break
        elif direction == "2":
            header()
            print(f"======== DECRYPTED: {crypt} ========")
            exit_program = input("\nExit program? [Y/n]").lower()
            if exit_program == "y":
                break
    if exit_program == "y":
        break

    clear_screen()