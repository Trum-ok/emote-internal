from logging import getLogger

from fastapi import FastAPI

from config.loggers import ROUTERS

from .messages import messages_router
from .users import user_router

routers = [messages_router, user_router]
__all__ = ("routers", "setup_routes")

logger = getLogger(ROUTERS)


def setup_routes(app: FastAPI) -> None:
    for router in routers:
        app.include_router(router)
    logger.info("Setuped routers: %s", [router.prefix for router in routers])
