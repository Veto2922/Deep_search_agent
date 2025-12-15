from langchain.agents import create_agent
from .llms import get_llm


from .tools import get_unread_emails , send_me_email


EMAIL_TOOLS_LIST = [get_unread_emails , send_me_email]






def get_email_agent(query: str):
    model  = get_llm()
    agent = create_agent(
    model=model,
    tools=EMAIL_TOOLS_LIST,
    system_prompt="You are a helpful assistant for managing my emails inbox for generating, sending and reading emails. use tools to help you and answer my questions",
    )

    # Run the agent
    response = agent.invoke(
    {"messages": [{"role": "user", "content": query}]}
    )


    return response
    