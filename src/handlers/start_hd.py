from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

start_router = Router()

@start_router.message(Command('start'))
async def cmd_start(m: Message):
    await m.answer(text='Ваш бот работает!')
