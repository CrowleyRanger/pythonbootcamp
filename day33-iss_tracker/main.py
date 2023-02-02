import requests
import time
from smtplib import SMTP
from datetime import date, datetime
from os import system

SENDER_EMAIL = "python.text1610@gmail.com"
SENDER_PASSWORD = "tantalusdrive"

MY_LAT = -23.563350
MY_LNG = -46.642140

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

def iss_is_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()["iss_position"]
    iss_longitude = data["longitude"]
    iss_latitude = data["latitude"]

    if MY_LAT+5 >= iss_latitude >= MY_LAT-5 and MY_LNG+5 >= iss_longitude >= MY_LNG-5:
        return True

def is_night():

    response = requests.get(f"https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0:2]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0:2]

    #UTC -3h : Sao Paulo
    sunrise[0] = str(int(sunrise[0]) - 3)
    sunset[0] = str(int(sunset[0]) - 3)
    print(sunrise)
    print(sunset)

    time_now_list = str(datetime.now()).split(" ")[1].split(":")[0:2]
    print(time_now_list)

    if time_now_list >= sunset or time_now_list <= sunrise:
        return True
while True:
    time.sleep(60)
    if iss_is_overhead == True and is_night == True:
        print("Look at the sky! ISS is orbiting over your area!")
        
        connection = SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(SENDER_EMAIL, SENDER_PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=SENDER_EMAIL,
            msg="Subject:Look at the sky!\n\nISS is orbiting over your area!"
        )