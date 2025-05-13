from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from internal.app.schemas import UserCreate, UserRead, UserUpdate
from internal.app.services.user_service import UserService
from internal.infrastructure.database import get_session
from internal.infrastructure.user_repository_impl import SQLUserRepository

user_router = APIRouter(prefix="/users", tags=["Пользователи"])


# Зависимость: сервис пользователей
async def get_user_service(session: AsyncSession = Depends(get_session)) -> UserService:
    repo = SQLUserRepository(session)
    return UserService(repo)


@user_router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserCreate, service: UserService = Depends(get_user_service)):
    return await service.create(user_in)


@user_router.get("/", response_model=list[UserRead])
async def read_users(service: UserService = Depends(get_user_service)):
    return await service.get_all()


@user_router.get("/count", response_model=int)
async def read_users_count(service: UserService = Depends(get_user_service)):
    return await service.count()


@user_router.get("/{user_id}", response_model=UserRead)
async def read_user_by_id(user_id: int, service: UserService = Depends(get_user_service)):
    user = await service.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user


@user_router.get("/search", response_model=UserRead)
async def search_user(
    email: str | None = None, telegram: str | None = None, service: UserService = Depends(get_user_service)
):
    user = await service.get(email=email, telegram=telegram)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user


@user_router.patch("/{user_id}", response_model=UserRead)
async def update_user(user_id: int, user_update: UserUpdate, service: UserService = Depends(get_user_service)):
    existing = await service.get_by_id(user_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    update_data = user_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(existing, field, value)
    return await service.update(existing)
