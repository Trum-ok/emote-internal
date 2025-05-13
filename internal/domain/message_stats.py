from dataclasses import dataclass


@dataclass
class MessageStats:
    id: int | None
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
