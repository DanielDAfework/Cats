from twilio.rest import Client
import requests
import os
from boto.s3.connection import S3Connection
import schedule 
import time

def ShipCat():
    print("Starting to ship cat")
    catImage = requests.get('https://api.thecatapi.com/v1/images/search').json()[0]['url']

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=os.environ['TO'],
        from_=os.environ['FROM'],
        body="Free Cat :)",
        media_url=catImage,
    )
    print("Cat Should be Shipped!")
schedule.every(60).minutes.do(ShipCat)

while 1:
    schedule.run_pending()
    time.sleep(1)
