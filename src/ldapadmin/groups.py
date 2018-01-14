'''
A CRUD view model for ldap Groups.
'''
from aiohttp import web


__all__ = (groups_list, groups_detail, groups_create, groups_update, groups_delete)


@route('GET', '/groups/')
async def groups_list(request):
    pass


@route('GET', '/groups/{gid}/')
async def groups_detail(request):
    pass


@route('POST', '/groups/')
async def groups_create(request):
    pass


@route('PUT', '/groups/{gid}/')
async def groups_update(request):
    pass


@route('DELETE', '/groups/{gid}/')
async def groups_delete(request):
    pass
