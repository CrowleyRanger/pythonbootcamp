import smtplib
import random
import datetime as dt

EMAIL = "python.test1610@gmail.com"
PASSWORD = "tantalusdrive"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:

    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
        rand_quote = random.choice(quotes)
        print(rand_quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Monday Motivation\n\n{rand_quote}"
        )