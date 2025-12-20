import os
from api.myemailer.gmail_imap_parser import GmailImapParser

# pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")


def read_inbox(hours: int = 24, unread_only: bool = True , verbose: bool = False):
    parser = GmailImapParser(
        email_address=EMAIL_HOST_USER,
        app_password=EMAIL_HOST_PASSWORD
    )

    # Fetch unread emails from last 24 hours
    emails = parser.fetch_emails(hours=hours, unread_only=unread_only)

    if verbose:
        for email in emails:
            print(f"From: {email['from']}")
            print(f"Subject: {email['subject']}")
            print(f"Date: {email['timestamp']}")
            print("---")
    
    return emails


if __name__ == "__main__":
    emails = read_inbox(verbose=True)
    # print(emails[0])

    for email in emails:
        data = email.copy()
        if "html_body" in data:
            del data["html_body"]
        msg = ""
        for key, value in data.items():
            msg += f"{key}: {value}\n"
        print("the message is :",  msg)
    # print("\n------\n".join(cleaned) )




