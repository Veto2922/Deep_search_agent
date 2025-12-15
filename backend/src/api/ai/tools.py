from langchain_core.tools import tool
from backend.src.api.myemailer.sender import send_email
from backend.src.api.myemailer.inbox_reader import read_inbox

@tool
def send_me_email(subject: str, content: str)-> str:
    """
    Send an email to the user with the given subject and content.

    Args:
        subject:str- The subject of the email
        content:str- The content of the email
    """
    try:
        send_email(subject, content)
        return "Email sent successfully"
    except Exception as e:
        return f"Failed to send email: {str(e)}"

@tool
def get_unread_emails(hours: int = 48)-> str:
    """
    Get unread emails from the user's inbox.

    Args:
        hours:int- The number of hours to look for unread emails
    """
    try:
        unread_emails = read_inbox(hours=hours, unread_only=True , verbose=False)
    except Exception as e:
        return f"Failed to get unread emails: {str(e)}"
    
    cleaned = []

    for email in unread_emails:
        data = email.copy()
        if "html_body" in data:
            del data["html_body"]
        msg = ""
        for key, value in data.items():
            msg += f"{key}: {value}\n"
        cleaned.append(msg)
    return "\n------\n".join(cleaned)[:500]
