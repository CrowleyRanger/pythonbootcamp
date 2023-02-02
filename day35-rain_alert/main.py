import requests
import os
from twilio.rest import Client

API_KEY = "7a25b9c558785a8bb5f6656a9a384436"
TWILIO_ACCOUNT_SID = "ACb102dde10d045365c46e4374e71582ac"
TWILIO_AUTH_TOKEN = "b02a4d41e966a5ecce920d1389b4d703"
SP_LAT = -23.550520
SP_LON = -46.633308

parameters = {
    "lat": -30.879520,
    "lon": -53.441640,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
    "hourly.dt": 12
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall?", params=parameters)
response.raise_for_status()

weather_data = response.json()

weather_12_hour = weather_data["hourly"][:13]
weather_id_list = [weather_12_hour[hour]["weather"][0]["id"] for hour in range(0, len(weather_12_hour))]

rain_hours = []
will_rain = False
for id in weather_id_list:
    if id < 600:
        will_rain = True

if will_rain == False:
    print("It's not going to rain in the next 12 hours!")
else:
    #Prints only the next rain hour
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    print(f"It's going to rain within 12 hours, bring an umbrella!")

    message = client.messages \
                    .create(
                        body=f"It's going to rain within 12 hours, bring an umbrella!",
                        from_='+14243533343',
                        to='+5511972096011'
                    )

    print(message.status)