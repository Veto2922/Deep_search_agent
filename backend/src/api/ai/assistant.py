

from typing import final
from .llms import get_llm
from .schemas import EmailMessage

from .tools import get_unread_emails , send_me_email

EMAIL_TOOLS = {
    "get_unread_emails": get_unread_emails,
    "send_me_email": send_me_email
}



def email_assistant(query: str) -> EmailMessage:

    llm= get_llm()
    llm= llm.bind_tools(list(EMAIL_TOOLS.values()))

    message = [
    (
        "system",
        "You are a helpful assistant for managing my emails inbox. use tools to help you and answer my questions"
    ),
    (
        "user",
        f"{query}"
    )
    ]
    response = llm.invoke(message)
    message.append(response)

    if hasattr(response , "tool_calls") and response.tool_calls:
        print("tool_calls")
        for tool_call in response.tool_calls:
            tool_name = tool_call.get("name")
            print("tool_name : ", tool_name)
            tool_args = tool_call.get("args")
            tool_func = EMAIL_TOOLS.get(tool_name)
            print("tool_func : ", tool_func)
            if not tool_func:
                continue
            tool_result = tool_func.invoke(tool_args)
            message.append(tool_result)
        
        final_response = llm.invoke(message)
        return final_response
    
    return response

if __name__ == "__main__":
    print(email_assistant("show me my latest emails"))


