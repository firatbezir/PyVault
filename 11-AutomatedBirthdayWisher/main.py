import datetime as dt
import random
import pandas as pd
import smtplib

today = dt.datetime.now()
year, month, day = today.year, today.month, today.day

birthday_df = pd.read_csv("birthdays.csv")
date_data = birthday_df.to_dict(orient="records")

EMAIL = "your email comes here"
PASSWORD = "your password will come here, check the link for gmail"

#link: https://myaccount.google.com/
# Enable 2-Step Verification
# Find the App Password and create one for this app.


for person in date_data:
    if person["month"] == month and person["day"] == day:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
            letter = file.read()
            name = date_data[0]["name"]
            letter = letter.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="recipientemail@mail.com",
                msg=f"Subject: Happy Birthday from X Person\n\n{letter}"
            )
        print("Mail has sent!")
