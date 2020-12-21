# import os
# from twilio.rest import Client
#
# client = Client()
# # num=input("enter a phone number: ")
# from_num = 'whatsapp:+14155238886'
# to_ = 'whatsapp:+918938095294'
#
# client.messages.create(body='hii',
#                        from_=from_num,
#                        to=to_)
from twilio.rest import Client

account_sid = 'AC2337ec5169b913841afcd80d78c003a6'
auth_token = '04d7c79a3cfa593f84fe657417280b38'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Your Twilio code is 1238432',
    to='whatsapp:+919359009773'
)

print(message.sid)