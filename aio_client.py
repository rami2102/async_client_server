import aiohttp
import asyncio
from datetime import datetime

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def get_test():
    async with aiohttp.ClientSession() as session:
        res = await fetch(session, 'http://127.0.0.1:8080/msg')
        print(res)

if __name__ == "__main__":

    now = datetime.now()
    str_timestamp1 = datetime.timestamp(now)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*[get_test() for i in range(10)]))

    now = datetime.now()
    str_timestamp2 = datetime.timestamp(now)

    print("total elapsed time=" + str(str_timestamp2 - str_timestamp1))
