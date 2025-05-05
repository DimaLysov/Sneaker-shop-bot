from config import API_URL
import aiohttp


async def get_new_orders():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_URL}/api/orders/new-order/") as resp:
            orders = await resp.json()
            return orders
