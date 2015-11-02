from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

@view_config(route_name="logout", renderer="logout.mako")
def main(request):
    try:
        del request.session["identity"]
    except KeyError:
        # User was not logged in when he tried to access the logout page
        url = request.route_url("login")
        
        return HTTPFound(location=url)
    
    return {
        "project": request.registry.settings.get("site_name"),
        "title": "You have logged out"
    }
