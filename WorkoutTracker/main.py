import requests
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
GENDER = "female"
WEIGHT_KG = 53
HEIGHT_CM = 167
AGE = 29

nutritionix_url_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint_url = os.environ.get("SHEET_ENDPOINT")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

exercise_tracking_parameters = {
    "query": input("Tell me what exercise did you do today ?"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutritionix_url_endpoint, headers=headers, json=exercise_tracking_parameters)
result = response.json()
today = datetime.now()

for exercise in result['exercises']:
    sheet_data_parameters = {
        "workout": {
            'date': today.strftime("%d/%m/%Y"),
            'time': today.strftime("%X"),
            'exercise': exercise['name'].title(),
            'duration': exercise["duration_min"],
            'calories': exercise["nf_calories"],
        }
    }
    bearer_headers = {
        "Authorization": os.environ.get("TOKEN")
    }
    sheet_response = requests.post(
        sheet_endpoint_url,
        json=sheet_data_parameters,
        headers=bearer_headers
    )
    print(sheet_response.text)
