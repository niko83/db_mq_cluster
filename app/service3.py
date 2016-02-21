import json
import sys
import time

from aiohttp import web

import amqp
import db
from app import app as my_app

amqp.get_connection()
db.get_connections()


async def handle(request):

    start_time = time.time()
    output = {}

    output = await my_app(
        command_name=request.match_info.get('name', "Anonymous"),
        data={},
    )

    output['time'] = '%.3f ms' % ((time.time() - start_time) * 1000)

    return web.Response(body=json.dumps(output, indent=2).encode('utf-8'))

app = web.Application()
app.router.add_route('GET', '/{name}', handle)

web.run_app(app)
