'''
A CRUD view model for ldap Users.
'''
from aiohttp import web
from aiohttp_route import route


@route('GET', '/users/')
async def users_list(request):
    return web.Response(text='')


@route('GET', '/users/{uid}/')
async def users_detail(request):
    return web.Response(text='')


@route('POST', '/users/')
async def users_create(request):
    return web.Response(text='')


@route('PUT', '/users/{uid}/')
async def users_update(request):
    return web.Response(text='')


@route('DELETE', '/users/{uid}/')
async def users_delete(request):
    return web.Response(text='')
