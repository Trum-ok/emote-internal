from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from internal.app.schemas import MessageStatsCreate, MessageStatsRead
from internal.app.services.message_stats_service import MessageStatsService
from internal.infrastructure.database import get_session
from internal.infrastructure.message_stats_repository_impl import SQLMessageStatsRepository

messages_router = APIRouter(prefix="/messages", tags=["Статистика сообщений"])


# Зависимость: сервис статистики сообщений
async def get_stats_service(session: AsyncSession = Depends(get_session)) -> MessageStatsService:
    repo = SQLMessageStatsRepository(session)
    return MessageStatsService(repo)


@messages_router.post("/stats/", response_model=MessageStatsRead, status_code=201)
async def add_message_stats(stats_in: MessageStatsCreate, service: MessageStatsService = Depends(get_stats_service)):
    return await service.add_stats(stats_in)


@messages_router.get("/stats/{chat_id}", response_model=list[MessageStatsRead])
async def get_stats(chat_id: str, service: MessageStatsService = Depends(get_stats_service)):
    return await service.get_by_chat(chat_id)
