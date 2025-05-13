from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from internal.infrastructure.sa_base import Base


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    tg: Mapped[str | None] = mapped_column(String, nullable=True)
    chats: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String, default="unpaid")


class MessageStatsModel(Base):
    __tablename__ = "msgs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[str] = mapped_column(String, nullable=False, index=True)
    username: Mapped[str] = mapped_column(String, nullable=False)
    chat_id: Mapped[str] = mapped_column(String, nullable=False, index=True)
    anger: Mapped[int] = mapped_column(Integer, nullable=False)
    disgust: Mapped[int] = mapped_column(Integer, nullable=False)
    fear: Mapped[int] = mapped_column(Integer, nullable=False)
    happy: Mapped[int] = mapped_column(Integer, nullable=False)
    neutral: Mapped[int] = mapped_column(Integer, nullable=False)
    sad: Mapped[int] = mapped_column(Integer, nullable=False)
    surprised: Mapped[int] = mapped_column(Integer, nullable=False)
