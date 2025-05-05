import asyncio

from api.get_new_orders import get_new_orders
from create_bot import bot


async def check_orders():
    while True:
        orders = await get_new_orders()
        if orders:
            for order in orders:
                text = '<b>Ваш заказ</b>\n\n'
                text += (f'<b>Данные</b>\n'
                        f'<b>ФИО: {order["fullname"]}</b>\n'
                        f'<b>Номер телефона:</b> {order["phone_number"]}\n'
                        f'<b>Адрес:</b> {order["delivery_address"]}\n\n')
                text += '<b>Товары:</b>\n'
                items_order = order['items']
                total_count = 0
                for item in items_order:
                    text += (f'* {item["brand"]} {item["name"]}, цвет - {item["color"]}, размер - {item["size"]}\n'
                             f'   Цена шт - {item["price"]}\n'
                             f'   Количество - {item["quantity"]}\n')
                    total_count += item["price"] * item["quantity"]
                text += (f'\nИтоговая цена:\n'
                         f'<b>{total_count} рублей</b>')
                await bot.send_message(chat_id=order['user_tg_id'], text=text)

        await asyncio.sleep(10)
