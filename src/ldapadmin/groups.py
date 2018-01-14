'''
A CRUD view model for ldap Groups.
'''
from aiohttp import web


__all__ = (groups_list, groups_detail, groups_create, groups_update, groups_delete)


@route('GET', '/groups/')
async def groups_list(request):
    web.Response(text='')


@route('GET', '/groups/{gid}/')
async def groups_detail(request):
    web.Response(text='')


@route('POST', '/groups/')
async def groups_create(request):
    web.Response(text='')


@route('PUT', '/groups/{gid}/')
async def groups_update(request):
    web.Response(text='')


@route('DELETE', '/groups/{gid}/')
async def groups_delete(request):
    web.Response(text='')
