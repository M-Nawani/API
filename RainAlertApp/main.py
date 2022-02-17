import requests
from twilio.rest import Client

api_key = ''
account_sid = ''
auth_token = ''

endpoint = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    'lat': 34.816800,
    'lon': 32.398270,
    'appid': api_key,
    'exclude': 'daily,minutely,current'

}

response = requests.get(url=endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = (hour_data['weather'][0]['id'])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, don't forget to carry an umbrella ☔️ ",
        from_='+19362431037',
        to='+91-9920295890'
    )
    print(message.status)
