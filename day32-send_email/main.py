import smtplib
import os
import pandas as pd
import random
from datetime import datetime

EMAIL = "python.test1610@gmail.com"
PASSWORD = "tantalusdrive"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]):data_row for (index, data_row) in data.iterrows()}

# if today_tuple in birthdays_dict:
if today_tuple in birthdays_dict:
    person_name = birthdays_dict[today_tuple]["name"]
    person_email = birthdays_dict[today_tuple]["email"]

    #Select random message text
    files = os.listdir("letter_templates")
    rand_index = random.randrange(0, len(files))
    rand_letter = files[rand_index]

    with open(f"letter_templates/{rand_letter}", "r+") as letters_file:
        letter = letters_file.read()
        with open(f"new_letters/letter_for_{person_name}.txt", "w+") as new_file:
            new_file.truncate(0)
            letter = letter.replace("[NAME]", person_name)
            new_file.write(letter)
            print("SENT E-MAIL:\n\n", letter)

# with smtplib.SMTP("smtp.gmail.mail") as connection:
#     connection.starttls()
#     connection.login(EMAIL, PASSWORD)
#     connection.sendemail(
#         from_addr=EMAIL,
#         to_addrs="xpace1610@gmail.com",
#         msg=f"Subject:Happy Birthday!\n\n{letter}"
#     )