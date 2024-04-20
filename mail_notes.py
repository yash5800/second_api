import smtplib
from email.mime.text import MIMEText
import base64
import urllib.parse


def send_notes_email(email, notes):
    sender_email = "jokerdeva18@gmail.com"
    sender_password = "acnu bsol osui tlps"

    # Create the email message
    message = MIMEText(f"Your Notes : {notes}")
    message["Subject"] = "Sending Notes"
    message["From"] = sender_email
    message["To"] = email

    # Connect to the SMTP server and send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, [email], message.as_string())
        print("sended!")
    return "done"

def decodeBase64(encodedText):
    latin1Text = base64.b64decode(encodedText).decode()
    return urllib.parse.unquote(latin1Text.encode('latin1').decode('utf-8'))
