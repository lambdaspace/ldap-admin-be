'''
A CRUD view model for ldap Users.
'''
from aiohttp import web


__all__ = (users_list, users_detail, users_create, users_update, users_delete)


@route('GET', '/users/')
async def users_list(request):
    web.Response(text='')


@route('GET', '/users/{uid}/')
async def users_detail(request):
    web.Response(text='')


@route('POST', '/users/')
async def users_create(request):
    web.Response(text='')


@route('PUT', '/users/{uid}/')
async def users_update(request):
    web.Response(text='')


@route('DELETE', '/users/{uid}/')
async def users_delete(request):
    web.Response(text='')
