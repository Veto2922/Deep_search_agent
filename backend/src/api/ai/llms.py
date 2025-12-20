import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chat_models import init_chat_model

load_dotenv()



OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL") or None
OPENAI_MODEL_NAME = os.environ.get("OPENAI_MODEL_NAME") or "ai/qwen3:0.6B-F16"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

if not OPENAI_API_KEY:
    raise NotImplementedError("`OPENAI_API_KEY` is required")

openai_params = {
    "model": OPENAI_MODEL_NAME,
    "api_key": OPENAI_API_KEY,
}

print("OPENAI_BASE_URL : ", OPENAI_BASE_URL)

if OPENAI_BASE_URL:
    openai_params["base_url"] = OPENAI_BASE_URL

def get_llm(provider: str = "openai"):
    if provider == "openai":
        return ChatOpenAI(**openai_params)
    elif provider == "google":
        model = init_chat_model(
            "google_genai:gemini-2.5-flash-lite",
            api_key=GOOGLE_API_KEY,
        )
        return model







