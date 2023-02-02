from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

BLUE = "#2b2e4a"
ORANGE = "#e84545"
PINK = "#903749"
PURPLE = "#53354a"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    global generate_password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    psw_letters = [choice(letters) for letter in range(0, nr_letters)]
    psw_symbols = [choice(symbols) for symbol in range(0, nr_symbols)]
    psw_numbers = [choice(numbers) for number in range(0, nr_numbers)]

    password_list = psw_letters + psw_numbers + psw_symbols
    shuffle(password_list)

    generated_password = "".join(password_list)

    pyperclip.copy(generated_password)

    entry_psw.delete(0, END)
    entry_psw.insert(0, generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_new_psw():

    website = entry_website.get()
    email = entry_email.get()
    password = entry_psw.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Not saved", message="Please, fill all blank spaces.")
    else:
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"""Is that correct?

Website Name: {website}
E-mail: {email}
Password: {password}
        """)

        if is_ok:
            try:
                with open("save.json", "r") as open_file:
                    #Reading old data
                    data = json.load(open_file)
            except FileNotFoundError:
                with open("save.json", "w") as open_file:
                    #Saving updated data
                    json.dump(new_data, open_file, indent=4)
            else:
                #Updating old data with new data
                data.update(new_data)    

                with open("save.json", "w") as open_file:
                    #Saving updated data
                    json.dump(data, open_file, indent=4)
            finally:
                entry_website.delete(0, END)
                entry_email.delete(0, END)
                entry_psw.delete(0, END)

# ---------------------------- SEARCH DATA ------------------------------- #
def search_data():
    website_searched = entry_website.get()

    try:
        with open("save.json", "r") as open_file:
            data = json.load(open_file)
            data_found = ""
            for website_found in data:
                if website_searched == website_found:
                    found_email = data[f"{website_searched}"]["email"]
                    found_password = data[f"{website_searched}"]["password"]
                    data_found += f"\nE-mail: {found_email}\nPassword: {found_password}"


            messagebox.showinfo(title="Success!", message=data_found)

    except (KeyError, FileNotFoundError):
        messagebox.showerror(title="Error", message=f"'{website_searched}' not found...")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass: Password Manager")
window.config(padx=30, pady=30, bg=BLUE)
window.resizable(0, 0)

#Image
canvas = Canvas(width=200, height=200, bg=BLUE, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

#Labels
text_website = Label(text="Website Name:", bg=BLUE, fg=ORANGE)
text_website.grid(column=0, row=1, sticky="e")

text_email = Label(text="Email/Username:", bg=BLUE, fg=ORANGE)
text_email.grid(column=0, row=2, sticky="e")

text_psw = Label(text="Password:", bg=BLUE, fg=ORANGE)
text_psw.grid(column=0, row=3, sticky="e")

#Entries
entry_website = Entry(width=34, bg=PURPLE, fg="white")
entry_website.grid(column=1, row=1, columnspan=2, sticky="w", pady=2)
entry_website.focus()

entry_email = Entry(width=55, bg=PURPLE, fg="white")
entry_email.grid(column=1, row=2, columnspan=2, sticky="w", pady=2)

entry_psw = Entry(width=34, bg=PURPLE, fg="white")
entry_psw.grid(column=1, row=3, sticky="w", pady=2)

#Buttons
button_search = Button(text="Search", width=16, bg=ORANGE, activebackground=PINK, command=search_data)
button_search.grid(column=2, row= 1,columnspan=3, sticky="w")

button_psw_gen = Button(text="Generate Password", width=16, bg=ORANGE, activebackground=PINK, command=generate_password)
button_psw_gen.grid(column=2, row= 3,columnspan=3, sticky="w")

button_add = Button(text="Add", width=46, bg=ORANGE, activebackground=PINK, command=save_new_psw)
button_add.grid(column=1, row=4, columnspan=2, sticky="EW", pady=2)

window.mainloop()