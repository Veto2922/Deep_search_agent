from _interpchannels import create
from sqlmodel import SQLModel, Field , DateTime
from datetime import datetime  , timezone

def get_utc_now():
    return datetime.now(timezone.utc)

class ChatMessagePayload(SQLModel):
    message: str 



class ChatMessages(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(
                                default_factory=get_utc_now , 
                                sa_type = DateTime(timezone = True),
                                primary_key=False,
                                nullable=True
                                
                                )
    message: str 


class ChatMessageList(SQLModel):
    id: int | None = Field(default=None)
    message:str
    created_at: datetime = Field(
                                default= None
                                )       