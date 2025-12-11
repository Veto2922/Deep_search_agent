from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session , select
from .models import ChatMessagePayload  ,ChatMessages , ChatMessageList


from api.ai.services import generate_email_message
from api.ai.schemas import EmailMessage
from api.db import get_session
router = APIRouter()


# chat health check
@router.get("/chat/health")
async def chat_health_check():
    return {"message": "ok"}

@router.get("/chat/recent" , response_model=List[ChatMessageList])
async def chat_list_messages(session: Session = Depends(get_session)):
    
    return session.exec(select(ChatMessages).limit(10)).all()


# curl -X POST -d "{"message":"hello"}"" -H "Content-Type: application/json" http://localhost:8070/chat
@router.post("/chat" , response_model=EmailMessage)
async def chat(payload: ChatMessagePayload,
    session: Session = Depends(get_session)):
    data = payload.model_dump()
    print(data)
    obj= ChatMessages.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)

    response = generate_email_message(data["message"])
    return response



