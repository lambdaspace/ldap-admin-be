'''
A CRUD view model for ldap Users.
'''
from aiohttp import web
from aiohttp_route import route


@route('GET', '/users/')
async def users_list(request):
    request.app['ldap'].search(
        'dc=example,dc=com',
        '(objectClass=person)',
        attributes=['objectClass', 'description', 'cn', 'dc']
    )
    return web.json_response([
        entry.entry_attributes_as_dict
        for entry in request.app['ldap'].entries
    ])


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
