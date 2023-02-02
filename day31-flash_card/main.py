from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
DARK_BACKGROUND_COLOR = "#91C2AF"
FONT = "Arial"

try:
    data = pd.read_csv("data/to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    data.to_csv("data/to_learn.csv")
    data = pd.read_csv("data/to_learn.csv")

to_learn = data.to_dict(orient="records")
random_word_num = random.randint(0, len(data))

# Starting flashcard language
language = "French"
current_card = random.choice(to_learn)

# ------------------------- FUNCTIONS ------------------------- #
def switch():
    flashcard_button.config(image=flashcard_config[language]["image"])
    label_lang.config(text=language, bg=flashcard_config[language]["bg"])
    label_word.config(text=current_card[language], bg=flashcard_config[language]["bg"])

def translate():
    global language
    if language == "French":
        language = "English"
    else:
        language = "French"
    switch()

def next_word():
    global current_card, language
    language = "French"
    current_card = random.choice(to_learn)
    switch()

def remove_word():
    data = pd.DataFrame(to_learn)
    to_learn.remove(current_card)
    data.to_csv("data/to_learn.csv", index=False)

    next_word()

# ------------------------- UI ------------------------- #
window = Tk()
window.minsize(width=600, height=600)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

#Images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

#Config
flashcard_config = {
    "French": {
        "image": card_front_img,
        "bg": "white",
        "word": data[language][random_word_num]
    },
    "English": {
        "image": card_back_img,
        "bg": DARK_BACKGROUND_COLOR,
        "word": data[language][random_word_num]
    }
}

#Buttons
flashcard_button = Button(image=card_front_img, highlightthickness=0, command=translate, bd=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR)
flashcard_button.grid(column=0, row=0, columnspan=2)

right_button = Button(image=right_img, command=remove_word, highlightthickness=0, bd=0, activebackground=BACKGROUND_COLOR)
right_button.grid(column=0, row=1)

wrong_button = Button(image=wrong_img, command=next_word, highlightthickness=0, bd=0, activebackground=BACKGROUND_COLOR)
wrong_button.grid(column=1, row=1)

#Labels
label_lang = Label(text=language, font=(FONT, 24, "italic"), bg="white")
label_lang.place(x=400, y=150, anchor="center", )

label_word = Label(text=current_card[language], font=(FONT, 48, "bold"), bg="white")
label_word.place(x=400, y=260, anchor="center")

window.mainloop()