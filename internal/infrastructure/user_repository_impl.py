from sqlalchemy import func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from internal.domain.user import User
from internal.infrastructure.models import UserModel
from internal.ports.user_repository import UserRepository


class SQLUserRepository(UserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, email: str | None = None, telegram: str | None = None) -> User | None:
        stmt = select(UserModel)
        if email and telegram:
            stmt = stmt.where(or_(UserModel.email == email, UserModel.tg == telegram))
        elif email:
            stmt = stmt.where(UserModel.email == email)
        elif telegram:
            stmt = stmt.where(UserModel.tg == telegram)
        else:
            return None
        result = await self.session.execute(stmt)
        model = result.scalars().first()
        if not model:
            return None
        return User(
            id=model.id,
            email=model.email,
            password=model.password,
            tg=model.tg,
            chats=model.chats,
            status=model.status,
        )

    async def get_by_id(self, id: int) -> User | None:
        result = await self.session.execute(select(UserModel).where(UserModel.id == id))
        model = result.scalars().first()
        if not model:
            return None
        return User(
            id=model.id,
            email=model.email,
            password=model.password,
            tg=model.tg,
            chats=model.chats,
            status=model.status,
        )

    async def get_all(self) -> list[User]:
        result = await self.session.execute(select(UserModel))
        models = result.scalars().all()
        return [
            User(
                id=m.id,
                email=m.email,
                password=m.password,
                tg=m.tg,
                chats=m.chats,
                status=m.status,
            )
            for m in models
        ]

    async def count(self) -> int:
        result = await self.session.execute(select(func.count(UserModel.id)))
        return result.scalar_one()

    async def create(self, user: User) -> User:
        model = UserModel(
            email=user.email,
            password=user.password,
            tg=user.tg,
            chats=user.chats,
            status=user.status,
        )
        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)
        return User(
            id=model.id,
            email=model.email,
            password=model.password,
            tg=model.tg,
            chats=model.chats,
            status=model.status,
        )

    async def update(self, user: User) -> User:
        result = await self.session.execute(select(UserModel).where(UserModel.id == user.id))
        model = result.scalars().first()
        if not model:
            return None
        model.email = user.email or model.email
        model.password = user.password or model.password
        model.tg = user.tg or model.tg
        model.chats = user.chats or model.chats
        model.status = user.status or model.status
        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)
        return User(
            id=model.id,
            email=model.email,
            password=model.password,
            tg=model.tg,
            chats=model.chats,
            status=model.status,
        )
