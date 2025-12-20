from langchain.agents import create_agent
from .llms import get_llm
from .tools import read_and_send_emails , research_and_write_email , generate_email_message , get_unread_emails , send_me_email 



EMAIL_TOOLS_LIST = [get_unread_emails , send_me_email ]






def get_email_agent(query: str):
    model  = get_llm(provider = "google")
    agent = create_agent(
                model=model,
                tools=EMAIL_TOOLS_LIST,
                system_prompt="You are a helpful assistant for managing my emails inbox for generating, sending and reading emails. use tools to help you and answer my questions. If the user requests to send an email without confirmation, proceed to call the send tool immediately.",
                # name = "email_agent"
    )

    # Run the agent
    response = agent.invoke(
    {"messages": [{"role": "user", "content": query}]}
    )

    return response["messages"][-1].text

def get_research_agent(query: str):
    model  = get_llm(provider = "google")
    agent = create_agent(
                model=model,
                tools=[generate_email_message],
                system_prompt="You are a helpful assistant for preparing email data",
                # name = "research_agent"
    )

    # Run the agent
    response = agent.invoke(
    {"messages": [{"role": "user", "content": query}]}
    )

    return response["messages"][-1].text



def get_supervisor_agent(query: str):

    llm = get_llm(provider = "google")
    SUPERVISOR_PROMPT = (
    "You are a helpful personal assistant. "
    "You can read and send emails. and research and write email data "
    "Break down user requests into appropriate tool calls and coordinate the results. "
    "When a request involves multiple actions, use multiple tools in sequence. "
    "IMPORTANT: If the user asks to write/research an email and then send it, you MUST first call research_and_write_email to get the content. "
    "Then, includes that content in the query to read_and_send_emails. Do NOT call them in parallel."
    )

    supervisor_agent = create_agent(
        llm,
        tools=[research_and_write_email , read_and_send_emails],
        system_prompt=SUPERVISOR_PROMPT,
    )

    # Run the agent
    # for step in supervisor_agent.stream(
    # {"messages": [{"role": "user", "content": query}]}
    # ):
    #     for update in step.values():
    #         for message in update.get("messages", []):
    #             message.pretty_print()

    response = supervisor_agent.invoke(
    {"messages": [{"role": "user", "content": query}]}
    )

    return response["messages"][-1].text
