from twilio.rest import Client
import requests
import os
from boto.s3.connection import S3Connection
import schedule 
import time
import sys

def ShipCat():
    print("Starting to ship cat")
    sys.stdout.flush()
    catImage = requests.get('https://api.thecatapi.com/v1/images/search').json()[0]['url']

    account_sid = os.environ('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=os.environ.get('TO'),
        from_=os.environ.get('FROM'),
        body="Free Cat :)",
        media_url=catImage,
    )
    print("Cat Should be Shipped!")
    sys.stdout.flush()

schedule.every(2).minutes.do(ShipCat)
print("Application Starting!")
sys.stdout.flush()

while 1:
    schedule.run_pending()
    time.sleep(1)
