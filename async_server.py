#!/usr/bin/python

import time
from sanic import Sanic
from sanic import response
from datetime import datetime

app = Sanic(__name__)


@app.route("/")
async def test(request):
    time.sleep(30)

    now = datetime.now()
    str_timestamp = datetime.timestamp(now)
    # change to received message!
    return response.json({"message": "msg", "timestamp" : str_timestamp})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)