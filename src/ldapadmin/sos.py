'''
A CRUD view model for ldap Security Object.
'''
from aiohttp import web


__all__ = (sos_list, sos_detail, sos_create, sos_update, sos_delete)


@route('GET', '/sos/')
async def sos_list(request):
    web.Response(text='')


@route('GET', '/sos/{sid}/')
async def sos_detail(request):
    web.Response(text='')


@route('POST', '/sos/')
async def sos_create(request):
    web.Response(text='')


@route('PUT', '/sos/{sid}/')
async def sos_update(request):
    web.Response(text='')


@route('DELETE', '/sos/{sid}/')
async def sos_delete(request):
    web.Response(text='')
