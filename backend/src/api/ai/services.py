
from .llms import get_llm
from .schemas import EmailMessage

def generate_email_message(query: str) -> EmailMessage:

    llm= get_llm(provider="google")
    llm= llm.with_structured_output(EmailMessage)

    message = [
    (
        "system",
        "You are a helpful assistant for research and composing plaintext emails and write the subject and content of the email. Do not use markdown in your response only plaintext"
    ),
    (
        "user",
        f"{query} , Do not use markdown in your response only plaintext"
    )
    ]
    response = llm.invoke(message)
    return response
