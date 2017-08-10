#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
async web application.
"""

import logging
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

# 通过logging.basicConfig函数对日志的输出格式进行配置
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='app.log',
                filemode='w')

def index(request):
    return web.Response(body=b'<html><head><title>myapp</title></head><body><h1>Awesome</h1></body></html>', content_type='text/html')
    # return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
