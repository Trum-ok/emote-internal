from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from internal.domain.message_stats import MessageStats
from internal.infrastructure.models import MessageStatsModel
from internal.ports.message_stats_repository import MessageStatsRepository


class SQLMessageStatsRepository(MessageStatsRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, stats: MessageStats) -> MessageStats:
        model = MessageStatsModel(
            user_id=stats.user_id,
            username=stats.username,
            chat_id=stats.chat_id,
            anger=stats.anger,
            disgust=stats.disgust,
            fear=stats.fear,
            happy=stats.happy,
            neutral=stats.neutral,
            sad=stats.sad,
            surprised=stats.surprised,
        )
        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)
        return MessageStats(
            id=model.id,
            user_id=model.user_id,
            username=model.username,
            chat_id=model.chat_id,
            anger=model.anger,
            disgust=model.disgust,
            fear=model.fear,
            happy=model.happy,
            neutral=model.neutral,
            sad=model.sad,
            surprised=model.surprised,
        )

    async def get_by_chat(self, chat_id: str) -> list[MessageStats]:
        result = await self.session.execute(select(MessageStatsModel).where(MessageStatsModel.chat_id == chat_id))
        models = result.scalars().all()
        return [
            MessageStats(
                id=m.id,
                user_id=m.user_id,
                username=m.username,
                chat_id=m.chat_id,
                anger=m.anger,
                disgust=m.disgust,
                fear=m.fear,
                happy=m.happy,
                neutral=m.neutral,
                sad=m.sad,
                surprised=m.surprised,
            )
            for m in models
        ]
