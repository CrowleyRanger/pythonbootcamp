import os
import math

string_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def clear_screen():
    os.system("cls")

def header():
    clear_screen()
    print('''
============================
======== BID WINNER ========
============================
''')

bidders = {}
repeat = True

while repeat == True:
    header()
    user_name = input("Type your name?\n>")

    only_numbers = False
    while only_numbers == False:
        only_numbers = True
        header()
        user_bid = input("Type your bid:\n>")
        for i in user_bid:
            if i not in string_numbers:
                only_numbers = False
    user_bid = int(user_bid)

    bidders[user_name] = user_bid

    there_is_another_user = ""
    while there_is_another_user != "y" and there_is_another_user != "n":
        header()
        there_is_another_user = input("Is there another user? [Y/n]\n>").lower()
        if there_is_another_user == "y":
            continue
        else:
            repeat = False
clear_screen()

bids = []
for name in bidders:
    bids.append(bidders[name])

greater_bid_position = bids.index(max(bids))

winner = list(bidders)[greater_bid_position]

header()
print(f"\nThe winner is {winner}!\n")
    

