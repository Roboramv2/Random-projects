import os
from twilio.rest import Client

tono = 'your mobile number'
frono = 'twilio appointed number'

def makecall():
    account_sid = '__insert twilio account__'
    auth_token = '__insert twilio authentication__'
    client = Client(account_sid, auth_token)

    client.calls.create(url='http://demo.twilio.com/docs/voice.xml',to=tono,from_=frono)

makecall()