from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.catalog.router import router as CatalogRouter
from app.users.router import router as UsersRouter
from redis import asyncio as aioredis
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from app.utilits import universal_key_builder

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}")
    FastAPICache.init(RedisBackend(redis), prefix="cache", key_builder=universal_key_builder)
    yield

app = FastAPI(
    title='SteelStore API',
    version='0.1',
    docs_url=None if settings.DEBUG == False else '/docs',
    redoc_url=None if settings.DEBUG == False else '/redoc',
    lifespan=lifespan
)

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins ,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS', 'DELETE', 'PATCH', 'PUT'],
    allow_headers=['Content-Type', 'Set-Cookie', 'Access-Control-Allow-Headers',
                   'Access-Control-Allow-Origin',
                   'Authorization'],
)

app.mount('/static', StaticFiles(directory='app/static'), 'static')
app.include_router(UsersRouter)
app.include_router(CatalogRouter)
