from contextlib import asynccontextmanager

from fastapi import FastAPI

from config.loggers import setup_logging
from internal.app.routes import setup_routes
from internal.infrastructure.database import init_db, stop_db

setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    setup_routes(app)
    yield
    await stop_db()


app = FastAPI(title="Emote Internal API", lifespan=lifespan)
