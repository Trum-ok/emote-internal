from abc import ABC, abstractmethod

from internal.domain.message_stats import MessageStats


class MessageStatsRepository(ABC):
    @abstractmethod
    async def add(self, stats: MessageStats) -> MessageStats:
        """Добавление статистики сообщения."""

    @abstractmethod
    async def get_by_chat(self, chat_id: str) -> list[MessageStats]:
        """Получение статистики сообщения по chat_id."""
