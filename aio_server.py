from aiohttp import web
from datetime import datetime
import asyncio

async def handle(request):
    msg = request.match_info.get('message', "default")

    await asyncio.sleep(10)

    now = datetime.now()
    str_timestamp = str(datetime.timestamp(now))
    res = msg + " timestamp=" + str_timestamp

    return web.Response(text=res)

if __name__ == "__main__":
    app = web.Application()
    app.add_routes([web.get('/', handle),
                    web.get('/{message}', handle)])

    web.run_app(app)