'''
A CRUD view model for ldap objectClasses.
'''
from aiohttp import web
from aiohttp_route import route
from json.decoder import JSONDecodeError
from ldap3.core.exceptions import LDAPObjectClassError


@route('GET', '/{object_class}/')
async def objectclass_list(request):
    request.app['ldap'].search(
        'dc=example,dc=com',
        '(objectClass={})'.format(request.match_info['object_class']),
        attributes='*'
    )
    return web.json_response([
        entry.entry_attributes_as_dict
        for entry in request.app['ldap'].entries
    ])


@route('POST', '/{object_class}/')
async def objectclass_create(request):
    try:
        body = await request.json()
        success = request.app['ldap'].add(
            body['dn'],
            [request.match_info['object_class']],
            body['attributes']
        )
    except (KeyError, JSONDecodeError, LDAPObjectClassError):
        raise web.HTTPBadRequest()
    if not success:
        raise web.HTTPBadRequest(text=str(request.app['ldap'].result))
    return web.HTTPCreated()


@route('DELETE', '/{object_class}/{oid}/')
async def users_delete(request):
    try:
        success = request.app['ldap'].delete(
            'cn={},dc=example,dc=com'.format(request.match_info['oid'])
        )
    except (IndexError, KeyError, LDAPObjectClassError) as err:
        raise web.HTTPBadRequest(text=str(err))
    if not success:
        raise web.HTTPBadRequest(text=str(request.app['ldap'].result))
    return web.HTTPNoContent()
