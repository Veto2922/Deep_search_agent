# Arabic Research Agent

An intelligent, agentic AI coding assistant designed to help with research tasks and email management. Built with **FastAPI**, **LangChain**, and **SQLModel**, this project utilizes a Supervisor Agent architecture to orchestrate tasked based agents for processing user requests efficiently.

## 🚀 Features

-   **Email Management Agent**:
    -   📚 **Read Inbox**: Retrieve and summarize unread emails.
    -   📤 **Send Emails**: Compose and send emails directly.
-   **Research Agent**:
    -   🔍 **Draft Content**: Research topics and draft professional email content based on user queries.
-   **Supervisor Agent**:
    -   🤖 Orchestrates the workflow between the User, Research Agent, and Email Agent.
    -   Ensures sequential execution (e.g., "Research this topic, *then* send the email").
-   **Conversation Memory**: Stores chat history in a PostgreSQL database.

## 🛠️ Tech Stack

-   **Backend**: Python, FastAPI
-   **AI Framework**: LangChain
-   **LLM Providers**: Google Gemini (via `google-genai`) or OpenAI-compatible endpoints.
-   **Database**: PostgreSQL, SQLModel
-   **Package Manager**: `uv` (modern Python package manager)
-   **Containerization**: Docker & Docker Compose

## 📋 Prerequisites

-   **Docker** & **Docker Compose** (Recommended)
-   **Python 3.13+** (for local development)
-   **API Keys**:
    -   `GOOGLE_API_KEY`: For Gemini models.
    -   (Optional) `OPENAI_API_KEY`: If using OpenAI models.
-   **Email Credentials**:
    -   SMTP credentials (e.g., Gmail App Password) for sending/reading emails.

## ⚙️ Configuration

1.  **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd Arabic_research_agent
    ```

2.  **Environment Setup**:
    Copy the example environment file and rename it to `.env`:
    ```bash
    cp .env.example .env
    ```

3.  **Edit `.env`**:
    Open `.env` and fill in the required values:
    ```ini
    # Database Config
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_DB=postgres
    POSTGRES_URL="postgresql://postgres:postgres@db_service:5432/postgres"

    # AI Model Keys
    GOOGLE_API_KEY="your_google_api_key_here"
    OPENAI_API_KEY="your_openai_key_here" # If applicable

    # Email Settings (Gmail Example)
    EMAIL_HOST="smtp.gmail.com"
    EMAIL_PORT=465
    EMAIL_HOST_USER="your_email@gmail.com"
    EMAIL_HOST_PASSWORD="your_app_password" # Use App Password, not login password
    ```

## 🏃‍♂️ Usage

### Option 1: Using Docker (Recommended)

Start the entire application stack:

```bash
docker-compose up --build
```

-   The **API** will be available at: `http://localhost:8070`
-   **Interactive API Docs**: `http://localhost:8070/docs`
-   **Database**: Running on port `5432`.

### Option 2: Local Development

1.  **Install `uv`** (if not installed):
    ```bash
    pip install uv
    ```

2.  **Sync dependencies**:
    ```bash
    uv sync
    ```

3.  **Run the application**:
    Navigate to the source directory and start the server:
    ```bash
    # From project root
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    cd backend/src
    uvicorn main:app --reload --port 8000
    ```

## 🔌 API Endpoints

-   `GET /chat/health`: Health check.
-   `GET /chat/recent`: Retrieve the last 10 chat messages.
-   `POST /chat`: Main endpoint to interact with the agent.
    -   **Payload**: `{"message": "Research about waking up early and send email to me"}`

## 🧪 Testing

You can test the agent using the provided `hello.py` script (ensure your `.env` is set up locally first):

```bash
python hello.py
```
