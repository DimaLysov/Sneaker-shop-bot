from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo

from src.keyboards.Kb_inline.inline_main import main_menu

commands_router = Router()


@commands_router.message(Command('start'))
async def cmd_start(m: Message):
    await m.answer(text='Добро пожаловать в наш магазин\n\nПерейдите в приложение, чтобы оформить заказ')


@commands_router.message(Command('catalog'))
async def cmd_catalog(m: Message):
    await m.answer(text='Каталог товаров', reply_markup=main_menu())
