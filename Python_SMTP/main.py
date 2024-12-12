import smtplib
import datetime as dt
import random

My_email="aloysiousmicheal@gmail.com"
password="lkoz ysfq dmgx cuuy"

now=dt.datetime.now()
week_day=now.weekday()
print(week_day)
if week_day == 3:
    with open("quotes.txt","r", encoding="utf-8") as quote_file:
        all_quotes = quote_file.readlines()
        quote=random.choice(all_quotes)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(My_email,password)
        connection.sendmail(from_addr=My_email,to_addrs=My_email,msg=f"Subject: Monday Motivation\n\n {quote}".encode("utf-8"))



























# import smtplib
#
#
# my_email="gdemo6693@gmail.com"
# password="12345mnbvc"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,to_addrs="aloysiousmicheal@gmail.com",msg="Hello")

#
# import datetime as dt
#
# now=dt.datetime.now()
# week=now.weekday()
# print(now.year)
# print(week)
# d_o_b=dt.datetime(year=2003,month=3,day=29,hour=4)
# print(d_o_b)
