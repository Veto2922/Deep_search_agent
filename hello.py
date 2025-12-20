from backend.src.api.ai.assistant import email_assistant


from backend.src.api.ai.agents import get_email_agent
from backend.src.api.ai.agents import get_supervisor_agent


from backend.src.api.ai.llms import get_llm

print(get_supervisor_agent("write email for how the ware up early can effict our health   and send it to my email and send it without my confirmation"))

# llm = get_llm(provider="google")

# response = llm.invoke("Hello, how are you?")

# print(response)