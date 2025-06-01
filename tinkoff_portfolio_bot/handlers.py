from aiogram import Router
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import CommandStart

from .tinkoff_client import get_portfolio_info

router = Router()

from aiogram.types import (
    Message, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
)

# Создаём WebApp-кнопку
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌐 Открыть веб-интерфейс", web_app=WebAppInfo(url="https://https://progwizer.github.io/TestTink"))],
        [KeyboardButton(text="📊 Мой портфель")]
    ],
    resize_keyboard=True
)









keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📊 Мой портфель")],
        [KeyboardButton(text="🔄 Обновить портфель")]
    ],
    resize_keyboard=True
)




@router.message(CommandStart())
async def handle_start(message: Message):
    user_id = message.from_user.id
    await message.answer(
        f"Привет, пользователь {user_id}!\nВыберите действие:",
        reply_markup=keyboard
    )

@router.message(lambda msg: msg.text in ["📊 Мой портфель", "🔄 Обновить портфель"])
async def handle_portfolio(message: Message):
    user_id = message.from_user.id
    await message.answer("⏳ Загружаю ваш портфель...")

    # пока токен один, но можно расширить
    portfolio = get_portfolio_info(user_id=user_id)
    await message.answer(portfolio)

