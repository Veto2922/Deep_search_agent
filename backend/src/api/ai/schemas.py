from pydantic import BaseModel ,Field


class EmailMessage(BaseModel):
    subject: str
    contents: str
    invalid_request: bool | None = Field(default=False)