from internal.domain.message_stats import MessageStats
from internal.ports.message_stats_repository import MessageStatsRepository


class MessageStatsService:
    def __init__(self, repository: MessageStatsRepository):
        self._repo = repository

    async def add_stats(self, stats: MessageStats) -> MessageStats:
        return await self._repo.add(stats)

    async def get_by_chat(self, chat_id: str) -> list[MessageStats]:
        return await self._repo.get_by_chat(chat_id)
