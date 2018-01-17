'''
A CRUD view model for ldap Security Object.
'''
from aiohttp import web
from aiohttp_route import route


@route('GET', '/sos/')
async def sos_list(request):
    return web.Response(text='')


@route('GET', '/sos/{sid}/')
async def sos_detail(request):
    return web.Response(text='')


@route('POST', '/sos/')
async def sos_create(request):
    return web.Response(text='')


@route('PUT', '/sos/{sid}/')
async def sos_update(request):
    return web.Response(text='')


@route('DELETE', '/sos/{sid}/')
async def sos_delete(request):
    return web.Response(text='')
