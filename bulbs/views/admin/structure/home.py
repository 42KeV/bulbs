from bulbs.resources import connection
from pyramid.view import view_config

@view_config(route_name="admin_struct_home", renderer="admin/structure/home.mako")
def main(request):

    return {
        "project": request.registry.settings.get("site_name"),
        "title": "ACP - Structure management",
        "session": request.session
    }
