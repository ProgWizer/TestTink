import asyncio
from aiogram import Bot, Dispatcher
from tinkoff_portfolio_bot.config import TELEGRAM_TOKEN
from tinkoff_portfolio_bot.handlers import router

async def main():
    bot = Bot(token=TELEGRAM_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    print("✅ Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
