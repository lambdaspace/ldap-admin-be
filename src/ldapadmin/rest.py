import asyncio

from aiohttp import web
from aiohttp_route import router

from ldapadmin import groups, ous, sos, users


async def get_app():
    app = web.Application()
    router(app, [groups, ous, sos, users])
    return app


def run_dev():
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(get_app())
    web.run_app(app, port=8080, host='127.0.0.1')


if __name__ == '__main__':
    run_dev()
else:
    APP = asyncio.get_event_loop().run_until_complete(get_app())
