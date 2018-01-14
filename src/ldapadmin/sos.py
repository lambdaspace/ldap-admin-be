'''
A CRUD view model for ldap Security Object.
'''
from aiohttp import web


__all__ = (sos_list, sos_detail, sos_create, sos_update, sos_delete)


@route('GET', '/sos/')
async def sos_list(request):
    pass


@route('GET', '/sos/{sid}/')
async def sos_detail(request):
    pass


@route('POST', '/sos/')
async def sos_create(request):
    pass


@route('PUT', '/sos/{sid}/')
async def sos_update(request):
    pass


@route('DELETE', '/sos/{sid}/')
async def sos_delete(request):
    pass
