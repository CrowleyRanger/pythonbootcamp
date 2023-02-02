import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def ask_user():
    user_input = input("Convert to NATO phonetic: ").upper()
    try:
        result = [nato_phonetic_dict[char] for char in user_input]
    except KeyError:
        print("Please, type only letters.")
        ask_user()
    else:
     print(result)

ask_user()

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
