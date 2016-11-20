from twilio.rest import TwilioRestClient

phoneNumbers = ["+16149439420","+12697672584","+16147531396","+16149359401"]

account_sid = "ACb2f28f9135a6746dc076e2a480198e8b"  # Your Account SID from www.twilio.com/console
auth_token  = "5b419b26f9c7847bcbf314db7b2287b3"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

def sendMessage(sendToNumber,message):
    message = client.messages.create(body=message,
        to=sendToNumber,       # Replace with your phone number
        from_="+16789168208")  # Replace with your Twilio number

    print(message.sid)


def sendItOutPlz(number,message):
   # for number in phoneNumbers:
    sendMessage(number,message)
