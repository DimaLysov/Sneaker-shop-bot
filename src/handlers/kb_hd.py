from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.Kb_inline.inline_main import main_sneakers, main_tech, main_menu

kb_hd_router = Router()


@kb_hd_router.callback_query(F.data == 'call_back_main_menu')
async def back_main_menu_call(call: CallbackQuery):
    await call.message.edit_reply_markup(str(call.message.message_id), reply_markup=main_menu())


@kb_hd_router.callback_query(F.data == 'call_main_sneakers')
async def main_sneakers_call(call: CallbackQuery):
    await call.message.edit_reply_markup(str(call.message.message_id), reply_markup=main_sneakers())


@kb_hd_router.callback_query(F.data == 'call_main_tech')
async def main_tech_call(call: CallbackQuery):
    await call.message.edit_reply_markup(str(call.message.message_id), reply_markup=main_tech())
