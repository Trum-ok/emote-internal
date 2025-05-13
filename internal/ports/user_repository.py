from abc import ABC, abstractmethod

from internal.domain.user import User


class UserRepository(ABC):
    @abstractmethod
    async def get(self, email: str | None = None, telegram: str | None = None) -> User | None:
        """Получение пользователя по email или telegram."""

    @abstractmethod
    async def get_by_id(self, id: int) -> User | None:
        """Получение пользователя по id."""

    @abstractmethod
    async def get_all(self) -> list[User]:
        """Получение всех пользователей."""

    @abstractmethod
    async def count(self) -> int:
        """Получение количества пользователей (всех)."""

    @abstractmethod
    async def create(self, user: User) -> User:
        """Создание нового пользователя."""

    @abstractmethod
    async def update(self, user: User) -> User:
        """Обновление пользователя."""
