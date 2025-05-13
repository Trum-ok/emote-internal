from pydantic import BaseModel, EmailStr, Field


# User schemas
class UserBase(BaseModel):
    email: EmailStr
    tg: str | None
    chats: str | None
    status: str | None = Field(default="unpaid")


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    email: EmailStr | None
    password: str | None
    tg: str | None
    chats: str | None
    status: str | None


class UserRead(UserBase):
    id: int


# MessageStats schemas
class MessageStatsBase(BaseModel):
    user_id: str
    username: str
    chat_id: str
    anger: int
    disgust: int
    fear: int
    happy: int
    neutral: int
    sad: int
    surprised: int


class MessageStatsCreate(MessageStatsBase): ...


class MessageStatsRead(MessageStatsBase):
    id: int


class MessageStatsList(BaseModel):
    items: list[MessageStatsRead]
