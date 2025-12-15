from email.message import EmailMessage
from dotenv import load_dotenv
from smtplib import SMTP_SSL
import os

load_dotenv()

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

def send_email(subject: str = "No subject provided", content: str = "No message provided", to_email: str = EMAIL_HOST_USER , from_email: str = EMAIL_HOST_USER):
    msg = EmailMessage()
    msg.set_content(content)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    with SMTP_SSL(EMAIL_HOST, EMAIL_PORT) as server:
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        return server.send_message(msg)


if __name__ == "__main__":
    send_email("hello", "test from python") 


    