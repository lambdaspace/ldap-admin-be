'''
A CRUD view model for ldap objectClasses.
'''
from json.decoder import JSONDecodeError
from aiohttp import web
from aiohttp_route import route
from ldap3.core.exceptions import LDAPObjectClassError


@route('GET', '/objects/{object_class}/')
async def objects_list(request):
    try:
        success = request.app['ldap'].search(
            'dc=example,dc=com',
            '(objectClass={})'.format(request.match_info['object_class']),
            attributes='*'
        )
    except KeyError:
        raise web.HTTPBadRequest()
    if not success:
        raise web.HTTPNotFound()
    return web.json_response([
        entry.entry_attributes_as_dict
        for entry in request.app['ldap'].entries
    ])

@route('GET', '/objects/{object_class}/{oid}/')
async def objectcs_detail(request):
    try:
        success = request.app['ldap'].search(
            'cn={},dc=example,dc=com'.format(request.match_info['oid']),
            '(objectClass={})'.format(request.match_info['object_class']),
            attributes='*'
        )
    except KeyError:
        raise web.HTTPBadRequest()
    if not success:
        raise web.HTTPNotFound()
    return web.json_response([
        entry.entry_attributes_as_dict
        for entry in request.app['ldap'].entries
    ])

@route('POST', '/objects/{object_class}/')
async def objects_create(request):
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


@route('DELETE', '/objects/{object_class}/{oid}/')
async def objects_delete(request):
    try:
        success = request.app['ldap'].delete(
            'cn={},dc=example,dc=com'.format(request.match_info['oid'])
        )
    except (KeyError, LDAPObjectClassError) as err:
        raise web.HTTPBadRequest(text=str(err))
    if not success:
        raise web.HTTPBadRequest(text=str(request.app['ldap'].result))
    return web.HTTPNoContent()

@route('GET', '/schemas/{object_class}/')
async def schemas_detail(request):
    try:
        object_class = request.match_info['object_class']
    except KeyError:
        raise web.HTTPBadRequest()
    try:
        elements = request.app['ldap'].server.schema.object_classes[object_class].may_contain
    except KeyError:
        raise web.HTTPNotFound()
    else:
        return web.json_response(elements)

@route('GET', '/schemas/')
async def schemas_list(request):
    return web.json_response(list(request.app['ldap'].server.schema.object_classes.keys()))
