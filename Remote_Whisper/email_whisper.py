import keys, smtplib, ssl

def send_email(username: str, text: str):
    password = input(f"Enter the password for {keys.email_sender}: ")

    try:
        server = smtplib.SMTP(keys.smtp_server, keys.port)
        # Create secure connection
        server.starttls(context=ssl.create_default_context())
        server.login(keys.email_sender, password)

        message = f"""\
Subject: Whisper from {username}


{text}
"""

        server.sendmail(keys.email_sender, keys.email_recipient, message)
    except Exception:
        print(Exception)