import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = ''
auth_token = ''

stock_api_endpoint = "https://www.alphavantage.co/query"
stock_api_parameters = {"function": "TIME_SERIES_DAILY",
                        "symbol": STOCK,
                        "apikey": "",
                        }

news_api_endpoint = "https://newsapi.org/v2/everything"

news_api_parameters = {"q": COMPANY_NAME,
                       "apiKey": "",
                       "sortBy": "publishedAt"}

# Verifying the fluctuations in tesla's stock price (An increase or decrease of 5% sends out a text
data = requests.get(url=stock_api_endpoint, params=stock_api_parameters).json()["Time Series (Daily)"]

# Using list comprehension to convert the dict to list and extract a list of values
data_list = [value for (key, value) in data.items()]
latest_data = data_list[0]
latest_closing_price = float(latest_data['4. close'])

previous_day_data = data_list[1]
previous_day_closing_price = float(previous_day_data['4. close'])
up_down = None
difference = (latest_closing_price - previous_day_closing_price)
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
percentage_change = round((difference / latest_closing_price) * 100)

# Getting top news from sources related to tesla stocks, that may have lead to stock price changes
if abs(percentage_change) >= 1:
    data = requests.get(url=news_api_endpoint, params=news_api_parameters).json()['articles']
    top_articles = data[:3]
    formatted_articles = [f"{STOCK}:{up_down}{percentage_change}%\nHeadline: {article['title']}\nBrief: {article['description']}" for article in top_articles]
    for article in formatted_articles:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=article,
                from_='',
                to=''
        )
        print(message.status)
