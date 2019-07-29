
from twilio.rest import Client
account_sid= "**************************"
auth_token= "***************************"
client=Client(account_sid,auth_token)
message=client.messages.create(from_='twilio_number',body='hello from twilio',to='your_number')
print(message.sid)
