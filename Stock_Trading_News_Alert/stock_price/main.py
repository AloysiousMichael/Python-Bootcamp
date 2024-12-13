import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY="63df08836eda4eda861c4101123fb248"

TWILIO_SID="AC1e216059904d1d4d62cd5d9f8ff98be6"
TWILIO_AUTH_TOKEN="443e0b6116d46ae29e40bfdcfa37f45a"

STOCK_API_KEY="AWR1LITRO7ZAP69G"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.


stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey":STOCK_API_KEY,
}

response=requests.get(STOCK_ENDPOINT,params=stock_params)
data=response.json()["Time Series (Daily)"]
data_list= [value for (key,value) in data.items()]
yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data["4. close"]


dayBefore_yesterday_data=data_list[1]
dayBefore_yesterday_data=dayBefore_yesterday_data["4. close"]
difference=float(yesterday_closing_price)-float(dayBefore_yesterday_data)

up_down=None
if difference >0:
    up_down="⬆️"
else:
    up_down="⬇️"



diff_percent=round((difference / float(yesterday_closing_price))*100)


print(yesterday_closing_price)
print(dayBefore_yesterday_data)
print(difference)
print(diff_percent)


if abs(diff_percent) > 1:

    news_params={
        "apiKey": NEWS_API_KEY,
        "qInTitle":COMPANY_NAME,
    }
    news_respones=requests.get("https://newsapi.org/v2/everything",params=news_params)
    articles=news_respones.json()["articles"]
    three_article=articles[:3]

    formatted_list=[f"{STOCK_NAME} : {up_down} {diff_percent} Headline: {article['title']}. \nBrief : {article['description']} "for article in three_article]

    client=Client(TWILIO_SID,TWILIO_AUTH_TOKEN)
    for article in formatted_list:
        message=client.messages.create(
            body=article,
            from_="+12705337722",
            to="+91 8590451899",
            )



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

