from internal.domain.user import User
from internal.ports.user_repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self._repo = repository

    async def get(self, email: str | None = None, telegram: str | None = None) -> User | None:
        return await self._repo.get(email=email, telegram=telegram)

    async def get_by_id(self, id: int) -> User | None:
        return await self._repo.get_by_id(id)

    async def get_all(self) -> list[User]:
        return await self._repo.get_all()

    async def count(self) -> int:
        return await self._repo.count()

    async def create(self, user: User) -> User:
        return await self._repo.create(user)

    async def update(self, user: User) -> User:
        return await self._repo.update(user)
