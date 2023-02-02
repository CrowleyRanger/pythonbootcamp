import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_KEY = "3TGRNKCICRKFZK0Q"
NEWS_KEY = "82c7f5e486874ca58bbf3803d1b1c298"
TWILIO_KEY = "ACb102dde10d045365c46e4374e71582ac"
TWILIO_AUTH_TOKEN = "b02a4d41e966a5ecce920d1389b4d703"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_KEY,
    "outputsize": "compact"
}

news_params = {
    "q": "tesla",
    "apiKey": NEWS_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()

stock_data = response.json()
data = stock_data["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]

today_data = data 

yesterday_data = data_list[0]
yesterday_close_price = float(yesterday_data["4. close"])

before_yesterday_data = data_list[1]
before_yesterday_close_price = float(before_yesterday_data["4. close"])

price_difference = yesterday_close_price - before_yesterday_close_price

up_down = None
if price_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

difference_percent = "%.2f" % float(100*(price_difference/before_yesterday_close_price))

if abs(price_difference) > 0.1:
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    news_data = response.json()
    #First 3 articles
    three_articles = news_data["articles"][:3]

formatted_articles = [f"{STOCK} {up_down}{difference_percent}% \n\nHeadline: {article['title']}\n\nBrief: {article['description']}\n" for article in three_articles]

client = Client(TWILIO_KEY, TWILIO_AUTH_TOKEN)

for article in formatted_articles:
    message = client.messages \
                    .create(
                        body=article,
                        from_='+14243533343',
                        to='+5511972096011'
                    )

print(f"{'%.2f' % difference_percent}%")


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """

