from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

@view_config(route_name="logout", renderer="logout.mako")
def main(request):
    try:
        del request.session["user"]
    except KeyError:
        # User was not logged in when he tried to access the logout page
        url = request.route_url("login")
        
        return HTTPFound(location=url)
        
    user_session = request.session
    
    return {
        "project": request.registry.settings.get("site_name"),
        "title": "You have logged out",
        "session": user_session
    }
