from datetime import datetime
import requests

APP_KEY = "00dfc9b4d90368349690cf0dc7ec896b"
APP_ID = "6ca248e7"

app_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/23ed44e12fb58ca763b1858ab49312e5/workouts/workouts"

user_input = input("Which exercises you did today?")

parameters = {
    "query": user_input,
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 185,
    "age": 19

}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

response = requests.post(url=app_endpoint, headers=headers, json=parameters)
result = response.json()

for exercise in result["exercises"]:
    date = datetime.now().strftime(r"%m/%d/%Y")
    time = datetime.now().strftime(r"%X")
    exercise = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]

    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    
    print(f"""
>>> {exercise}
Date: {date}
Time: {time}
Duration: {duration}
Calories: {calories}
    """)