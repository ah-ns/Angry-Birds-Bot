from twilio.rest import Client
import keys

def text_whisper(message_body):
    client = Client(keys.twilio_account_sid, keys.twilio_auth_token)

    country_ISO = input("""Enter the 2-letter ISO of 
                the country your phone number is from:""")
    target_number = input("Enter your phone number (without country code): ")

    message = client.message.create(
        body=message_body,
        from_=keys.twilio_number,
        to=keys.country_codes[country_ISO] + target_number
    )

    print(message.sid)