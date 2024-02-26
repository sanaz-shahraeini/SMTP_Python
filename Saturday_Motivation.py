from datetime import datetime
import smtplib
import random

my_email = "ostad7test@gmail.com"
password = "#Your App password in gmail account"

now = datetime.now()
# print(now)
weekday = now.weekday()
if weekday == 5:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        # print(quote)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="ostad7test@yahoo.com",
                        msg=f"Subject:Saturday quote\n\n {quote}"
                        )