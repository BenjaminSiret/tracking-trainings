import requests
import datetime as dt
import os

APP_ID = "88024513"
APP_KEY = "6c86ddf522410b2decf66097d54f1ad6"
GENDER = "male"
AGE = 41
WEIGHT = 63.5
HEIGHT = 176.0

SHEETY_USERNAME = "ben"
SHEETY_PASSWORD = "5oU1Pz%6aaTb%arx"

# Get the exercise from user
user_input = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0",

}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

parameters = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}


# get the response from Nutritionix-API
response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()['exercises'][0]

# Set results
exercise = result['name']
duration = round(result['duration_min'])
calories = round(result['nf_calories'])

# Set date time
today = dt.datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_time = today.time().strftime("%X")

# # Add row to Sheety
sheety_endpoint = "https://api.sheety.co/0f7781c48bb92afd4adddedb39036b68/workoutTraining/workouts"

sheety_headers = {
    "username": SHEETY_USERNAME,
    "password": SHEETY_PASSWORD,
    "Authorization": "Basic YmVuOjVvVTFQeiU2YWFUYiVhcng",
}
content = {
    "workout": {
        "date": today_date,
        "time": today_time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}


response = requests.post(url=sheety_endpoint, json=content, headers=sheety_headers)
response.raise_for_status()


