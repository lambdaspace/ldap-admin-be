'''
A CRUD view model for ldap Organisational Units.
'''
from aiohttp import web
from aiohttp_route import route


@route('GET', '/ous/')
async def ous_list(request):
    return web.Response(text='')


@route('GET', '/ous/{oid}/')
async def ous_detail(request):
    return web.Response(text='')


@route('POST', '/ous/')
async def ous_create(request):
    return web.Response(text='')


@route('PUT', '/ous/{oid}/')
async def ous_update(request):
    return web.Response(text='')


@route('DELETE', '/ous/{oid}/')
async def ous_delete(request):
    return web.Response(text='')
