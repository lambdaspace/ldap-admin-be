'''
A CRUD view model for ldap Groups.
'''
from aiohttp import web
from aiohttp_route import route


@route('GET', '/groups/')
async def groups_list(request):
    return web.Response(text='')


@route('GET', '/groups/{gid}/')
async def groups_detail(request):
    return web.Response(text='')


@route('POST', '/groups/')
async def groups_create(request):
    return web.Response(text='')


@route('PUT', '/groups/{gid}/')
async def groups_update(request):
    return web.Response(text='')


@route('DELETE', '/groups/{gid}/')
async def groups_delete(request):
    return web.Response(text='')
