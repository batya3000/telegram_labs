import asyncio
from aiogram import Bot, Dispatcher
from settings import Settings
from application.handlers import start as start_handlers

async def main() -> None:
    cfg = Settings()
    bot = Bot(cfg.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(start_handlers.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())