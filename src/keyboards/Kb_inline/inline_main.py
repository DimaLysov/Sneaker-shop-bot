from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu():
    inline_kb_list = [
        [InlineKeyboardButton(text='Кроссовки', callback_data='call_main_sneakers'),
         InlineKeyboardButton(text='Техника', callback_data='call_main_tech')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def main_sneakers():
    builder = InlineKeyboardBuilder()
    # тут должен быть запрос к бд
    list_brand = ['Nike', 'Adidas', 'Asics']
    for brand in list_brand:
        builder.row(InlineKeyboardButton(text=f'{brand}', callback_data=f'call_brand_{brand}'))
    builder.row(InlineKeyboardButton(text='Ввести свое название', callback_data='call_brand_mine'))
    builder.row(InlineKeyboardButton(text='Назад', callback_data='call_back_main_menu'))
    return builder.as_markup()

def main_tech():
    inline_kb_list = [
        [InlineKeyboardButton(text='Нет в наличии', callback_data='call'),
         InlineKeyboardButton(text='Назад', callback_data='call_back_main_menu')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)