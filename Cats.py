from twilio.rest import Client
import requests
import os
import schedule 
import time
import sys

def ShipCat():
    print("Starting to ship cat")
    sys.stdout.flush()
    catImage = requests.get('https://api.thecatapi.com/v1/images/search').json()[0]['url']

    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=os.environ.get('TO'),
        from_=os.environ.get('FROM'),
        body="Free Automated Cat From Daniel <3",
        media_url=catImage,
    )
    print("Cat Should be Shipped!")
    sys.stdout.flush()

schedule.every().hour.at(":52").do(ShipCat)
print("Application Starting!")
sys.stdout.flush()

while 1:
    schedule.run_pending()
    time.sleep(1)
