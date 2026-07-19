#twilio.com/try-twilio
from twilio.rest import Client
import os

def sending_sms(text='Wake up Neo...', receiver="+79035057070"):
    try:
        account_sid = os.getenv('SID')
        auth_token = os.getenv("AUTH_TOKEN")

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=text,
            from_='+14055925046',
            to=receiver
        )

        return 'The message was successfully sent!'
    except Exception as ex:
        return 'Something was wrong...', ex



def main():
    text = input("Please enter your message: ")
    sending_sms(text=text, receiver=os.getenv('RECEIVER_PHONE'))


if __name__ == '__main__':
    main()