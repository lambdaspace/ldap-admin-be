'''
A CRUD view model for ldap Organisational Units.
'''
from aiohttp import web


__all__ = (ous_list, ous_detail, ous_create, ous_update, ous_delete)


@route('GET', '/ous/')
async def ous_list(request):
    pass


@route('GET', '/ous/{oid}/')
async def ous_detail(request):
    pass


@route('POST', '/ous/')
async def ous_create(request):
    pass


@route('PUT', '/ous/{oid}/')
async def ous_update(request):
    pass


@route('DELETE', '/ous/{oid}/')
async def ous_delete(request):
    pass
