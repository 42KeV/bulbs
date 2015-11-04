from bulbs.resources import connection
from pyramid.view import view_config

@view_config(route_name="admin_home", renderer="admin/home.mako")
#@view_config()
def response(request):

    return {
        "project": request.registry.settings.get("site_name"),
        "title": "Admin Control Panel",
        "session": request.session
    }
