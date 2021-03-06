import asyncio
import aiohttp_cors

from aiohttp import web
from aiohttp_route import router
from ldap3 import Connection, Server

from ldapadmin import crud


async def get_app():
    app = web.Application()
    routes = router(app, [crud])

    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*"
        )
    })

    for route in routes:
        cors.add(route)

    app['ldap'] = Connection(
        Server('openldap'),
        user="cn=admin,dc=example,dc=com",
        password="admin", auto_bind=True
    )
    return app


def run_dev():
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(get_app())
    web.run_app(app, port=8080, host='127.0.0.1')


if __name__ == '__main__':
    run_dev()
else:
    APP = asyncio.get_event_loop().run_until_complete(get_app())
