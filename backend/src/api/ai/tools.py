from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig
from api.myemailer.sender import send_email
from api.myemailer.inbox_reader import read_inbox

from .services import generate_email_message as generate_email_message_service

@tool
def generate_email_message(query: str , config: RunnableConfig)-> str:
    """
    Generate an email message based on the given query.

    Args:
        query:str- The query to generate an email message for
    """
    try:

        message = generate_email_message_service(query)
        return f"Subject: {message.subject}\nContent: {message.contents}"
    except Exception as e:
        return f"Failed to generate email message: {str(e)}"

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



# Wrap sub-agents as tools
@tool
def read_and_send_emails(query: str):
    """
    Read and send emails
    Args:
        query:str- The query to read and send emails
    """
    from .agents import get_email_agent  # Import here to avoid circular import
    try:
        email_agent = get_email_agent(query)
        return email_agent
    except Exception as e:
        return f"Failed to read and send emails: {str(e)}"

@tool
def research_and_write_email(query: str):
    """
    Research and write email data
    Args:
        query:str- The query to research and write email data
    """
    from .agents import get_research_agent  # Import here to avoid circular import
    try:
        research_agent = get_research_agent(query)
        return research_agent
    except Exception as e:
        return f"Failed to research and write email data: {str(e)}"
    