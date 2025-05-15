from config import API_URL
import aiohttp


# async def get_new_orders():
#     async with aiohttp.ClientSession() as session:
#         async with session.get(f"{API_URL}/api/orders/new-order/") as resp:
#             orders = await resp.json()
#             return orders
#
async def get_new_orders():
    connector = aiohttp.TCPConnector(ssl=False)  # Отключает проверку SSL
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(f"{API_URL}api/orders/new-order/") as resp:
            orders = await resp.json()
            return orders
