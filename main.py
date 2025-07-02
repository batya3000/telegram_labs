import asyncio
import aioredis
from aiogram import Bot, Dispatcher

from settings import Settings
from application.handlers import start as start_handlers
from application.middlewares.auth import RequireAuth


async def main() -> None:
    cfg = Settings()
    bot = Bot(cfg.BOT_TOKEN)
    dp = Dispatcher()

    redis = await aioredis.from_url(cfg.REDIS_DSN, decode_responses=True)

    dp["settings"] = cfg
    dp["redis"] = redis

    dp.message.middleware(RequireAuth(redis))
    dp.include_router(start_handlers.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())