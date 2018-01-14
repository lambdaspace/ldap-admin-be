'''
A CRUD view model for ldap Organisational Units.
'''
from aiohttp import web


__all__ = (ous_list, ous_detail, ous_create, ous_update, ous_delete)


@route('GET', '/ous/')
async def ous_list(request):
    web.Response(text='')


@route('GET', '/ous/{oid}/')
async def ous_detail(request):
    web.Response(text='')


@route('POST', '/ous/')
async def ous_create(request):
    web.Response(text='')


@route('PUT', '/ous/{oid}/')
async def ous_update(request):
    web.Response(text='')


@route('DELETE', '/ous/{oid}/')
async def ous_delete(request):
    web.Response(text='')
